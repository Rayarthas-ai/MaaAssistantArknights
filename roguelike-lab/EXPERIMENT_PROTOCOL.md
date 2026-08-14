# Experiment Protocol

## Purpose

Run controlled Roguelike strategy experiments without overwriting official MAA resources or assuming a strategy is better before test evidence exists.

## Environment Split

Company development machine:

- Analyze code and resources.
- Modify JSON only inside `roguelike-lab/experiments/Vxxx/` unless a later phase explicitly approves a core change.
- Run static checks and unit tests where available.
- Generate candidate strategy files and reports.
- Do not start emulator or connect to the game.

Game-testing machine:

- Applies a selected experiment version to a test MAA copy.
- Runs real games.
- Exports logs and normalized result files.

## Version Workflow

1. Select one target theme/mode and one variable family.
2. Create `roguelike-lab/experiments/Vxxx/`.
3. Copy only the files that may change from `baseline/V000/resource/roguelike/`.
4. Add `metadata.md` before editing.
5. Make minimal JSON changes.
6. Record expected effects.
7. Test externally.
8. Store results in `roguelike-lab/results/Vxxx/`.
9. Add analysis in `roguelike-lab/analysis/Vxxx.md`.
10. Decide: keep, revise, rollback, or escalate to core-change proposal.

## Metadata Template

```markdown
# Vxxx Experiment Metadata

Strategy version: Vxxx
Base MAA commit: <commit>
Created at: <date/time>
Theme:
Mode:
Difficulty:

## Modified Files

- `path`: reason

## Hypothesis

Describe exactly what should improve and why.

## Expected Impact

- Success rate:
- Average final floor:
- Failure modes expected to decrease:
- Risks/regressions:

## Test Plan

- Number of runs:
- Game-testing machine:
- MAA version/build:
- Account assumptions:

## Actual Results

Fill after external testing.

## Decision

Keep / revise / rollback / propose core change.
```

## Result File Naming

Recommended:

```text
roguelike-lab/results/Vxxx/YYYYMMDD-HHMMSS-<theme>-<run_id>.json
```

For batches, JSONL is acceptable:

```text
roguelike-lab/results/Vxxx/YYYYMMDD-<theme>-batch.jsonl
```

## Rollback

Rollback is deleting or ignoring the experiment directory. Official resources remain unchanged. If an experiment was manually applied to a game-testing copy, restore from `baseline/V000` or upstream MAA resources.

## Escalation To Core Change

Open a core-change proposal only when repeated results show that JSON cannot represent the needed behavior. The proposal must include:

- observed failure evidence
- why JSON cannot solve it
- smallest C++/TaskData surface to change
- compatibility risk
- validation plan
