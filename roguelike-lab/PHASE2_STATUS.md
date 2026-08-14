# Phase 2 Status

Phase 2 scope: JieGarden recruitment research baseline and candidate-generation tooling.

No MAA Core files were modified. Official `resource/roguelike/JieGarden/recruitment.json` was not modified. No emulator or game client was started.

## 1. JieGarden V000 Current Strategy

V000 baseline was copied to:

`roguelike-lab/baseline/JieGarden/recruitment.json`

Static baseline summary:

- Theme: `JieGarden`
- Operator groups: 45
- Operator definitions: 741
- Unique operators/summons/reserves: 417
- Start operator definitions: 49
- Key operator definitions: 89
- Team complete conditions: 4

The official strategy uses:

- `is_start` to protect opening recruitment.
- `is_key` to preserve hope and slots before the team shell is complete.
- `team_complete_condition` to require core output, ground stabilization, healing, and DP/cost recovery.
- `recruit_priority_offsets` to downrank duplicated lanes and upweight missing lanes.
- `collection_priority_offsets` for a small number of collectible-sensitive operators.

Generated analysis:

- `roguelike-lab/analysis/JieGarden_RECRUITMENT_BASELINE.md`
- `roguelike-lab/analysis/JieGarden_RECRUITMENT_STATIC_ANALYSIS.md`
- `roguelike-lab/analysis/JieGarden_RECRUITMENT_STATIC_ANALYSIS.json`

## 2. Most Obvious Potential Weaknesses

These are hypotheses from static analysis only, not proven gameplay conclusions:

- Static analyzer reports references to group `焰苇` that are not found as a group name in the parsed baseline. This affects one `team_complete_condition` and one Kal'tsit offset. It may be a naming/schema drift issue or an intentional-but-stale reference.
- Many operators intentionally appear in multiple groups. The analyzer flags strategy metadata conflicts where the same operator has full metadata in one group and placeholder metadata in another. This is common in MAA group design, but it makes community diff review important.
- Opening and key counts are broad. This may be intentional for account compatibility, but V001 should avoid expanding them further without evidence.
- JSON cannot see current hope directly, so hope-shortage behavior is mostly indirect.
- Temporary recruitment has hard-coded C++ influence, so JSON scores may not fully control its impact.

## 3. Points JSON Can Improve

V001 can safely experiment with:

- Recruit/promote priority tuning inside JieGarden only.
- `is_start` and `is_key` flags for a small operator subset.
- `team_complete_condition` thresholds after V000 run evidence.
- Negative offsets to reduce duplicate role over-recruitment.
- Positive offsets for missing healing, blocking, or DP recovery.
- `*_when_team_full` values to favor promotion over low-impact extra recruitment.
- `collection_priority_offsets` where a collectible clearly changes an operator's value.

## 4. Points JSON Cannot Solve

Current recruitment JSON cannot:

- Compare support operator skill level or module.
- Rank multiple support candidates by real strength.
- Read exact current hope and make hope-aware decisions.
- Evaluate route, current map, final ending target, or future battle risk.
- Change the hard-coded temporary recruitment bonus.
- Change the hard-coded E1 level threshold behavior.

These require Core or TaskData changes in a later phase.

## 5. Recommended V001 Parameters To Modify

Do not create strategy changes until V000 gameplay results are collected. If results confirm recruitment is the dominant failure point, keep V001 narrow:

- Explicitly tune healing offsets for the main healer groups.
- Explicitly tune ground-stabilizer offsets for early floors.
- Tune `recruit_priority_when_team_full` and `promote_priority_when_team_full` for a small list of high-value carries.
- Review the unresolved `焰苇` group reference before changing `team_complete_condition`.
- Avoid changing encounter, shopping, autopilot, route, or support logic in V001.

## 6. Recommended Actual-Test Metrics

Record at least:

- `strategy_version`
- `maa_version` and commit/build if available
- `roguelike_theme`
- mode and difficulty
- `run_id`
- start/end time
- success
- ending
- final floor
- opening operator and whether support was used
- recruited operators in order
- first healer floor/timing
- first ground stabilizer floor/timing
- promotions taken or skipped
- failure reason
- recognition error
- notes and raw log paths

Use `roguelike-lab/results/result.schema.json` as the normalized format.

## 7. Community JSON To Search For Next

Prioritize community sources that:

- Target `JieGarden` specifically.
- Include tested difficulty/mode and run counts.
- Modify only `recruitment.json` or clearly separate recruitment changes from shopping/autopilot changes.
- Explain opening operator assumptions.
- Include failure/success evidence, not just a final JSON.
- Are near the current MAA commit or can be normalized with documented compatibility edits.

Community import rules are documented in `roguelike-lab/community/README.md`.

## Tooling Added

- `roguelike-lab/tools/recruitment_diff.py`
- `roguelike-lab/tools/recruitment_static_analyzer.py`

The diff tool produced a zero-change self diff for V000 baseline.

## Static Checks

Available local static checks run in Phase 2:

- `recruitment_static_analyzer.py` generated Markdown and JSON reports for JieGarden V000.
- `recruitment_diff.py` compared JieGarden V000 against itself and produced an empty diff.

No MAA build, emulator, or game run was started.
