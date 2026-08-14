"""SpecialSkillAI prototype interfaces.

Phase 3 deliberately avoids MaaCore integration. These classes are a typed
contract for the later C++ design: disabled-by-default orchestration,
operator-specific adapters, and a generic target selection path for L2 skills.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterable, Protocol


class SkillOperationLevel(str, Enum):
    L0 = "L0"  # No active action or automatically triggered.
    L1 = "L1"  # Click operator, then click skill.
    L2 = "L2"  # Click skill, then choose a secondary target/tile/object.


@dataclass(frozen=True)
class TargetCandidate:
    location: tuple[int, int] | str
    valid: bool
    threat_score: float = 0.0
    tactical_score: float = 0.0
    reason: str = ""


@dataclass(frozen=True)
class BattlefieldState:
    map_tiles: Any = None
    deployed_operators: dict[str, tuple[int, int]] = field(default_factory=dict)
    summons: dict[str, tuple[int, int]] = field(default_factory=dict)
    enemies: Any = None
    enemy_density: Any = None
    enemy_path: Any = None
    homes: list[tuple[int, int]] = field(default_factory=list)
    available_target_tiles: list[tuple[int, int]] = field(default_factory=list)
    skill_state: dict[str, Any] = field(default_factory=dict)
    current_kill_count: int | None = None
    stage_name: str = ""


@dataclass(frozen=True)
class ExecutionResult:
    acted: bool
    skipped: bool = False
    reason: str = ""
    candidate: TargetCandidate | None = None


@dataclass(frozen=True)
class SpecialSkillAIConfig:
    enable_special_skill_ai: bool = False


class SkillExecutor(Protocol):
    def execute(self, operator_name: str, state: BattlefieldState) -> ExecutionResult:
        ...


class SkillReadinessDetector(Protocol):
    def is_ready(self, operator_name: str, state: BattlefieldState) -> bool:
        ...


class BattlefieldEvaluator(Protocol):
    def evaluate(self, operator_name: str, state: BattlefieldState) -> list[TargetCandidate]:
        ...


class SummonManager(Protocol):
    def known_summons(self, state: BattlefieldState) -> dict[str, tuple[int, int]]:
        ...


class TargetSelector:
    """Choose the highest tactical score among legal target candidates."""

    def select(self, candidates: Iterable[TargetCandidate]) -> TargetCandidate | None:
        legal = [candidate for candidate in candidates if candidate.valid]
        if not legal:
            return None
        return max(legal, key=lambda candidate: (candidate.tactical_score, candidate.threat_score))


class NormalSkillExecutor:
    """Placeholder contract for L1 skills: operator click plus skill click."""

    def execute(self, operator_name: str, state: BattlefieldState) -> ExecutionResult:
        return ExecutionResult(acted=True, reason=f"normal skill execution requested for {operator_name}")


class TargetedSkillExecutor:
    """Generic L2 flow: evaluate battlefield, choose target, then perform targeted action later."""

    def __init__(self, evaluator: BattlefieldEvaluator, selector: TargetSelector | None = None) -> None:
        self.evaluator = evaluator
        self.selector = selector or TargetSelector()

    def execute(self, operator_name: str, state: BattlefieldState) -> ExecutionResult:
        candidate = self.selector.select(self.evaluator.evaluate(operator_name, state))
        if candidate is None:
            return ExecutionResult(acted=False, skipped=True, reason="no valid target candidate")
        return ExecutionResult(acted=True, candidate=candidate, reason=candidate.reason)


class OperatorAdapter:
    operator_name: str = ""
    operation_level: SkillOperationLevel = SkillOperationLevel.L1
    supported_skills: tuple[int, ...] = ()

    def build_executor(self, evaluator: BattlefieldEvaluator | None = None) -> SkillExecutor:
        if self.operation_level == SkillOperationLevel.L2:
            if evaluator is None:
                raise ValueError("L2 operator requires a BattlefieldEvaluator")
            return TargetedSkillExecutor(evaluator)
        return NormalSkillExecutor()


class WangAdapter(OperatorAdapter):
    operator_name = "望"
    operation_level = SkillOperationLevel.L2
    supported_skills = (3,)


class OperatorAdapterRegistry:
    def __init__(self) -> None:
        self._adapters: dict[str, OperatorAdapter] = {}

    def register(self, adapter: OperatorAdapter) -> None:
        if not adapter.operator_name:
            raise ValueError("adapter.operator_name is required")
        self._adapters[adapter.operator_name] = adapter

    def get(self, operator_name: str) -> OperatorAdapter | None:
        return self._adapters.get(operator_name)


class SpecialSkillAI:
    """Disabled-by-default orchestrator.

    When disabled, this object must not call adapter, evaluator, readiness, or executor code.
    That mirrors the required MaaCore compatibility behavior for future integration.
    """

    def __init__(self, config: SpecialSkillAIConfig | None = None, registry: OperatorAdapterRegistry | None = None) -> None:
        self.config = config or SpecialSkillAIConfig()
        self.registry = registry or OperatorAdapterRegistry()

    def run_once(
        self,
        operator_name: str,
        state: BattlefieldState,
        evaluator: BattlefieldEvaluator | None = None,
    ) -> ExecutionResult:
        if not self.config.enable_special_skill_ai:
            return ExecutionResult(acted=False, skipped=True, reason="special skill ai disabled")

        adapter = self.registry.get(operator_name)
        if adapter is None:
            return ExecutionResult(acted=False, skipped=True, reason="no adapter registered")

        executor = adapter.build_executor(evaluator)
        return executor.execute(operator_name, state)
