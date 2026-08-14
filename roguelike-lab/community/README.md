# Community Strategy Imports

This directory stores external Roguelike strategy references for later comparison. Community files are inputs for research, not trusted replacements for MAA resources.

Do not assume a third-party `recruitment.json` is compatible with the current MAA schema or with the current base commit.

## Required Layout

Each source must use its own directory:

```text
roguelike-lab/community/<source-id>/
  metadata.json
  original/
    recruitment.json
  normalized/
    recruitment.json
  analysis/
    static_analysis.md
    diff_vs_V000.md
    diff_vs_V000.json
```

`original/` preserves the imported file unchanged. `normalized/` is optional and may contain a schema-adjusted copy for analysis. Never edit `original/`.

## Required Metadata

`metadata.json`:

```json
{
  "source": "community post, PR, issue, personal test, etc.",
  "url": "https://example.invalid/source",
  "author": "name or unknown",
  "date_collected": "YYYY-MM-DD",
  "target_theme": "JieGarden",
  "MAA_version_if_known": "vX.Y.Z or commit",
  "notes": "Important context, account assumptions, difficulty, mode, known limitations."
}
```

## Compatibility Check

Before comparing or using an imported strategy:

1. Run static schema analysis:

   ```powershell
   C:\Users\Arthas\AppData\Local\Programs\Python\Python312\python.exe roguelike-lab\tools\recruitment_static_analyzer.py `
     roguelike-lab\community\<source-id>\original\recruitment.json `
     --md-out roguelike-lab\community\<source-id>\analysis\static_analysis.md `
     --json-out roguelike-lab\community\<source-id>\analysis\static_analysis.json
   ```

2. Compare with the current V000 baseline:

   ```powershell
   C:\Users\Arthas\AppData\Local\Programs\Python\Python312\python.exe roguelike-lab\tools\recruitment_diff.py `
     roguelike-lab\baseline\JieGarden\recruitment.json `
     roguelike-lab\community\<source-id>\original\recruitment.json `
     --md-out roguelike-lab\community\<source-id>\analysis\diff_vs_V000.md `
     --json-out roguelike-lab\community\<source-id>\analysis\diff_vs_V000.json
   ```

3. If analysis reports unknown groups, missing fields, incompatible top-level structure, or unparseable offsets, create a `normalized/` copy and document every compatibility edit in `metadata.json`.

## Import Rules

- Keep imported files versioned by source.
- Record whether the source targets `JieGarden` specifically.
- Record whether it was tested on the same MAA commit as V000.
- Treat score changes, group changes, and offsets as hypotheses until real runs are recorded in `roguelike-lab/results/`.
- Do not copy community strategy directly over official MAA files.
