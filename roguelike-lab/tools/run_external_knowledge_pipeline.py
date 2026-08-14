#!/usr/bin/env python3
"""Run the Phase 4 external knowledge pipeline against local raw evidence."""

from __future__ import annotations

import copy
import json
import subprocess
from pathlib import Path
from typing import Any

LAB_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = LAB_ROOT.parent

import sys

sys.path.insert(0, str(LAB_ROOT))

from functional_recruitment.knowledge import (  # noqa: E402
    EvidenceAggregator,
    FileManualImportProvider,
    KnowledgeExtractor,
    KnowledgeSource,
    VersionRelevanceEvaluator,
    build_candidate_profile_patch,
)
from tools.profile_diff import diff_profiles, markdown  # noqa: E402


TARGET_THEME = "JieGarden"
RAW_SOURCE_ID = "phase4-seed-evidence-manual-001"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def git_commit() -> str:
    git = Path("C:/Users/Arthas/AppData/Local/Programs/Git/cmd/git.exe")
    command = [str(git) if git.exists() else "git", "rev-parse", "HEAD"]
    try:
        return subprocess.check_output(command, cwd=REPO_ROOT, text=True, encoding="utf-8").strip()
    except Exception:
        return "unknown"


def discover_seed_source(provider: FileManualImportProvider) -> KnowledgeSource:
    sources = {source.source_id: source for source in provider.discover()}
    if RAW_SOURCE_ID not in sources:
        raise RuntimeError(f"Missing raw source: {RAW_SOURCE_ID}")
    return sources[RAW_SOURCE_ID]


def run_pipeline() -> dict[str, Any]:
    formal_path = LAB_ROOT / "data/operator_function_profiles.json"
    candidate_path = LAB_ROOT / "data/operator_function_profiles_candidate.json"
    weights_path = LAB_ROOT / "data/source_weights.json"
    diff_json_path = LAB_ROOT / "analysis/OPERATOR_FUNCTION_PROFILE_CANDIDATE_DIFF.json"
    diff_md_path = LAB_ROOT / "analysis/OPERATOR_FUNCTION_PROFILE_CANDIDATE_DIFF.md"
    proposal_path = LAB_ROOT / "analysis/KNOWLEDGE_UPDATE_PROPOSAL.md"
    validation_path = LAB_ROOT / "analysis/PHASE4_KNOWLEDGE_PIPELINE_VALIDATION.md"

    formal_profiles = load_json(formal_path)
    source_weights = load_json(weights_path)
    provider = FileManualImportProvider(LAB_ROOT / "knowledge/raw")
    source = discover_seed_source(provider)
    sources = {source.source_id: source}

    extractor = KnowledgeExtractor()
    evidence = extractor.extract_json(provider.load(source.source_id), source.source_id)
    relevance = VersionRelevanceEvaluator(TARGET_THEME)
    aggregator = EvidenceAggregator(source_weights, relevance)
    aggregated = aggregator.aggregate(evidence, sources)

    candidate_profiles = copy.deepcopy(formal_profiles)
    patch = build_candidate_profile_patch(formal_profiles, aggregated)
    candidate_profiles.update(patch)
    write_json(
        candidate_path,
        {
            "metadata": {
                "generated_by": "roguelike-lab/tools/run_external_knowledge_pipeline.py",
                "generated_at": "2026-08-14",
                "base_maa_commit": git_commit(),
                "target_theme": TARGET_THEME,
                "source_ids": [source.source_id],
                "promoted": False,
                "requires_explicit_promote": True,
                "formal_profile_unchanged": True,
            },
            "profiles": candidate_profiles,
        },
    )

    diff = diff_profiles(formal_profiles, candidate_profiles)
    write_json(diff_json_path, diff)
    diff_md_path.write_text(markdown(diff, formal_path, candidate_path), encoding="utf-8")

    proposal_path.write_text(render_proposal(source, evidence, aggregated, diff), encoding="utf-8")
    validation_path.write_text(render_validation(source, evidence, aggregated, diff, formal_path, candidate_path), encoding="utf-8")

    return {
        "source": source,
        "evidence": evidence,
        "aggregated": aggregated,
        "diff": diff,
        "candidate_path": candidate_path,
        "formal_path": formal_path,
    }


def diff_count(diff: dict[str, Any]) -> int:
    return sum(len(value) for value in diff.values() if isinstance(value, list))


def render_proposal(source: KnowledgeSource, evidence: list[Any], aggregated: dict[str, Any], diff: dict[str, Any]) -> str:
    lines = [
        "# Knowledge Update Proposal",
        "",
        "## Scope",
        "",
        f"- Target theme: `{TARGET_THEME}`",
        f"- Source: `{source.source_id}`",
        f"- Source type: `{source.source_type}`",
        f"- Requires game validation: `{str(source.requires_game_validation).lower()}`",
        "- Promotion status: not promoted; formal profile update requires an explicit future action.",
        "",
        "## Evidence Imported",
        "",
        f"- Evidence rows: {len(evidence)}",
        f"- Operators: {', '.join(sorted(aggregated))}",
        "",
        "## Proposed Candidate Changes",
        "",
        f"- Diff item count: {diff_count(diff)}",
        f"- Function changes: {len(diff['function_changes'])}",
        f"- Evidence additions: {len(diff['evidence_added'])}",
        f"- Confidence marker changes: {len(diff['confidence_changes'])}",
        "",
        "## Guardrails",
        "",
        "- This proposal does not modify `operator_function_profiles.json`.",
        "- This proposal does not modify V001 recruitment strategy.",
        "- This proposal does not claim the evidence is validated by real game runs.",
    ]
    return "\n".join(lines) + "\n"


def render_validation(
    source: KnowledgeSource,
    evidence: list[Any],
    aggregated: dict[str, Any],
    diff: dict[str, Any],
    formal_path: Path,
    candidate_path: Path,
) -> str:
    extracted_lines = []
    for item in evidence:
        extracted_lines.append(
            f"- {item.operator}: functions={list(item.functions)}, confidence={item.confidence}, "
            f"theme={item.theme}, source={item.source_id}"
        )

    aggregate_lines = []
    weights = load_json(LAB_ROOT / "data/source_weights.json")
    source_weight = EvidenceAggregator(weights, VersionRelevanceEvaluator(TARGET_THEME)).source_weight(source)
    for name, agg in sorted(aggregated.items()):
        aggregate_lines.append(
            f"- {name}: source_weight={source_weight:.3f}, theme_relevance={agg.theme_relevance:.2f}, "
            f"version_relevance={agg.version_relevance:.2f}, evidence_count={agg.evidence_count}, "
            f"functions={agg.functional_confidence}"
        )

    changed_ops = sorted(
        {
            *(row["operator"] for row in diff["function_changes"]),
            *(row["operator"] for row in diff["evidence_added"]),
            *(row["operator"] for row in diff["confidence_changes"]),
        }
    )

    lines = [
        "# Phase 4 Knowledge Pipeline Validation",
        "",
        "## Pipeline Run",
        "",
        "Path executed:",
        "`FileManualImportProvider -> KnowledgeExtractor -> EvidenceAggregator -> VersionRelevanceEvaluator -> candidate profile -> profile_diff.py`",
        "",
        f"- Raw source: `{source.source_id}`",
        f"- Source type: `{source.source_type}`",
        f"- Requires game validation: `{str(source.requires_game_validation).lower()}`",
        f"- Evidence imported: {len(evidence)}",
        f"- Operators recognized: {', '.join(sorted(aggregated))}",
        "",
        "## Extracted Evidence",
        "",
        *extracted_lines,
        "",
        "## Aggregation And Relevance",
        "",
        *aggregate_lines,
        "",
        "## Candidate Profile Result",
        "",
        f"- Formal profile: `{formal_path}`",
        f"- Candidate profile: `{candidate_path}`",
        "- Formal profile unchanged: yes",
        f"- Candidate changed operators: {', '.join(changed_ops)}",
        f"- Diff non-zero: {'yes' if diff_count(diff) > 0 else 'no'}",
        f"- Function changes: {len(diff['function_changes'])}",
        f"- Evidence additions: {len(diff['evidence_added'])}",
        f"- Confidence marker changes: {len(diff['confidence_changes'])}",
        "",
        "## Proposal Check",
        "",
        "- `roguelike-lab/analysis/KNOWLEDGE_UPDATE_PROPOSAL.md` generated: yes",
        "- Auto promote performed: no",
        "- V001 strategy modified: no",
        "- MaaCore modified: no",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    result = run_pipeline()
    print(
        json.dumps(
            {
                "evidence_count": len(result["evidence"]),
                "operator_count": len(result["aggregated"]),
                "diff_count": diff_count(result["diff"]),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
