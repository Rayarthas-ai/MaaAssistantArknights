#!/usr/bin/env python3
"""Generate Phase 4 functional recruitment lab artifacts."""

from __future__ import annotations

import json
from pathlib import Path

BASE_COMMIT = "00da4c367d3167ef732167854314e361b5d5d37f"
ROOT = Path(__file__).resolve().parents[2]
REC = json.loads((ROOT / "resource/roguelike/JieGarden/recruitment.json").read_text(encoding="utf-8"))
BATTLE = json.loads((ROOT / "resource/battle_data.json").read_text(encoding="utf-8"))["chars"]
BY_NAME = {v["name"]: v for v in BATTLE.values()}

WANG = "\u671b"
SEEDS = ["\u53e4\u7c73", "\u4f0a\u6851", "\u783e", "\u8c46\u82d7", "\u6885", "\u6e05\u6d41", "\u7f57\u5c0f\u9ed1"]
FUNCTIONS = [
    "main_carry", "ground", "block", "healing", "sustain", "economy", "ranged", "anti_air",
    "burst", "control", "fast_redeploy", "bait", "summon", "utility", "emergency",
]


def battle_fact(name: str) -> dict:
    b = BY_NAME.get(name, {})
    return {k: b.get(k) for k in ["rarity", "position", "profession", "subProfessionId"]}


def effective(oper: dict) -> dict:
    recruit = oper.get("recruit_priority", 0)
    promote = oper.get("promote_priority", 0)
    row = dict(oper)
    row["recruit_priority"] = recruit
    row["promote_priority"] = promote
    row["recruit_priority_when_team_full"] = oper.get("recruit_priority_when_team_full", recruit - 100)
    row["promote_priority_when_team_full"] = oper.get("promote_priority_when_team_full", promote + 300)
    row["is_start"] = bool(oper.get("is_start", False))
    row["is_key"] = bool(oper.get("is_key", False))
    return row


def defs_for(name: str) -> list[dict]:
    rows = []
    for gi, group in enumerate(REC.get("priority", [])):
        for oi, oper in enumerate(group.get("opers", [])):
            if oper.get("name") == name:
                row = effective(oper)
                row["group"] = group.get("name", "")
                row["group_index"] = gi
                row["operator_index"] = oi
                rows.append(row)
    return rows


def ev(*items: tuple[str, str]) -> list[dict]:
    return [{"type": t, "detail": d} for t, d in items]


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def build_profiles() -> dict:
    profiles = {
        WANG: {
            "rarity": battle_fact(WANG)["rarity"],
            "functions": {"main_carry": 1.0, "ranged": 0.8, "burst": 0.6, "utility": 0.4},
            "multi_role": True,
            "strategy_tier": "T0",
            "notes": ["Manual Wang-First constraint.", "Seed weights, not final measured strength."],
            "evidence": ev(("manual strategy", "Wang-First experiment constraint"), ("MAA official", "JieGarden configures Wang skill=3")),
            "confidence": "medium",
        },
        "\u53e4\u7c73": {
            "rarity": 4,
            "functions": {"ground": 0.6, "block": 0.8, "healing": 0.6, "sustain": 0.7},
            "multi_role": True,
            "strategy_tier": "T1",
            "notes": ["Conservative multi-role seed; not final balance."],
            "evidence": ev(("MAA official", "Groups: \u91cd\u88c5, \u5730\u9762\u963b\u6321, \u5976\u76fe"), ("manual strategy", "Ground + Block + Healing + Sustain")),
            "confidence": "medium",
        },
        "\u4f0a\u6851": {
            "rarity": 4,
            "functions": {"ground": 0.4, "control": 0.7, "utility": 0.4, "emergency": 0.3},
            "multi_role": True,
            "strategy_tier": "T1",
            "notes": ["Control/utility values need external validation."],
            "evidence": ev(("MAA official", "Group: \u5730\u523a; SPECIAL/stalker"), ("manual strategy", "Phase 4 seed")),
            "confidence": "low",
        },
        "\u783e": {
            "rarity": 4,
            "functions": {"ground": 0.4, "fast_redeploy": 0.9, "bait": 0.9, "emergency": 0.7},
            "multi_role": True,
            "strategy_tier": "T1",
            "notes": ["Supported by MAA bait-style group and auto_retreat; still test-adjustable."],
            "evidence": ev(("MAA official", "Group: \u70ae\u7070; auto_retreat=15"), ("manual strategy", "Phase 4 seed")),
            "confidence": "medium",
        },
        "\u8c46\u82d7": {
            "rarity": 4,
            "functions": {"economy": 0.7, "ranged": 0.4, "summon": 0.4, "utility": 0.4},
            "multi_role": True,
            "strategy_tier": "T1",
            "notes": ["Economy is MAA-offset backed; summon/utility need validation."],
            "evidence": ev(("MAA official", "Offset references \u56de\u8d39"), ("MAA official", "PIONEER/tactician"), ("manual strategy", "Phase 4 seed")),
            "confidence": "low",
        },
        "\u6885": {
            "rarity": 4,
            "functions": {"ranged": 0.7, "anti_air": 0.7, "control": 0.3},
            "multi_role": True,
            "strategy_tier": "T1",
            "notes": ["Control is low-confidence seed tag."],
            "evidence": ev(("MAA official", "Groups: \u901f\u72d9, \u9ad8\u53f0\u8f93\u51fa"), ("manual strategy", "Phase 4 seed")),
            "confidence": "medium",
        },
        "\u6e05\u6d41": {
            "rarity": 4,
            "functions": {"healing": 0.8, "sustain": 0.6, "ranged": 0.2},
            "multi_role": True,
            "strategy_tier": "T1",
            "notes": ["Sustain value is conservative and test-adjustable."],
            "evidence": ev(("MAA official", "Groups: \u5355\u5976, \u5976"), ("manual strategy", "Phase 4 seed")),
            "confidence": "medium",
        },
        "\u7f57\u5c0f\u9ed1": {
            "rarity": 4,
            "functions": {"ground": 0.7, "block": 0.4, "utility": 0.3},
            "multi_role": True,
            "strategy_tier": "T1",
            "notes": ["Ground/block follows MAA group; utility remains manual hypothesis."],
            "evidence": ev(("MAA official", "Group: \u5730\u9762\u963b\u6321"), ("manual strategy", "Phase 4 seed")),
            "confidence": "low",
        },
    }
    write("roguelike-lab/data/operator_function_profiles.json", json.dumps(profiles, ensure_ascii=False, indent=2) + "\n")
    return profiles


def seed_report(profiles: dict) -> None:
    lines = [
        "# Low-Hope Seed Operators", "", f"Base MAA commit: `{BASE_COMMIT}`", "",
        "Facts are read from official MAA resources. Functional tags are seed hypotheses unless explicitly tied to MAA groups/resources.",
        "", "## Functional Role Tags", "", ", ".join(f"`{f}`" for f in FUNCTIONS), "",
    ]
    for name in SEEDS:
        rows = defs_for(name)
        fact = battle_fact(name)
        profile = profiles[name]
        lines += [
            f"## {name}", "", "### MAA Facts", "",
            f"- Rarity: `{fact.get('rarity')}`; position: `{fact.get('position')}`; profession: `{fact.get('profession')}`; subProfessionId: `{fact.get('subProfessionId')}`",
            "",
            "| Group | Recruit | Promote | Full Recruit | Full Promote | Skill | Start | Key | Auto Retreat | Offsets |",
            "| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | --- |",
        ]
        for r in rows:
            lines.append(
                f"| `{r.get('group','')}` | {r.get('recruit_priority',0)} | {r.get('promote_priority',0)} | "
                f"{r.get('recruit_priority_when_team_full',0)} | {r.get('promote_priority_when_team_full',0)} | "
                f"{r.get('skill','')} | {r.get('is_start',False)} | {r.get('is_key',False)} | {r.get('auto_retreat',0)} | "
                f"`{json.dumps(r.get('recruit_priority_offsets', []), ensure_ascii=False)}` |"
            )
        lines += ["", "### Functional Mapping", "", "| Functional Role | Weight | Evidence status |", "| --- | ---: | --- |"]
        for fn, val in profile["functions"].items():
            lines.append(f"| `{fn}` | {val:.1f} | seed hypothesis with recorded evidence |")
        evidence_text = "; ".join(f"{e['type']}: {e['detail']}" for e in profile["evidence"])
        lines += [
            "", "### Interpretation", "",
            f"- Current MAA classification: `{', '.join(r.get('group', '') for r in rows)}`.",
            f"- Functional profile confidence: `{profile['confidence']}`.",
            f"- Evidence: {evidence_text}.",
            "- Needs community guide or game-test validation before being treated as stable.",
            "",
        ]
    write("roguelike-lab/analysis/LOW_HOPE_SEED_OPERATORS.md", "\n".join(lines))


def all_records() -> list[dict]:
    rows = []
    for group in REC["priority"]:
        for oper in group.get("opers", []):
            name = oper.get("name", "")
            if not name:
                continue
            row = effective(oper)
            row.update({"name": name, "group": group.get("name", ""), **battle_fact(name)})
            rows.append(row)
    return rows


def candidate_pool_report() -> None:
    records = all_records()
    by_op: dict[str, dict] = {}
    for r in records:
        cur = by_op.get(r["name"])
        if cur is None or (r.get("recruit_priority", 0), r.get("promote_priority", 0)) > (cur.get("recruit_priority", 0), cur.get("promote_priority", 0)):
            by_op[r["name"]] = dict(r)
    for name, row in by_op.items():
        row["groups"] = sorted({r["group"] for r in records if r["name"] == name})
    low = [r for r in by_op.values() if isinstance(r.get("rarity"), int) and r["rarity"] <= 4]
    low = sorted(low, key=lambda r: (r.get("recruit_priority", 0), r.get("promote_priority", 0), -r.get("rarity", 99)), reverse=True)
    seed_set = set(SEEDS)
    confirmed = [r for r in low if r["name"] in seed_set]
    official_high = [r for r in low if r["name"] not in seed_set and r.get("recruit_priority", 0) >= 500][:10]
    multi = []
    for r in low:
        groups = " ".join(r.get("groups", []))
        if r["name"] not in seed_set and any(k in groups for k in ["奶", "阻挡", "回费", "炮灰", "地刺", "速狙", "高台输出", "召唤"]):
            multi.append(r)
    multi = multi[:10]
    verification = [r for r in low if r["name"] not in seed_set and r not in official_high and r not in multi and r.get("recruit_priority", 0) > 0][:8]
    not_recommended = [r for r in low if r.get("recruit_priority", 0) <= 0][:8]
    reserve = [r for r in by_op.values() if "预备干员" in r["name"] or "Reserve" in r["name"]]

    def table(rows: list[dict]) -> list[str]:
        out = ["| Operator | Rarity | Groups | Recruit | Promote | Skill | Start | Key | Reason |", "| --- | ---: | --- | ---: | ---: | ---: | --- | --- | --- |"]
        for r in rows:
            reason = []
            if r["name"] in seed_set:
                reason.append("Phase 4 seed")
            if r.get("recruit_priority", 0) >= 500:
                reason.append("MAA high priority")
            if len(r.get("groups", [])) > 1:
                reason.append("multiple MAA groups")
            if r.get("recruit_priority_offsets"):
                reason.append("has offsets")
            if not reason:
                reason.append("needs validation")
            out.append(f"| `{r['name']}` | {r.get('rarity','')} | `{', '.join(r.get('groups',[]))}` | {r.get('recruit_priority',0)} | {r.get('promote_priority',0)} | {r.get('skill','')} | {r.get('is_start',False)} | {r.get('is_key',False)} | {', '.join(reason)} |")
        return out

    lines = ["# Low-Hope Candidate Pool", "", f"Base MAA commit: `{BASE_COMMIT}`", "", "This is a research pool, not a final “best low-star” list. Exact Hope cost is not present in recruitment JSON, so rarity is only a first-pass research signal.", "", "## A. Confirmed High-Value Seeds", ""]
    lines += table(confirmed) + ["", "## B. MAA Official High-Priority Low-Star Candidates", ""] + table(official_high)
    lines += ["", "## C. Multi-Function Candidates", ""] + table(multi)
    lines += ["", "## D. Needs Community Guide Or Game-Test Validation", ""] + table(verification)
    lines += ["", "## E. Temporarily Not Recommended", "", "Low-star entries with no positive priority signal in the JieGarden baseline. Not permanently rejected; they need stronger evidence.", ""] + table(not_recommended)
    lines += ["", "## Reserve / Temporary Recruitment Related", ""] + table(reserve[:12])
    write("roguelike-lab/analysis/LOW_HOPE_CANDIDATE_POOL.md", "\n".join(lines))


def prototype_files() -> None:
    pkg = ROOT / "roguelike-lab/functional_recruitment"
    pkg.mkdir(parents=True, exist_ok=True)
    (pkg / "__init__.py").write_text('''"""Functional recruitment policy lab prototypes."""\n\nfrom .core import Candidate, CandidateScoreBreakdown, CandidateScorer, FunctionalCoverage, FunctionalRoleEvaluator, HopeBudget, HopeBudgetPolicy, OperatorState, TeamState, WangPolicy, WangState\n\n__all__ = ["Candidate", "CandidateScoreBreakdown", "CandidateScorer", "FunctionalCoverage", "FunctionalRoleEvaluator", "HopeBudget", "HopeBudgetPolicy", "OperatorState", "TeamState", "WangPolicy", "WangState"]\n''', encoding="utf-8")
    (pkg / "core.py").write_text(r'''"""Functional Recruitment Policy prototypes."""

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
''', encoding="utf-8")


def docs() -> None:
    roles = "\n".join(f"- `{role}`" for role in FUNCTIONS)
    write("roguelike-lab/docs/FUNCTIONAL_RECRUITMENT_POLICY.md", f"""# Functional Recruitment Policy

Base MAA commit: `{BASE_COMMIT}`

## Goal

Move recruitment research from fixed profession/star thinking toward an explainable functional model around the first Carry `{WANG}`. This document is a lab policy design only; it does not change MaaCore or official resources.

## Functional Roles

{roles}

An operator may carry multiple functional tags. Profession is input evidence, not the final team-completeness model. For example, `{SEEDS[0]}` is represented as ground, block, healing, and sustain because current MAA groups include `重装`, `地面阻挡`, and `奶盾`.

## Current MAA Support

Current JSON can directly support coarse score changes through priority fields and group-based offsets. It cannot fully compute current Hope budget, exact missing functional roles, multi-role value, or duplicate functional saturation.

## Lab-Only Model

`FunctionalRoleEvaluator` takes a `TeamState` plus `operator_function_profiles.json` and outputs coverage, missing roles, weak roles, and saturated roles. Thresholds are configurable and intentionally not tied to fixed profession templates.

`CandidateScorer` explains scores with Wang policy, missing function bonus, multi-role bonus, zero/low Hope efficiency, promotion value, duplicate penalties, and Hope reserve pressure. The prototype does not claim final numeric balance.

## Decision Types

- `RECRUIT`: currently supported by recruitment scoring.
- `PROMOTE`: currently approximated by promote priority.
- `SKIP`: needs Core decision support.
- `RESERVE`: needs Core/Hope-aware state support.
""")
    write("roguelike-lab/docs/HOPE_BUDGET_POLICY.md", f"""# Hope Budget Policy

Base MAA commit: `{BASE_COMMIT}`

## Budget Model

```text
Hope Budget
|-- Core Reserve
|-- Survival Budget
`-- Optional Budget
```

## Core Reserve

- `{WANG}` not owned: reserve Hope for core recruitment.
- `{WANG}` E1: reserve Hope for key promotion.
- `{WANG}` E2: core reserve can decrease.

## Survival Budget

May be spent on healing, ground stability, leak prevention, and necessary economy.

## Optional Budget

Used for second Carry, high-value utility, or tactical enhancement after core and survival needs are protected.

## Zero Hope Logic

Zero Hope must be linked to `MissingFunctionNeed`. Forbidden rule:

```text
HopeCost == 0 -> unconditional recruit
```

The prototype grants ZeroHopeBonus only when the candidate covers missing or weak functional roles.
""")


def tests() -> None:
    write("roguelike-lab/tests/test_phase4_functional_recruitment.py", r'''from __future__ import annotations

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
        covered_team = TeamState((OperatorState("望"), OperatorState("古米"), OperatorState("古米"), OperatorState("古米"), OperatorState("古米"), OperatorState("清流")), hope=3)
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
''')


def status() -> None:
    roles = "\n".join(f"- `{role}`" for role in FUNCTIONS)
    write("roguelike-lab/PHASE4_STATUS.md", f"""# Phase 4 Status

Base MAA commit: `{BASE_COMMIT}`

## A. Current Low-Star Candidate Pool

Generated `roguelike-lab/analysis/LOW_HOPE_CANDIDATE_POOL.md`. The pool is grouped into confirmed seeds, MAA high-priority low-star candidates, multi-function candidates, community-validation candidates, temporarily not recommended entries, and reserve/temporary-related entries.

## B. Confirmed Functional Tags

Defined initial functional tags:

{roles}

Seed profiles were created for `{WANG}`, `{SEEDS[0]}`, `{SEEDS[1]}`, `{SEEDS[2]}`, `{SEEDS[3]}`, `{SEEDS[4]}`, `{SEEDS[5]}`, and `{SEEDS[6]}`.

## C. Needs External Community Validation

Low-confidence profiles, especially `{SEEDS[1]}`, `{SEEDS[3]}`, and `{SEEDS[6]}`, need community guide or game-test evidence before affecting a real strategy version.

## D. Directly Supported By Current MAA

JSON priority changes, group-based offsets, collection offsets, skill metadata, and separate recruit/promote scoring.

## E. Needs Core Changes

Exact Hope-aware decisions, functional coverage during recruitment, `SKIP` / `RESERVE`, zero-Hope logic tied to missing functions, duplicate functional saturation penalties, and WangPolicy as live recruitment control.

## F. WangPolicy And Low-Hope Interaction

Wang remains the first Carry. Low-Hope functional operators remain valid when they cover survival gaps, especially while Wang is E1 and waiting for a promotion opportunity.

## G. HopeReserve Model

Generated `roguelike-lab/docs/HOPE_BUDGET_POLICY.md`. Core reserve is highest before Wang is recruited, remains high for E1 promotion, and decreases after E2.

## H. Community Data Needed Next

Low-Hope JieGarden recommendations with reasons, observed Hope costs, Wang offered/recruited/promoted/skipped logs, and zero-Hope duplicate-role examples.

## I. First Game-Test Parameters

Record Wang state, offered candidates, selected candidate, current missing/weak/saturated roles, current Hope, estimated reserve pressure, whether low-Hope pick covered a missing function, final floor, ending, failure reason, recognition errors, and notes.

## Generated Files

- `roguelike-lab/data/operator_function_profiles.json`
- `roguelike-lab/analysis/LOW_HOPE_SEED_OPERATORS.md`
- `roguelike-lab/analysis/LOW_HOPE_CANDIDATE_POOL.md`
- `roguelike-lab/docs/FUNCTIONAL_RECRUITMENT_POLICY.md`
- `roguelike-lab/docs/HOPE_BUDGET_POLICY.md`
- `roguelike-lab/functional_recruitment/`
- `roguelike-lab/tests/test_phase4_functional_recruitment.py`

No official JieGarden recruitment JSON, V001 recruitment JSON, MaaCore behavior, emulator, or game runtime was modified or launched.
""")


def main() -> int:
    profiles = build_profiles()
    seed_report(profiles)
    candidate_pool_report()
    prototype_files()
    docs()
    tests()
    status()
    print("generated Phase 4 artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
