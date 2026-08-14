# Phase 3 Status

Base MAA commit: `00da4c367d3167ef732167854314e361b5d5d37f`

## A. V001 Wang-First

Created `roguelike-lab/experiments/V001/recruitment.json` from the JieGarden V000 baseline without touching official resources.

V001 now follows the minimal-change rule: it modifies only priority-series fields on the strategy-bearing `望` entry in group `其他高台`:

- `recruit_priority`: 600 -> 3000
- `promote_priority`: 600 -> 3000
- `recruit_priority_when_team_full`: implicit 500 -> 3000
- `promote_priority_when_team_full`: implicit 900 -> 3000

V001 does not change `is_start` or `is_key`. The experiment first tests whether priority alone can make `望` the first recruitment/promotion core. If logs prove start/key gating blocks Wang-First, flag changes should be proposed separately with evidence.

## B. V000/V001 Diff

Generated:

- `roguelike-lab/experiments/V001/V000_V001_RECRUITMENT_DIFF.md`
- `roguelike-lab/experiments/V001/V000_V001_RECRUITMENT_DIFF.json`

No operators, groups, offsets, start/key flags, skill metadata, or `team_complete_condition` changed. Only Wang priority fields changed.

## C. Wang Official Skill Config

V000 has two `望` entries:

- `高台输出`: membership-only entry.
- `其他高台`: full strategy entry with `skill=3`, `recruit_priority=600`, `promote_priority=600`.

No `alternate_skill` is configured. Current skill selection code clicks `alternate_skill` if present, then `skill` if present; it does not infer elite-aware S2/S3 switching from promotion status. Based on current code/resource evidence, Wang is configured for skill 3 only.

## D. SpecialSkillAI Architecture

Added a lab-only Python prototype in `roguelike-lab/special_skill_ai/`:

- `SkillExecutor`
- `NormalSkillExecutor`
- `TargetedSkillExecutor`
- `BattlefieldEvaluator`
- `TargetSelector`
- `SummonManager`
- `SkillReadinessDetector`
- `OperatorAdapterRegistry`
- `WangAdapter`

Default config is `enable_special_skill_ai=false`.

## E. Reusable MAA Components

Reusable current components:

- `BattleHelper::click_oper_on_battlefield`
- `BattleHelper::is_skill_ready`
- `BattleHelper::click_skill`
- `BattleHelper::use_skill`
- TilePack/Copilot logical grid to screen coordinate conversion
- Roguelike `deploy_plan` and `retreat_plan` location parsing
- `BattlefieldMatcher` for deployments, kills, costs, battle status
- `BattlefieldClassifier` for skill-ready classification
- existing drone/summon-like `Role::Drone` bookkeeping

## F. Must Add Later

Core integration would need:

- target-selection-state detector
- legal target tile/object analyzer
- targeted skill timeout/cancel handling
- skill-specific adapter dispatch in battle loop
- safe debug capture/reporting for target selection mistakes

## G. Not Implemented In Phase 3

- No MaaCore C++ behavior changed.
- No BattleTask or RoguelikeBattleTaskPlugin integration.
- No real Wang target scoring AI.
- No encounter/shopping/route/autopilot changes.
- No `is_start` / `is_key` expansion in V001.
- No emulator or game run.

## H. Next Stage

Recommended Phase 4:

1. Run V001 on the separate game-test machine and record result schema fields plus ?Wang offered/recruited/promoted/skipped? timestamps.
2. Specifically record whether `望` was skipped while `starts_complete` or `team_complete` was false; that is the evidence needed before any flag change.
3. Collect community JieGarden recruitment JSONs that explicitly use Wang or targeted-skill carries.
4. Add a C++ design doc/ADR for disabled-by-default SpecialSkillAI integration points before touching Core.
5. Gather screenshots/video for Wang skill target-selection UI to define the missing Vision Analyzer.
