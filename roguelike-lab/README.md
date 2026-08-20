# Roguelike Strategy Lab

This directory is an isolated experiment workspace for MAA Integrated Strategy / Roguelike strategy research.

The lab does not overwrite official MAA resources. `resource/roguelike/` remains the upstream baseline. Experiments copy only the files they intend to change.

## Directory Layout

```text
roguelike-lab/
  baseline/      official snapshots, starting with V000
  community/     external notes, shared strategies, manually imported references
  experiments/   versioned experimental strategies V001, V002, ...
  results/       normalized run results from the game-testing machine
  analysis/      comparisons, summaries, charts, and decision notes
```

## Versions

- `V000`: official baseline at the recorded MAA commit.
- `V001`: first experimental strategy. Not created in phase 1.
- `V002+`: later experiments.

Every version must record:

- base MAA commit
- modified files
- reason for changes
- hypothesis
- expected impact
- actual test result

Use `experiments/Vxxx/metadata.md` from the protocol template before changing JSON.

## Current Baseline

`baseline/V000/` contains a copied snapshot of `resource/roguelike/` from commit `00da4c367d3167ef732167854314e361b5d5d37f`.

The generated manifest is `baseline/V000/manifest.json`.

## Safety Rules

Company development environment:

- Allowed: code analysis, JSON modification in lab copies, static checks, unit tests, strategy generation.
- Not allowed: launching an emulator, connecting to the game, running live automation against a game client.

Actual game testing is performed on another machine. Store its normalized output under `results/`.

## First-Phase Status

Phase 1 creates the lab framework and architecture map only. It does not create V001 and does not change upstream strategy files.

## Current Handoff

- [MAA_STRATEGY_AI_HANDOFF.md](MAA_STRATEGY_AI_HANDOFF.md): AI / development working context. Future AI context recovery should read this first.
- [MAA_STRATEGY_AI_HANDOFF_2026-08-19.docx](MAA_STRATEGY_AI_HANDOFF_2026-08-19.docx): frozen human-readable snapshot.
