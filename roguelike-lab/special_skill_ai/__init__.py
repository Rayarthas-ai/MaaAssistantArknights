"""Prototype interfaces for the Roguelike SpecialSkillAI lab.

This package is intentionally outside MaaCore. It documents and tests the
interfaces before any production integration is attempted.
"""

from .core import (
    BattlefieldEvaluator,
    BattlefieldState,
    ExecutionResult,
    NormalSkillExecutor,
    OperatorAdapter,
    OperatorAdapterRegistry,
    SkillExecutor,
    SkillOperationLevel,
    SkillReadinessDetector,
    SpecialSkillAI,
    SpecialSkillAIConfig,
    SummonManager,
    TargetCandidate,
    TargetSelector,
    TargetedSkillExecutor,
    WangAdapter,
)

__all__ = [
    "BattlefieldEvaluator",
    "BattlefieldState",
    "ExecutionResult",
    "NormalSkillExecutor",
    "OperatorAdapter",
    "OperatorAdapterRegistry",
    "SkillExecutor",
    "SkillOperationLevel",
    "SkillReadinessDetector",
    "SpecialSkillAI",
    "SpecialSkillAIConfig",
    "SummonManager",
    "TargetCandidate",
    "TargetSelector",
    "TargetedSkillExecutor",
    "WangAdapter",
]
