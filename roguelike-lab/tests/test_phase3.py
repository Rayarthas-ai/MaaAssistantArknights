from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = LAB_ROOT.parent
sys.path.insert(0, str(LAB_ROOT))

from special_skill_ai import (  # noqa: E402
    BattlefieldState,
    OperatorAdapterRegistry,
    SkillOperationLevel,
    SpecialSkillAI,
    SpecialSkillAIConfig,
    TargetCandidate,
    TargetSelector,
    WangAdapter,
)


class DummyEvaluator:
    def __init__(self) -> None:
        self.called = False

    def evaluate(self, operator_name: str, state: BattlefieldState) -> list[TargetCandidate]:
        self.called = True
        return [
            TargetCandidate(location=(1, 1), valid=False, tactical_score=100, reason="blocked"),
            TargetCandidate(location=(2, 2), valid=True, threat_score=2, tactical_score=5, reason="best legal"),
            TargetCandidate(location=(3, 3), valid=True, threat_score=9, tactical_score=5, reason="tie by threat"),
        ]


class Phase3Tests(unittest.TestCase):
    def test_v001_recruitment_schema_and_wang_fields(self) -> None:
        data = json.loads((REPO_ROOT / "roguelike-lab/experiments/V001/recruitment.json").read_text(encoding="utf-8"))
        self.assertEqual(data["theme"], "JieGarden")
        self.assertIsInstance(data.get("priority"), list)
        wang_defs = [
            (group.get("name"), oper)
            for group in data["priority"]
            for oper in group.get("opers", [])
            if oper.get("name") == "望"
        ]
        full_defs = [(group, oper) for group, oper in wang_defs if "recruit_priority" in oper]
        self.assertEqual(len(full_defs), 1)
        group, wang = full_defs[0]
        self.assertEqual(group, "其他高台")
        self.assertEqual(wang["recruit_priority"], 3000)
        self.assertEqual(wang["promote_priority"], 3000)
        self.assertEqual(wang["recruit_priority_when_team_full"], 3000)
        self.assertEqual(wang["promote_priority_when_team_full"], 3000)
        self.assertNotIn("is_start", wang)
        self.assertNotIn("is_key", wang)
        self.assertEqual(wang["skill"], 3)

    def test_v000_v001_diff_captures_wang_changes(self) -> None:
        diff = json.loads((REPO_ROOT / "roguelike-lab/experiments/V001/V000_V001_RECRUITMENT_DIFF.json").read_text(encoding="utf-8"))
        priority_fields = {item["field"] for item in diff["priority_changes"] if item.get("operator") == "望"}
        flag_fields = {item["field"] for item in diff["flag_changes"] if item.get("operator") == "望"}
        self.assertEqual(
            priority_fields,
            {
                "recruit_priority",
                "promote_priority",
                "recruit_priority_when_team_full",
                "promote_priority_when_team_full",
            },
        )
        self.assertEqual(flag_fields, set())

    def test_special_skill_ai_disabled_compatibility(self) -> None:
        registry = OperatorAdapterRegistry()
        registry.register(WangAdapter())
        evaluator = DummyEvaluator()
        result = SpecialSkillAI(SpecialSkillAIConfig(enable_special_skill_ai=False), registry).run_once(
            "望", BattlefieldState(), evaluator
        )
        self.assertFalse(result.acted)
        self.assertTrue(result.skipped)
        self.assertFalse(evaluator.called)

    def test_target_selector_mock_candidates(self) -> None:
        chosen = TargetSelector().select(
            [
                TargetCandidate(location=(0, 0), valid=False, tactical_score=999),
                TargetCandidate(location=(1, 0), valid=True, tactical_score=10, threat_score=1),
                TargetCandidate(location=(2, 0), valid=True, tactical_score=10, threat_score=5),
            ]
        )
        self.assertIsNotNone(chosen)
        self.assertEqual(chosen.location, (2, 0))

    def test_operator_adapter_registration_and_wang_interface(self) -> None:
        registry = OperatorAdapterRegistry()
        wang = WangAdapter()
        registry.register(wang)
        self.assertIs(registry.get("望"), wang)
        self.assertEqual(wang.operation_level, SkillOperationLevel.L2)
        self.assertEqual(wang.supported_skills, (3,))

    def test_wang_adapter_targeted_execution_contract(self) -> None:
        registry = OperatorAdapterRegistry()
        registry.register(WangAdapter())
        evaluator = DummyEvaluator()
        result = SpecialSkillAI(SpecialSkillAIConfig(enable_special_skill_ai=True), registry).run_once(
            "望", BattlefieldState(stage_name="mock"), evaluator
        )
        self.assertTrue(evaluator.called)
        self.assertTrue(result.acted)
        self.assertIsNotNone(result.candidate)
        self.assertEqual(result.candidate.location, (3, 3))


if __name__ == "__main__":
    unittest.main()
