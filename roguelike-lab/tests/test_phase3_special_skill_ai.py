from pathlib import Path
import importlib.util
import json
import sys

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

from special_skill_ai import (
    BattlefieldState,
    OperatorAdapterRegistry,
    SpecialSkillAI,
    SpecialSkillAIConfig,
    TargetCandidate,
    TargetSelector,
    TargetedSkillExecutor,
    WangAdapter,
)


class MockEvaluator:
    def evaluate(self, operator_name, state):
        return [
            TargetCandidate(location=(1, 1), valid=False, tactical_score=999, reason="invalid"),
            TargetCandidate(location=(2, 2), valid=True, tactical_score=10, reason="low"),
            TargetCandidate(location=(3, 3), valid=True, tactical_score=30, reason="best"),
        ]


def test_v001_recruitment_schema_and_wang_fields():
    data = json.loads((LAB_ROOT / "experiments" / "V001" / "recruitment.json").read_text(encoding="utf-8"))
    assert data["theme"] == "JieGarden"
    definitions = [
        (group["name"], oper)
        for group in data["priority"]
        for oper in group.get("opers", [])
        if oper.get("name") == "\u671b"
    ]
    full = [oper for group, oper in definitions if group == "\u5176\u4ed6\u9ad8\u53f0" and "recruit_priority" in oper]
    assert len(full) == 1
    wang = full[0]
    assert wang["recruit_priority"] == 3000
    assert wang["promote_priority"] == 3000
    assert wang["recruit_priority_when_team_full"] == 3000
    assert wang["promote_priority_when_team_full"] == 3000
    assert wang["is_start"] is True
    assert wang["is_key"] is True
    assert wang["skill"] == 3


def test_v000_v001_diff_reports_wang_changes():
    diff = json.loads((LAB_ROOT / "experiments" / "V001" / "V000_V001_RECRUITMENT_DIFF.json").read_text(encoding="utf-8"))
    changed = {(row["operator"], row["group"], row["field"]) for row in diff["priority_changes"] + diff["flag_changes"]}
    assert ("\u671b", "\u5176\u4ed6\u9ad8\u53f0", "recruit_priority") in changed
    assert ("\u671b", "\u5176\u4ed6\u9ad8\u53f0", "promote_priority") in changed
    assert ("\u671b", "\u5176\u4ed6\u9ad8\u53f0", "is_start") in changed
    assert ("\u671b", "\u5176\u4ed6\u9ad8\u53f0", "is_key") in changed


def test_special_skill_ai_disabled_compatibility():
    ai = SpecialSkillAI(config=SpecialSkillAIConfig(enable_special_skill_ai=False))
    ai.registry.register(WangAdapter(TargetedSkillExecutor(MockEvaluator())))
    assert ai.execute_if_enabled("\u671b", BattlefieldState()) is None


def test_target_selector_picks_highest_valid_candidate():
    selected = TargetSelector().select(MockEvaluator().evaluate("\u671b", BattlefieldState()))
    assert selected is not None
    assert selected.location == (3, 3)
    assert selected.reason == "best"


def test_operator_adapter_registration_and_wang_interface():
    registry = OperatorAdapterRegistry()
    adapter = WangAdapter(TargetedSkillExecutor(MockEvaluator()))
    registry.register(adapter)
    assert registry.get("\u671b") is adapter
    result = adapter.execute(BattlefieldState(stage_name="mock"))
    assert result.executed is True
    assert result.target is not None
    assert result.target.location == (3, 3)
