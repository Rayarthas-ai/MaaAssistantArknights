# Wang Special Skill Driver Research

This document designs the Phase 3 research interface for a future `SpecialSkillAI`. It is not a MaaCore implementation and it does not change current battle behavior.

## Research Baseline

Relevant current files:

- `src/MaaCore/Task/BattleHelper.cpp`
- `src/MaaCore/Task/BattleHelper.h`
- `src/MaaCore/Task/Roguelike/RoguelikeBattleTaskPlugin.cpp`
- `src/MaaCore/Task/Roguelike/RoguelikeSkillSelectionTaskPlugin.cpp`
- `src/MaaCore/Task/Miscellaneous/BattleProcessTask.cpp`
- `src/MaaCore/Config/Roguelike/RoguelikeCopilotConfig.cpp`
- `src/MaaCore/Config/Roguelike/RoguelikeRecruitConfig.cpp`
- `src/MaaCore/Vision/Battle/BattlefieldMatcher.h`
- `src/MaaCore/Vision/Battle/BattlefieldClassifier.h`

## Answers

### 1. Current MAA How Clicks Deployed Operators

`BattleHelper::click_oper_on_battlefield(name)` resolves the operator name through `m_battlefield_opers`, then calls `click_oper_on_battlefield(loc)`. The location is a logical map `Point`; it is converted through `m_normal_tile_info[loc].pos` into a screen point and clicked by `ctrler()->click`.

This gives SpecialSkillAI a reusable operator-click primitive, provided the target operator has already been registered in `m_battlefield_opers`.

### 2. Current MAA How Judges Skill Ready

`BattleHelper::is_skill_ready(loc, image)` converts the logical tile to a battlefield screen point, then uses `BattlefieldClassifier` with `skill_ready=true` and `set_base_point`. This returns `skill_ready.ready`.

The readiness detector is local to a deployed operator/tile. It does not understand secondary targeting state after a skill button is clicked.

### 3. Current MAA How Clicks Skill

`BattleHelper::use_skill(loc, keep_waiting)` performs:

1. `click_oper_on_battlefield(loc)`
2. `click_skill(keep_waiting)`

`click_skill` uses `get_top_view`, template task `BattleSkillReadyOnClick-TopView`, and then clicks `m_skill_button_pos`.

This covers L1 skills: click operator, click skill.

### 4. Target Selection State After Skill Click

Current normal skill flow treats `click_skill` success as completion. It does not maintain a state machine for ?skill button clicked, now select a target/tile/summon?. Existing `BattlefieldMatcher` can detect battle flag, deployment list, kills, costs, speed/pause button; `BattlefieldClassifier` can detect skill ready and deploy direction. Neither exposes a generic target-selection-state result.

A future SpecialSkillAI therefore needs a small state detector for secondary targeting UI, cancel/fallback behavior, and timeout handling.

### 5. Generic Map Target Click Capability

MAA already has a generic way to click a logical battlefield tile: the same `m_normal_tile_info` and `m_side_tile_info` maps used by deploy, retreat, and battlefield operator clicks convert grid locations to screen points. Copilot actions also accept `location` as logical tile coordinates.

What is missing is not ?click map tile?; it is ?know which target tiles are legal after a specific skill enters target selection?.

### 6. Existing Summon Capability

Summons are represented mainly as `Role::Drone` in battle definitions. Roguelike battle logic includes `check_drone_tiles`, `m_need_clear_tiles`, and special handling that ignores drones in some deployment counts. `BattleHelper` uses a separate `BattleDroneAvatarData` threshold and avoids replacing existing non-drone operators the same way.

This is enough for basic summon occupancy bookkeeping, but not enough to reason about a specific special skill's summoned object, target candidates, or lifetime beyond existing drone cleanup.

### 7. Reusing Copilot Tile/Grid Coordinates

Yes. `RoguelikeCopilotConfig` parses `replacement_home`, `blacklist_location`, `force_deploy_direction`, `deploy_plan`, and `retreat_plan` with logical `Point(x, y)`. `BattleHelper::calc_tiles_info` and Roguelike `calc_stage_info` use TilePack data to map these logical points to screen positions.

SpecialSkillAI should reuse this coordinate model for target candidates rather than introduce raw coordinates.

### 8. Parts That Need New Vision Analyzer

Needed additions:

- Detect whether the battle UI is in a secondary skill target-selection state.
- Detect legal target tiles/objects for the active special skill.
- Distinguish invalid tile click, valid tile hover/selection, and skill cancel/confirm states if the game shows them differently.
- Optionally detect skill-specific summons or target markers.
- Provide debug captures for false positive target selection, similar in spirit to existing skill-ready debug output.

### 9. Generic SpecialSkillAI Components

The reusable design should include:

- `SkillExecutor`: common execution contract.
- `NormalSkillExecutor`: L1 flow, delegates to existing `BattleHelper::use_skill` in future C++ integration.
- `TargetedSkillExecutor`: L2 flow, click operator, click skill, wait for target-selection state, evaluate targets, click selected target.
- `SkillReadinessDetector`: wrapper over current `is_skill_ready`.
- `BattlefieldEvaluator`: converts battlefield state into `TargetCandidate[]`.
- `TargetSelector`: chooses the highest `tactical_score` valid candidate.
- `SummonManager`: tracks special-skill-created objects without mixing them directly into BattleTask.
- `OperatorAdapterRegistry`: maps operator names to adapters.

Default config must be `enable_special_skill_ai=false`, and when disabled no new evaluator/executor path should be invoked.

### 10. WangAdapter-Specific Logic

`WangAdapter` should only define Wang-specific metadata and scoring hooks, for example:

- operator name: `望`
- skill class: L2 targeted skill
- supported skill ids from current config: V000 uses `skill=3`; no `alternate_skill` is configured
- target preference function once real observations exist
- special summon/target interpretation if Wang's skill produces unique UI affordances

It should not be hardcoded into `BattleTask` or `RoguelikeBattleTaskPlugin`.

## Skill Config Research Note

For JieGarden V000, `望` has:

- group membership in `高台输出`
- full strategy definition in `其他高台`
- `skill=3`
- no `alternate_skill`
- no `skill_usage` / `skill_times`, so current default active-skill behavior depends on `RoguelikeOperInfo` defaults

`RoguelikeSkillSelectionTaskPlugin` clicks `alternate_skill` if configured, then clicks `skill` if configured. It does not compare current elite stage against skill availability. Promotion/elite status is recorded by recruitment and used in battle for attack-range lookup, but the observed code does not automatically switch `skill` versus `alternate_skill` based on elite status.

Therefore, based on current code/config only, Wang S3 is selected when available by JSON configuration. There is no current resource evidence that S2/S3 are automatically switched by elite stage for `望`.

## Proposed Interface Shape

The Phase 3 lab prototype lives in `roguelike-lab/special_skill_ai/` and models this future C++ structure:

```text
SpecialSkillAI
|-- SkillExecutor
|   |-- NormalSkillExecutor
|   `-- TargetedSkillExecutor
|-- BattlefieldEvaluator
|-- TargetSelector
|-- SummonManager
|-- SkillReadinessDetector
`-- OperatorAdapter
    `-- WangAdapter
```

`BattlefieldEvaluator` receives a `BattlefieldState` that may include map tiles, deployed operators, summons, enemies, enemy density/path, home tiles, available target tiles, skill state, kill count, and stage name.

It returns `TargetCandidate[]` with:

- `location`
- `valid`
- `threat_score`
- `tactical_score`
- `reason`

`TargetSelector` chooses the legal candidate with the highest `tactical_score`, with `threat_score` as a deterministic tie-breaker in the lab prototype.

## Compatibility Contract

`enable_special_skill_ai=false` is the default. When false, future Core integration must return before calling readiness, adapters, target evaluators, or click routines. This preserves existing `BattleTask`, `Copilot`, Roguelike autopilot, and normal skill auto-use behavior.
