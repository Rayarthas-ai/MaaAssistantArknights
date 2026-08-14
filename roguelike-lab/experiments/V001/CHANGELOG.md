# V001 Changelog - JieGarden Wang-First Recruitment

Base MAA commit: `00da4c367d3167ef732167854314e361b5d5d37f`

## Scope

V001 changes only `roguelike-lab/experiments/V001/recruitment.json`. It does not overwrite `resource/roguelike/JieGarden/recruitment.json`, and it does not change encounter, shopping, route, autopilot, Support Core, Battle Core, or Roguelike Core.

## Minimal-Change Rule

Wang-First must follow the smallest useful JSON change. V001 therefore does **not** change `is_start` or `is_key` by default. The current experiment first tests whether priority fields alone can make `望` the first recruitment and promotion core. If later game-run logs prove the existing start/key gating prevents `望` from being selected when offered, then a separate V002 proposal can evaluate flag changes with evidence.

## Current Wang Baseline

`望` appears twice in V000:

| Group | Fields |
| --- | --- |
| `高台输出` | Group membership only; no priority or skill metadata. |
| `其他高台` | `skill=3`, `recruit_priority=600`, `promote_priority=600`; no explicit full-team priorities, no `is_start`, no `is_key`, no `alternate_skill`, no offsets. |

Because `RoguelikeRecruitConfig` stores operator info by operator name while still retaining group ids, the complete definition in `其他高台` is the strategy-bearing definition V001 modifies.

## Changes

| Field | Before | After | Why | Expected impact | Potential side effect |
| --- | ---: | ---: | --- | --- | --- |
| `recruit_priority` | 600 | 3000 | Enforce the manual hypothesis that `望` is first Carry before she is obtained, without changing start/key flags. | `望` should outrank ordinary six-star Carry choices through score alone when she is eligible for scoring. | If MAA's start/key gating applies before score comparison, priority alone may still be insufficient. |
| `promote_priority` | 600 | 3000 | Enforce promotion focus after `望` has been recruited but is not yet at the key promotion state. | Promotion ticket decisions should strongly favor `望`. | May delay promotion of a stabilizing medic/blocker in edge cases. |
| `recruit_priority_when_team_full` | implicit 500 | 3000 | Keep the Wang-first score active if the team is considered full by MAA's current status logic. | Avoids full-team score fallback suppressing `望`. | Full-team state cannot distinguish whether `望` is already complete. |
| `promote_priority_when_team_full` | implicit 900 | 3000 | Keep promotion focus active in full-team mode. | Promotion selection remains consistent with the Wang-first hypothesis. | JSON cannot express ?only until key promotion complete?. |

## Explicit Non-Changes

- `is_start` remains absent/false.
- `is_key` remains absent/false.
- `skill` remains `3` because V000 already selects skill 3 for `望`.
- `alternate_skill` remains absent because V000 does not define it, and current code does not infer an elite-aware alternate skill from recruitment JSON.
- No offsets were added. Current JSON offsets can reference groups, not ?has exactly Wang and Wang is promoted?; adding a dedicated Wang group would be a larger schema/strategy change.
- `team_complete_condition` is unchanged.

## Flag Risk To Validate

Current Core logic applies large penalties to non-start operators before `starts_complete` and to non-key operators before `team_complete`. V001 intentionally does not bypass those gates yet. Actual run logs must record whether `望` was offered but skipped before the run reached start/team completion.

## Generated Artifacts

- `V000_V001_RECRUITMENT_DIFF.md`
- `V000_V001_RECRUITMENT_DIFF.json`
- `STATIC_ANALYSIS.md`
- `STATIC_ANALYSIS.json`
