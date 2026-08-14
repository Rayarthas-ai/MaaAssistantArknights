"""Functional Recruitment Policy prototypes."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping

FUNCTIONAL_ROLES = (
    "main_carry", "ground", "block", "healing", "sustain", "economy", "ranged", "anti_air",
    "burst", "control", "fast_redeploy", "bait", "summon", "utility", "emergency",
)

DEFAULT_ROLE_TARGETS = {
    "main_carry": (1.0, 1.0), "ground": (1.0, 2.0), "block": (1.0, 2.0),
    "healing": (1.0, 2.0), "sustain": (1.0, 2.0), "ranged": (1.0, 2.0),
    "anti_air": (1.0, 2.0), "economy": (0.0, 1.0), "burst": (0.0, 1.0),
    "control": (0.0, 1.0), "fast_redeploy": (0.0, 1.0), "bait": (0.0, 1.0),
    "summon": (0.0, 1.0), "utility": (0.0, 1.0), "emergency": (0.0, 1.0),
}


@dataclass(frozen=True)
class OperatorState:
    name: str
    elite: int = 0
    rarity: int | None = None


@dataclass(frozen=True)
class TeamState:
    operators: tuple[OperatorState, ...]
    hope: int | None = None


@dataclass(frozen=True)
class FunctionalCoverage:
    coverage: dict[str, float]
    missing_roles: tuple[str, ...]
    weak_roles: tuple[str, ...]
    saturated_roles: tuple[str, ...]


class FunctionalRoleEvaluator:
    def __init__(self, profiles: Mapping[str, Mapping], role_targets: Mapping[str, tuple[float, float]] | None = None) -> None:
        self.profiles = profiles
        self.role_targets = dict(role_targets or DEFAULT_ROLE_TARGETS)

    def evaluate(self, team: TeamState) -> FunctionalCoverage:
        coverage = {role: 0.0 for role in FUNCTIONAL_ROLES}
        for operator in team.operators:
            for role, value in self.profiles.get(operator.name, {}).get("functions", {}).items():
                if role in coverage:
                    coverage[role] += float(value)
        missing, weak, saturated = [], [], []
        for role, (minimum, target) in self.role_targets.items():
            value = coverage.get(role, 0.0)
            if value < minimum:
                missing.append(role)
            elif value < target:
                weak.append(role)
            elif target > 0 and value > target:
                saturated.append(role)
        return FunctionalCoverage(coverage, tuple(missing), tuple(weak), tuple(saturated))


class WangState(str, Enum):
    NOT_OWNED = "NOT_OWNED"
    E1 = "E1"
    E2 = "E2"


@dataclass(frozen=True)
class WangPolicy:
    state: WangState

    def recruitment_bonus(self, candidate_name: str) -> float:
        return 1.0 if self.state == WangState.NOT_OWNED and candidate_name == "望" else 0.0

    def promotion_bonus(self, candidate_name: str, decision_type: str) -> float:
        return 1.0 if candidate_name == "望" and decision_type == "PROMOTE" and self.state in {WangState.NOT_OWNED, WangState.E1} else 0.0

    def core_reserve_level(self) -> str:
        if self.state == WangState.NOT_OWNED:
            return "high_recruit_reserve"
        if self.state == WangState.E1:
            return "high_promotion_reserve"
        return "reduced"


@dataclass(frozen=True)
class HopeBudget:
    core_reserve: float
    survival_budget: float
    optional_budget: float


class HopeBudgetPolicy:
    def __init__(self, total_hope: float, wang_policy: WangPolicy) -> None:
        self.total_hope = float(total_hope)
        self.wang_policy = wang_policy

    def allocate(self) -> HopeBudget:
        core_ratio = 0.55 if self.wang_policy.state == WangState.NOT_OWNED else 0.45 if self.wang_policy.state == WangState.E1 else 0.20
        core = self.total_hope * core_ratio
        survival = self.total_hope * 0.30
        return HopeBudget(core, survival, max(0.0, self.total_hope - core - survival))


@dataclass(frozen=True)
class Candidate:
    name: str
    decision_type: str = "RECRUIT"
    hope_cost: float | None = None
    base_value: float = 0.0
    promotion_value: float = 0.0


@dataclass(frozen=True)
class CandidateScoreBreakdown:
    total: float
    parts: dict[str, float]
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class CandidateScorerConfig:
    missing_function_weight: float = 1.0
    weak_function_weight: float = 0.4
    multi_role_weight: float = 0.25
    zero_hope_weight: float = 0.5
    low_hope_efficiency_weight: float = 0.3
    duplicate_penalty_weight: float = 0.5
    hope_cost_penalty_weight: float = 0.2
    hope_reserve_penalty_weight: float = 0.4


class CandidateScorer:
    def __init__(self, profiles: Mapping[str, Mapping], evaluator: FunctionalRoleEvaluator, config: CandidateScorerConfig | None = None) -> None:
        self.profiles = profiles
        self.evaluator = evaluator
        self.config = config or CandidateScorerConfig()

    def score(self, candidate: Candidate, team: TeamState, wang_policy: WangPolicy) -> CandidateScoreBreakdown:
        coverage = self.evaluator.evaluate(team)
        functions = self.profiles.get(candidate.name, {}).get("functions", {})
        parts = {"base_value": candidate.base_value, "promotion_value": candidate.promotion_value}
        reasons = []
        missing_hits = [role for role in functions if role in coverage.missing_roles]
        weak_hits = [role for role in functions if role in coverage.weak_roles]
        saturated_hits = [role for role in functions if role in coverage.saturated_roles]
        parts["wang_policy_bonus"] = wang_policy.recruitment_bonus(candidate.name) + wang_policy.promotion_bonus(candidate.name, candidate.decision_type)
        if parts["wang_policy_bonus"]:
            reasons.append("WangPolicy applies")
        parts["missing_function_bonus"] = sum(float(functions[r]) for r in missing_hits) * self.config.missing_function_weight
        parts["weak_function_bonus"] = sum(float(functions[r]) for r in weak_hits) * self.config.weak_function_weight
        if missing_hits:
            reasons.append("fills missing roles: " + ", ".join(missing_hits))
        distinct_helpful = len(set(missing_hits + weak_hits))
        parts["multi_role_bonus"] = max(0, distinct_helpful - 1) * self.config.multi_role_weight
        if distinct_helpful > 1:
            reasons.append("multi-role bonus")
        hope_cost = candidate.hope_cost
        parts["zero_hope_bonus"] = self.config.zero_hope_weight if hope_cost == 0 and (missing_hits or weak_hits) else 0.0
        parts["low_hope_efficiency_bonus"] = self.config.low_hope_efficiency_weight if hope_cost is not None and 0 < hope_cost <= 2 and (missing_hits or weak_hits) else 0.0
        parts["duplicate_function_penalty"] = -sum(float(functions[r]) for r in saturated_hits) * self.config.duplicate_penalty_weight
        if saturated_hits:
            reasons.append("duplicate saturated roles: " + ", ".join(saturated_hits))
        parts["hope_cost_penalty"] = 0.0 if hope_cost is None else -hope_cost * self.config.hope_cost_penalty_weight
        if hope_cost and wang_policy.core_reserve_level() != "reduced" and candidate.name != "望" and not missing_hits:
            parts["hope_reserve_penalty"] = -hope_cost * self.config.hope_reserve_penalty_weight
            reasons.append("hope reserve protected for Wang policy")
        else:
            parts["hope_reserve_penalty"] = 0.0
        return CandidateScoreBreakdown(sum(parts.values()), parts, tuple(reasons))
