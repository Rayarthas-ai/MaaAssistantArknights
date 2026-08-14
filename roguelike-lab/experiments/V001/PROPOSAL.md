# V001 Candidate Proposal

Status: proposal only. No strategy JSON has been modified.

Theme: `JieGarden`
Baseline: `roguelike-lab/baseline/JieGarden/recruitment.json`
Base MAA commit: `00da4c367d3167ef732167854314e361b5d5d37f`

## Goal

Design a narrow first candidate for JieGarden recruitment tuning while preserving the official baseline. V001 should be a controlled JSON experiment, not a broad rewrite.

## Candidate Direction A: Core Output Priority

Hypothesis: early runs are most sensitive to whether the team obtains at least one high-value carry and enough follow-up damage.

JSON currently can implement:

- Tune `recruit_priority` and `promote_priority` for existing core-output operators.
- Mark or unmark `is_start` and `is_key`.
- Use negative `recruit_priority_offsets` to reduce redundant carries after the first one is secured.
- Use `team_complete_condition` to require a minimum number of core-output groups.

JSON cannot implement:

- Evaluate map-specific carry suitability.
- Compare actual support skill/module quality.
- Spend hope optimally across future unknown tickets.

Core changes needed:

- State-aware scoring that considers current hope, difficulty, floor, route, and boss target.

## Candidate Direction B: Medical Minimum Guarantee

Hypothesis: failure may cluster around runs that obtain output but lack reliable healing.

JSON currently can implement:

- Raise `recruit_priority` for selected medic/healing groups when healing count is low.
- Use `recruit_priority_offsets` with `is_less=true` against healing groups.
- Keep the team-complete healing condition at one or tune it after baseline tests.

JSON cannot implement:

- Distinguish effective healing coverage by map shape.
- Reason about healing from collectibles or temporary effects unless represented as existing collection offsets.

Core changes needed:

- Richer team-state evaluator that classifies healing quality, not just group membership.

## Candidate Direction C: Ground Blocking Minimum Guarantee

Hypothesis: some failed runs may have enough damage but too little reliable ground presence.

JSON currently can implement:

- Raise priority for ground block/summon/Kal'tsit-style stabilizers while the relevant groups are below threshold.
- Downrank extra ground units after the second stabilizer is present.
- Keep separate deploy group metadata for battle behavior.

JSON cannot implement:

- Understand lane pressure or map-specific blocking requirements during route selection.

Core changes needed:

- Route/battle-aware recruitment scoring.

## Candidate Direction D: Avoid Repeated Over-Recruitment By Role

Hypothesis: once a role lane is covered, duplicate recruitment can waste hope or slots.

JSON currently can implement:

- Negative `recruit_priority_offsets` by group.
- Lower `recruit_priority_when_team_full` for low-impact duplicates.
- Keep high `promote_priority_when_team_full` for elite upgrades instead of more bodies.

JSON cannot implement:

- General class balancing by exact current hope and ticket type.
- Detect that two operators overlap tactically despite living in different groups unless manually encoded.

Core changes needed:

- A role/utility model outside manual group offsets.

## Candidate Direction E: Team Complete Then High-Value Promotion

Hypothesis: after the minimum team shell exists, promotions are often more valuable than extra low-impact recruits.

JSON currently can implement:

- Increase `promote_priority_when_team_full` for selected high-value operators.
- Decrease `recruit_priority_when_team_full` for filler.
- Tune default promote/recruit full values explicitly for key operators.

JSON cannot implement:

- Decide promotion value from current relics and future boss target unless manually encoded via `collection_priority_offsets`.

Core changes needed:

- Promotion scoring that consumes full run state.

## Candidate Direction F: Temporary Recruitment Interaction

Hypothesis: temporary recruitment can distort team structure because MAA adds hard-coded priority to temporary operators.

JSON currently can implement:

- Lower base priority for operators that become undesirable when temporary.
- Use group offsets so temporary duplicates are less attractive after a lane is filled.

JSON cannot implement:

- Change the hard-coded temporary recruitment bonus.
- Treat temporary Elite 2 as a separate candidate class in JSON.

Core changes needed:

- Configurable temporary-recruitment weighting.

## Candidate Direction G: Hope Shortage Handling

Hypothesis: when hope is low, the current JSON can approximate thrift only indirectly.

JSON currently can implement:

- Prefer low-rarity or reserve operators by score.
- Downrank high-cost duplicates after team-complete conditions are met.

JSON cannot implement:

- Read current hope directly in `recruitment.json`.
- Conditional scoring based on exact hope, ticket type, or planned future upgrades.

Core changes needed:

- Hope-aware recruitment policy fields or C++ scoring hooks.

## Recommended V001 Narrow Scope

Do not modify every group. Recommended first V001 should only change:

1. A small set of healing-priority offsets if V000 tests show healing shortages.
2. A small set of ground-blocking offsets if V000 tests show lane leaks.
3. Explicit `*_when_team_full` values for high-value promotion candidates.
4. At most one `team_complete_condition` threshold, and only after V000 run evidence.

## Required Evidence Before Editing JSON

Collect V000 results first:

- run success/failure
- final floor
- failure reason
- opening operator/support
- first 5 recruited operators
- whether at least one healer was recruited before floor 3
- whether at least two ground stabilizers were recruited before floor 3
- whether promotions were available but skipped
- recognition errors

V001 should be generated only after those results identify a dominant failure mode.
