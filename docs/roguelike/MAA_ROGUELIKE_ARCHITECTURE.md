# MAA Roguelike Strategy Architecture

Base MAA commit: `00da4c367d3167ef732167854314e361b5d5d37f`

This document records how the current MAA roguelike strategy resources are structured, which code reads them, and where strategy experiments can stay JSON-only versus requiring core code changes. Phase 1 is descriptive: it does not claim that any strategy is better than upstream.

## Scope

Scanned areas:

- `resource/roguelike/`
- `src/MaaCore/Config/Roguelike/`
- `src/MaaCore/Task/Roguelike/`
- `src/MaaCore/Task/Interface/RoguelikeTask.cpp`
- `src/MaaCore/Vision/Roguelike/`
- `src/MaaCore/Ui/SupportList.*`
- `docs/*/protocol/integrated-strategy-schema.md`

Primary keywords indexed: recruitment, encounter, shopping, investment, squad, support unit, route/node, relic/collectible, autopilot, battle, difficulty, ending.

## Resource Inventory

`resource/roguelike/` currently contains five themes:

| Theme | Root JSON | Encounter JSON | Autopilot JSON | Special files |
| --- | ---: | ---: | ---: | --- |
| `Phantom` | 2 | 2 | 47 | none found |
| `Mizuki` | 2 | 2 | 48 | none found |
| `Sami` | 4 | 3 | 55 | `foldartal.json`, `collapsal_paradigms.json` |
| `Sarkaz` | 4 | 1 | 30 | `fragments.json`, `map.json` |
| `JieGarden` | 4 | 1 | 38 | `coppers.json`, `map.json` |

Root JSON files by convention:

- `recruitment.json`: operator grouping, recruitment score, promotion score, start/key flags, deploy skill metadata.
- `shopping.json`: collectible/relic buying order and conditional filters.
- `map.json`: node-template-to-node-type mapping for routing-capable themes.
- `foldartal.json`: Sami foldartal combination rules.
- `collapsal_paradigms.json`: Sami collapsal paradigm classes.
- `fragments.json`: Sarkaz idea/fragment data.
- `coppers.json`: JieGarden copper pickup/discard strategy.

Subdirectories:

- `autopilot/*.json`: per-stage battle deployment plans.
- `encounter/default.json`: default encounter option strategy.
- `encounter/deposit.json`: deposit/start-related encounter option strategy where present.
- `encounter/collapse.json`: Sami collapsal paradigm mode encounter strategy.

## Runtime Entry Point

`src/MaaCore/Task/Interface/RoguelikeTask.cpp` registers the roguelike plugin pipeline. The important plugins are:

- `RoguelikeCustomStartTaskPlugin`: initial theme/squad/role/core-char setup.
- `RoguelikeDifficultySelectionTaskPlugin`: difficulty selection.
- `RoguelikeRecruitTaskPlugin`: recruitment and initial support selection.
- `RoguelikeSkillSelectionTaskPlugin`: selected operator skill setup.
- `RoguelikeFormationTaskPlugin`: team formation recognition/reordering.
- `RoguelikeBattleTaskPlugin`: battle execution using autopilot data.
- `RoguelikeShoppingTaskPlugin`: trader collectible purchase logic.
- `RoguelikeStageEncounterTaskPlugin`: encounter option logic.
- `RoguelikeRoutingTaskPlugin` and `RoguelikeBoskyPassageRoutingTaskPlugin`: route/node navigation for supported special modes.
- `RoguelikeInvestTaskPlugin`: investment behavior.
- `RoguelikeSettlementTaskPlugin`, `RoguelikeResetTaskPlugin`, `RoguelikeControlTaskPlugin`: run lifecycle and restart control.

`RoguelikeConfig::verify_and_load_params` stores task parameters such as `theme`, `mode`, `difficulty`, `squad`, `start_with_elite_two`, and mode-specific flags. It also chooses TaskData strategy bases for some hard-coded theme/mode/squad combinations.

## JSON Schemas And Readers

### `recruitment.json`

Reader: `src/MaaCore/Config/Roguelike/RoguelikeRecruitConfig.cpp`.

Top-level shape:

```json
{
  "theme": "Sami",
  "priority": [
    {
      "name": "group name",
      "opers": [
        {
          "name": "operator name",
          "skill": 3,
          "alternate_skill": 2,
          "skill_usage": 1,
          "skill_times": 1,
          "alternate_skill_usage": 1,
          "alternate_skill_times": 1,
          "recruit_priority": 900,
          "promote_priority": 600,
          "is_key": true,
          "is_start": true,
          "is_alternate": false,
          "auto_retreat": 0,
          "recruit_priority_when_team_full": 800,
          "promote_priority_when_team_full": 900,
          "recruit_priority_offsets": [
            { "groups": ["group"], "threshold": 1, "is_less": false, "offset": -300 }
          ],
          "collection_priority_offsets": [
            { "collection": "collectible name", "offset": 100 }
          ]
        }
      ]
    }
  ],
  "team_complete_condition": [
    { "groups": ["group A", "group B"], "threshold": 2 }
  ]
}
```

Actual effects:

- `priority[].name` creates a group. Group order also becomes the fallback group id order.
- `priority[].opers[]` records operator group membership and order in group. This affects battle deployment priority when autopilot `deploy_plan.groups` asks for a group.
- `recruit_priority` scores new recruitment.
- `promote_priority` scores promotion for already owned operators.
- `is_start` protects opening recruitment until a start operator is obtained; non-start operators are penalized before that.
- `is_key` protects team completion; non-key operators are penalized until `team_complete_condition` is satisfied.
- `recruit_priority_offsets` changes a candidate score based on current team composition.
- `collection_priority_offsets` changes a candidate score based on already held collectibles.
- `skill`, `alternate_skill`, `skill_usage`, `skill_times`, and `auto_retreat` are used later by skill selection and battle deployment.

Core logic not controlled by JSON:

- Default minimum recruitment practice is hard-coded in `RoguelikeRecruitTaskPlugin`: Elite 2 is allowed; Elite 1 requires level >= 55 or level OCR result 0. Elite 1 below 55 is heavily penalized.
- Temporary recruitment receives hard-coded score bonuses.
- If no candidate is found, MAA may fallback to an Elite 2 temporary recruitment.
- After repeated recruitment failures, start/team-complete restrictions are relaxed.
- Unknown operators are assigned to fallback ground/high-ground groups through C++ role/location logic.

### `shopping.json`

Reader: `src/MaaCore/Config/Roguelike/RoguelikeShoppingConfig.cpp`.

Top-level shape:

```json
{
  "theme": "Sami",
  "priority": [
    {
      "name": "collectible name",
      "roles": ["WARRIOR", "SNIPER"],
      "chars": ["operator name"],
      "promotion": 1,
      "promotion_rarity": 6,
      "no_longer_buy": false,
      "ignore_no_longer_buy": false,
      "decrease_collapse": false,
      "effect": "documentation only",
      "No": 123
    }
  ],
  "others": [
    { "name": "ignored/documented collectible" }
  ]
}
```

Actual effects:

- `priority` order is the purchase order. The plugin scans OCR results and buys the first configured item that matches all filters.
- `roles` requires the current team to contain at least one matching role.
- `chars` requires the current team to contain at least one matching operator.
- `promotion` and `promotion_rarity` require operators waiting for promotion.
- `no_longer_buy` sets a run-state flag after purchase; later items are skipped unless `ignore_no_longer_buy` is set.
- `decrease_collapse` is skipped in Sami collapsal-paradigm mode.
- `effect`, `No`, and similar notes are documentation-only.

Core logic not controlled by JSON:

- The shop refresh pattern is hard-coded by theme/mode.
- Purchase affordability, OCR matching behavior, and click/confirm flows are TaskData/C++ behavior.
- The role/char filters only see operators recorded in current run status.

### `encounter/*.json`

Reader: `src/MaaCore/Config/Roguelike/RoguelikeStageEncounterConfig.cpp`.

Shape:

```json
{
  "theme": "Sami",
  "mode": [5],
  "stage": [
    {
      "name": "event name",
      "option_text": ["optional OCR text"],
      "option_num": 3,
      "choose": 2,
      "next_event": "event name",
      "fallback_choices": [[3, 2], [2, 1]],
      "choices": [
        {
          "name": "choice name",
          "choose": 1,
          "requirements": [
            { "name": "Vision", "value": "3", "type": ">" },
            { "name": "Relic", "value": "x", "type": "=" }
          ]
        }
      ]
    }
  ]
}
```

Actual effects:

- `name` identifies the encounter by OCR.
- `option_num` and `choose` define the default option index.
- `fallback_choices` chooses alternatives when detected option count differs.
- `choices[].requirements` currently supports `Vision`; `Relic` is explicitly not supported in parser logic.
- Mode-specific files can inherit default event config and override entries.

Core logic not controlled by JSON:

- Event detection, option click coordinates, and unavailable-choice handling live in C++/TaskData.
- Dynamic route-to-ending logic based on current team/relics is limited; many `choices` fields are annotations or only partially supported.

### `autopilot/*.json`

Reader: `src/MaaCore/Config/Roguelike/RoguelikeCopilotConfig.cpp`.

Shape:

```json
{
  "stage_name": "stage name",
  "replacement_home": [
    { "location": [6, 4], "direction": "left" }
  ],
  "blacklist_location": [[0, 0]],
  "not_use_dice": false,
  "role_order": ["warrior", "pioneer", "medic", "tank", "sniper", "caster", "support", "special", "drone"],
  "force_air_defense_when_deploy_blocking_num": {
    "melee_num": 2,
    "air_defense_num": 1,
    "ban_medic": false
  },
  "force_deploy_direction": [
    { "location": [3, 1], "role": ["sniper"], "direction": "left" }
  ],
  "deploy_plan": [
    { "groups": ["ground block"], "location": [6, 4], "direction": "left", "condition": [0, 10] }
  ],
  "retreat_plan": [
    { "location": [4, 1], "condition": [7, 8] }
  ]
}
```

Actual effects:

- `stage_name` maps OCR-recognized stage name to a battle plan.
- `replacement_home` overrides blue-box defensive anchors for fallback deployment.
- `blacklist_location` blocks deployment at coordinates.
- `not_use_dice` disables Mizuki dice behavior for that stage.
- `deploy_plan` flattens group/location steps into ranked deploy candidates.
- `retreat_plan` schedules retreats by kill-count condition.
- `role_order`, `force_air_defense_when_deploy_blocking_num`, and `force_deploy_direction` exist but are discouraged in upstream docs in favor of explicit deploy plans.

Core logic not controlled by JSON:

- Generic fallback battle algorithm, map tile recognition, kill-count recognition, skill auto-use timing, and unavailable tile handling are C++.
- JSON cannot currently express hold-skill timing or close-skill behavior; upstream docs mark these as TODO.

### `map.json`

Reader: `src/MaaCore/Config/Roguelike/RoguelikeMapConfig.cpp`.

Shape:

```json
{
  "theme": "Sarkaz",
  "nodes": [
    { "type": "CombatOps", "template": ["template name"] }
  ]
}
```

Actual effects:

- Maps node icon template names to enum node types.
- Used by routing plugins after template matching.

Core logic not controlled by JSON:

- Path graph generation, edge detection, route cost function, refresh behavior, and restart thresholds are hard-coded in routing plugins.
- General routing is only enabled for selected theme/mode/squad combinations.

### Theme-special JSON

`Sami/foldartal.json`:

- Reader: `RoguelikeFoldartalConfig.cpp`.
- Controls foldartal pair combinations by `usage` and ordered `up`/`down` lists.
- Used by `RoguelikeFoldartalUseTaskPlugin`.

`Sami/collapsal_paradigms.json`:

- Reader: `RoguelikeCollapsalParadigmConfig.cpp`.
- Defines level-1 and level-2 collapsal paradigm classes.
- Used by `RoguelikeCollapsalParadigmTaskPlugin`.

`JieGarden/coppers.json`:

- Reader: `RoguelikeCoppersConfig.cpp`.
- Controls `pickup_priority`, `discard_priority`, and optional `cast_discard_priority`.
- Used by `RoguelikeCoppersTaskPlugin` for pickup and exchange decisions.

`Sarkaz/fragments.json`:

- Theme-specific idea/fragment data. Treat as strategy-adjacent; verify reader before changing in experiments.

## Decision Flow

1. User/API passes a `Roguelike` task with `theme`, `mode`, `squad`, `roles`, `core_char`, `difficulty`, and optional flags.
2. `RoguelikeConfig` validates parameters and selects mode-specific TaskData bases.
3. Custom start selects theme, squad, roles, core operator, support usage, and difficulty.
4. Recruitment chooses opening operator/support, then later recruitment tickets based on `recruitment.json` plus hard-coded filters and run state.
5. Skill selection uses the chosen operator metadata from `recruitment.json`.
6. Formation records current operators into `RoguelikeStatus`.
7. Stage routing/strategy selection enters nodes. For most modes this is TaskData strategy; for selected Sarkaz/JieGarden modes C++ routing builds a node graph.
8. Battle uses `autopilot/<stage>.json` if a stage plan exists; otherwise falls back to generic battle logic.
9. Encounters use `encounter/*.json` to choose options after OCR identifies the event.
10. Shopping uses `shopping.json` priority order and current run status to buy collectibles.
11. Settlement/reset/control plugins update lifecycle and repeat according to mode.

## A. Opening Support Selection

Current support status:

- Supported for opening recruitment through task parameter `use_support=true`.
- `use_nonfriend_support` controls whether non-friend support can be accepted.
- The requested support operator is `core_char`.
- `RoguelikeRecruitTaskPlugin` only attempts support on the first initial recruitment.
- If support selection fails, it falls back to own-operator recruitment.

How support is selected:

- `RoguelikeRecruitTaskPlugin::recruit_support_char()` gets max refresh times from TaskData key `RoguelikeRefreshSupportBtnOcr`.
- It clicks the choose-support button if detected by `RoguelikeRecruitSupportAnalyzer`.
- It scans up to two support-list pages per refresh cycle.
- It filters candidates by exact required name and friend/non-friend permission.
- It refreshes the support list until max refresh count or cooldown handling blocks progress.
- It selects the first satisfying candidate collected, then confirms.

What it compares today:

| Feature | Current opening roguelike support behavior |
| --- | --- |
| Operator name | Yes, exact required `core_char` through OCR required list. |
| Friend/non-friend | Yes, via red-channel color heuristic. |
| Level | Recognized and recorded, but not used to rank candidates except invalid level is discarded. |
| Elite | Recognized and recorded; Elite 2 support is downgraded to the max recruitable Elite 1 level for rarity > 3. Not used to rank among candidates. |
| Skill level | Not used by this opening roguelike support path. |
| Module | Not used by this opening roguelike support path. |
| Active refresh | Yes, up to TaskData max refresh times, with cooldown waiting. |
| Strongest among candidates | No. It selects the first candidate satisfying name and friend policy. |

Important nuance:

- `src/MaaCore/Ui/SupportList.cpp` has generic support-list APIs that can select skill and module with minimum levels, but the current roguelike opening recruitment path uses `RoguelikeRecruitSupportAnalyzer` and does not call `SupportList::select_skill` or `SupportList::select_module`.

JSON-only optimization possible:

- Choose whether to use support (`use_support`) and which operator name to seek (`core_char`) from task parameters/profile, not `resource/roguelike`.
- JSON resources cannot currently express minimum skill level, module, or candidate ranking for opening support.

Core changes required:

- Compare support candidates by Elite/level/skill/module.
- Prefer friend over non-friend only after strength comparison, or vice versa.
- Select a specific support skill/module in the opening roguelike flow.
- Continue refreshing until a strictly stronger candidate appears.

## B. Recruitment Strategy

Current mechanism:

- Candidate operators are OCR-recognized across the recruit list pages.
- For each candidate, C++ looks up `RoguelikeRecruit.get_oper_info(theme, name)`.
- If the operator is already in team, score becomes promotion priority unless it is an alternate/reserve-style operator.
- If not in team, score starts from recruitment priority, promotion priority may be added for Elite 2 candidates.
- Elite 1 operators below level 55 are heavily penalized by core logic.
- Temporary recruitment adds a hard-coded bonus.
- `recruit_priority_offsets` and `collection_priority_offsets` adjust score using current team/relic state.
- Before start completeness is satisfied, non-`is_start` operators are penalized.
- Before team completeness is satisfied, non-`is_key` operators are penalized.
- Highest score wins; if there are no candidates, fallback logic may choose Elite 2 temporary recruitment.

`team_complete_condition` meaning:

- Each condition contains groups and a threshold.
- MAA expands groups to unique operator names and counts already recruited operators matching those groups.
- Every condition must meet its threshold for team completeness.
- An operator duplicated across groups counts once inside one condition, but can contribute to separate conditions independently.

Existing-team impact:

- Current operators are stored in `m_config->status().opers` with elite/level.
- Already owned operators shift duplicate appearances into promotion scoring.
- Team composition can trigger `recruit_priority_offsets`.
- Current collectibles can trigger `collection_priority_offsets`.
- Shopping and battle also read the same run-state operator list.

Profession/team-structure补强:

- Configurable補強 exists through group conditions and priority offsets.
- Legacy role-count offsets still exist in code but are marked will-be-removed.
- There is no general optimizer that reasons from current map, HP/life, hope, ending target, and exact future risk; it is score/rule based.

JSON-only optimization possible:

- Reorder groups and operators within groups.
- Tune `recruit_priority`, `promote_priority`, start/key flags, and team-complete thresholds.
- Add or adjust `recruit_priority_offsets` and `collection_priority_offsets`.
- Tune skill metadata and `auto_retreat` for battle behavior.

Core changes required:

- Change minimum level/elite thresholds.
- Add skill-level or module-level checks during recruitment.
- Add hope-aware or life-aware scoring if not already present in status fields used by the plugin.
- Add lookahead over future stages/routes/endings.
- Add a learned/evaluation-based selection policy.

## C. Route Selection

Current route behavior has two layers:

1. Default TaskData route/strategy tasks for most themes/modes.
2. C++ routing plugins for selected special cases.

`RoguelikeRoutingTaskPlugin` is currently limited by `load_params` to:

- Sarkaz FastPass with blueprint squad.
- Sarkaz Investment with point-stab squad.
- JieGarden Investment/Collectible with command squad and difficulty >= 3.

How nodes are selected in C++ routing:

- `map.json` maps node icon templates to node types.
- The plugin template-matches visible nodes and uses pixel analysis to infer edges.
- It assigns hard-coded costs by route strategy.
- Sarkaz FastPass tries to avoid combat nodes by giving combat/emergency/dreadful nodes cost `1` and refreshed combat nodes cost `1000`.
- JieGarden FastPass variants assign combat costs and restart if unavoidable battle count exceeds hard-coded thresholds.
- Some combat nodes are actively refreshed once, then reclassified.

Whether it considers state:

| State | Current C++ routing evidence |
| --- | --- |
| Node priority | Yes, through hard-coded cost functions and some TaskData strategy bases. |
| Current team | Not in C++ route cost functions observed. |
| Life/HP | Not in observed route cost functions. |
| Hope | Not in observed route cost functions. |
| Collectibles/relics | Not in observed route cost functions. |
| Target ending | Mostly encounter strategy/TaskData dependent; no general route optimizer observed. |
| Difficulty | Used to enable JieGarden special strategy; not a rich route cost input. |
| Squad/mode/theme | Yes, central to strategy selection. |

JSON-only optimization possible:

- Update `map.json` template-to-type mappings when recognition is wrong.
- Adjust encounter choices that influence endings or special resources.
- Adjust TaskData resources if treating those as config, but this lab currently isolates `resource/roguelike` rather than broad `resource/tasks` changes.

Core changes required:

- General configurable node priority per theme/mode.
- Route cost functions that account for team, life, hope, current relics, difficulty, floor, target ending, and expected battle risk.
- A route policy file separate from TaskData/C++.
- Result feedback loop that updates route policy from actual runs.

## JSON-Only Optimization Boundary

Safe JSON-only experiment variables:

- Operator recruit/promotion scores.
- `is_start`, `is_key`, team completion thresholds.
- Operator group membership and order.
- Team/relic-based recruitment offsets already supported by JSON.
- Per-stage deployment plans, retreat plans, replacement home, deployment blacklist.
- Shop collectible priority and simple role/char/promotion filters.
- Encounter default/fallback choices where parser supports them.
- Sami foldartal pairing priority.
- JieGarden copper pickup/discard priorities.
- Map template node-type mappings for supported routing.

Must modify Core/TaskData for:

- Support selection by skill level/module/best candidate ranking.
- Recruitment threshold changes beyond scores, such as accepting E1 under 55 by policy.
- Dynamic route strategy based on run state.
- Dynamic encounter choices based on relics, team, life, hope, or target ending beyond supported `Vision` requirement.
- Battle skill-hold/skill-close plans.
- A/B experiment runner that automatically consumes game results and mutates strategy.
- Structured run-result export if existing callbacks/logs are insufficient.

## Existing Logs And Result Reuse

Observed code emits structured-ish callbacks in places such as routing restart (`TaskChainExtraInfo` with `what=RoutingRestart`) and foldartal gain. Most run information is also present in logs through `Log.info`/`Log.trace` for chosen operators, support list, shopping purchases, route costs, collapsal paradigms, etc.

Phase 1 should reuse these logs when analyzing external game-machine runs. The lab result schema intentionally records normalized outputs derived from logs/manual notes rather than requiring MAA core changes now.

## Recommended First Experiment Variables

Do not start V001 in phase 1. For the first real experiment, prefer one variable family at a time:

1. Recruitment score tuning for one theme only, probably `Sami` or `JieGarden`.
2. Opening `core_char` / `use_support` policy comparison, without changing support internals.
3. Team-complete thresholds for early stability versus hope conservation.
4. Shop priority changes for a small list of high-impact collectibles.
5. One or two stage autopilot fixes only where external logs show repeated failures.
6. Encounter choices tied to one target ending, with clear success/failure labels.
7. JieGarden copper pickup/discard priorities if tests focus on JieGarden.

## Next Phase Plan

1. Choose one theme and mode as experiment target.
2. Collect 10-20 baseline V000 runs from the game machine using the result schema.
3. Identify the top failure class: recruitment miss, support quality, route risk, battle failure, shop waste, encounter wrong choice, recognition error.
4. Create V001 by copying only the affected baseline files into `roguelike-lab/experiments/V001/`.
5. Record hypothesis and expected impact before testing.
6. Run V001 externally; store normalized result JSON/JSONL under `roguelike-lab/results/V001/`.
7. Compare against V000 in `roguelike-lab/analysis/`.
8. Promote only proven, narrowly scoped changes; otherwise rollback by deleting/ignoring the experiment version.
