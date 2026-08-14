# Phase 4 Status

Base MAA commit: `00da4c367d3167ef732167854314e361b5d5d37f`

## A. Current Low-Star Candidate Pool

Generated `roguelike-lab/analysis/LOW_HOPE_CANDIDATE_POOL.md`. The pool is grouped into confirmed seeds, MAA high-priority low-star candidates, multi-function candidates, community-validation candidates, temporarily not recommended entries, and reserve/temporary-related entries.

## B. Confirmed Functional Tags

Defined initial functional tags:

- `main_carry`
- `ground`
- `block`
- `healing`
- `sustain`
- `economy`
- `ranged`
- `anti_air`
- `burst`
- `control`
- `fast_redeploy`
- `bait`
- `summon`
- `utility`
- `emergency`

Seed profiles were created for `望`, `古米`, `伊桑`, `砾`, `豆苗`, `梅`, `清流`, and `罗小黑`.

## C. Needs External Community Validation

Low-confidence profiles, especially `伊桑`, `豆苗`, and `罗小黑`, need community guide or game-test evidence before affecting a real strategy version.

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

## J. External Knowledge Learning

Added a lab-only external knowledge learning pipeline:

- `roguelike-lab/data/external_sources.json`
- `roguelike-lab/data/source_weights.json`
- `roguelike-lab/data/operator_function_profiles_candidate.json`
- `roguelike-lab/knowledge/raw/`
- `roguelike-lab/docs/EXTERNAL_KNOWLEDGE_LEARNING.md`
- `roguelike-lab/analysis/KNOWLEDGE_UPDATE_PROPOSAL.md`
- `KnowledgeExtractor`
- `EvidenceAggregator`
- `VersionRelevanceEvaluator`
- `ExternalKnowledgeProvider`
- `FileManualImportProvider`
- `MockKnowledgeProvider`
- `profile_diff.py`

Current capability:

- register sources,
- keep raw knowledge intake separate,
- extract structured recommendation evidence,
- aggregate evidence with configurable source weights,
- discount stale/different-theme/different-difficulty evidence,
- generate candidate profile patches,
- diff formal vs candidate profiles.

Knowledge Candidate flow:

```text
external evidence
-> raw intake
-> extracted evidence
-> aggregate
-> operator_function_profiles_candidate.json
-> profile diff
-> KNOWLEDGE_UPDATE_PROPOSAL.md
-> experiment
-> explicit promote
```

Safety boundary:

- no external code execution,
- no automatic remote schema trust,
- no automatic overwrite of MAA resources,
- no automatic promotion into `operator_function_profiles.json`,
- no internet access from the game automation process.

Next automation suggestions:

1. Add a manual JSON import command that validates and writes raw evidence.
2. Add `RunAnalyzer` to turn our own results into `game_test` evidence.
3. Add GitHub/wiki/forum providers only as offline/manual-import adapters first.
4. Add stronger schema validation before accepting community JSON.

## Generated Files

- `roguelike-lab/data/operator_function_profiles.json`
- `roguelike-lab/analysis/LOW_HOPE_SEED_OPERATORS.md`
- `roguelike-lab/analysis/LOW_HOPE_CANDIDATE_POOL.md`
- `roguelike-lab/docs/FUNCTIONAL_RECRUITMENT_POLICY.md`
- `roguelike-lab/docs/HOPE_BUDGET_POLICY.md`
- `roguelike-lab/docs/EXTERNAL_KNOWLEDGE_LEARNING.md`
- `roguelike-lab/functional_recruitment/`
- `roguelike-lab/tests/test_phase4_functional_recruitment.py`

No official JieGarden recruitment JSON, V001 recruitment JSON, MaaCore behavior, emulator, or game runtime was modified or launched.
