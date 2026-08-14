from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = LAB_ROOT.parent
sys.path.insert(0, str(LAB_ROOT))

from functional_recruitment import Candidate, CandidateScorer, FunctionalRoleEvaluator, HopeBudgetPolicy, OperatorState, TeamState, WangPolicy, WangState


class Phase4FunctionalRecruitmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profiles = json.loads((REPO_ROOT / "roguelike-lab/data/operator_function_profiles.json").read_text(encoding="utf-8"))

    def test_profile_schema_seed_values(self) -> None:
        gummy = self.profiles["古米"]
        self.assertEqual(gummy["rarity"], 4)
        for value in gummy["functions"].values():
            self.assertGreaterEqual(value, 0.0)
            self.assertLessEqual(value, 1.0)
        self.assertTrue(gummy["multi_role"])
        self.assertIn("ground", gummy["functions"])
        self.assertIn("healing", gummy["functions"])
        self.assertTrue(gummy["evidence"])

    def test_functional_coverage_not_profession_template(self) -> None:
        coverage = FunctionalRoleEvaluator(self.profiles).evaluate(TeamState((OperatorState("望", elite=2, rarity=6),)))
        self.assertNotIn("main_carry", coverage.missing_roles)
        self.assertIn("healing", coverage.missing_roles)
        self.assertIn("block", coverage.missing_roles)

    def test_multi_role_zero_hope_requires_need(self) -> None:
        evaluator = FunctionalRoleEvaluator(self.profiles)
        scorer = CandidateScorer(self.profiles, evaluator)
        need_team = TeamState((OperatorState("望", elite=2, rarity=6),), hope=3)
        score = scorer.score(Candidate("古米", hope_cost=0), need_team, WangPolicy(WangState.E2))
        self.assertGreater(score.parts["missing_function_bonus"], 0)
        self.assertGreater(score.parts["multi_role_bonus"], 0)
        self.assertGreater(score.parts["zero_hope_bonus"], 0)
        covered_team = TeamState(
            (
                OperatorState("望"),
                OperatorState("古米"),
                OperatorState("古米"),
                OperatorState("古米"),
                OperatorState("古米"),
                OperatorState("清流"),
            ),
            hope=3,
        )
        covered_score = scorer.score(Candidate("古米", hope_cost=0), covered_team, WangPolicy(WangState.E2))
        self.assertEqual(covered_score.parts["zero_hope_bonus"], 0.0)

    def test_duplicate_function_penalty_uses_functional_roles(self) -> None:
        evaluator = FunctionalRoleEvaluator(self.profiles)
        scorer = CandidateScorer(self.profiles, evaluator)
        team = TeamState((OperatorState("望"), OperatorState("古米"), OperatorState("清流"), OperatorState("罗小黑")), hope=3)
        score = scorer.score(Candidate("古米", hope_cost=0), team, WangPolicy(WangState.E2))
        self.assertLessEqual(score.parts["duplicate_function_penalty"], 0)

    def test_wang_policy_and_hope_budget(self) -> None:
        not_owned = WangPolicy(WangState.NOT_OWNED)
        self.assertGreater(not_owned.recruitment_bonus("望"), 0)
        self.assertEqual(not_owned.recruitment_bonus("古米"), 0)
        budget = HopeBudgetPolicy(10, not_owned).allocate()
        self.assertGreater(budget.core_reserve, budget.optional_budget)
        e2_budget = HopeBudgetPolicy(10, WangPolicy(WangState.E2)).allocate()
        self.assertLess(e2_budget.core_reserve, budget.core_reserve)

    def test_candidate_scorer_is_explainable(self) -> None:
        evaluator = FunctionalRoleEvaluator(self.profiles)
        score = CandidateScorer(self.profiles, evaluator).score(Candidate("望", hope_cost=6), TeamState(tuple(), hope=6), WangPolicy(WangState.NOT_OWNED))
        self.assertGreater(score.parts["wang_policy_bonus"], 0)
        self.assertTrue(score.reasons)


if __name__ == "__main__":
    unittest.main()
