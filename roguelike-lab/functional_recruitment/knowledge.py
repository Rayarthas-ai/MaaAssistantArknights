"""External knowledge learning prototypes for functional recruitment.

External inputs are treated as untrusted data. This module never executes
external content and never writes to the formal operator profile by itself.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Protocol


ALLOWED_FUNCTIONS = {
    "main_carry",
    "ground",
    "block",
    "healing",
    "sustain",
    "economy",
    "ranged",
    "anti_air",
    "burst",
    "control",
    "fast_redeploy",
    "bait",
    "summon",
    "utility",
    "emergency",
}


@dataclass(frozen=True)
class KnowledgeSource:
    source_id: str
    source_type: str
    title: str = ""
    author: str = ""
    url: str = ""
    collected_at: str | None = None
    published_at: str | None = None
    game_version: str | None = None
    maa_version_if_known: str | None = None
    roguelike_theme: str | None = None
    difficulty: str | None = None
    language: str | None = None
    credibility: str = "unknown"
    requires_game_validation: bool = False
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class OperatorRecommendationEvidence:
    operator: str
    theme: str
    difficulty: str | None
    recommendation_type: str
    functions: tuple[str, ...]
    hope_context: str | None
    priority_claim: str | None
    reason: str
    source_id: str
    confidence: float
    evidence_type: str


@dataclass(frozen=True)
class AggregatedOperatorEvidence:
    operator: str
    recommendation_confidence: float
    functional_confidence: dict[str, float]
    version_relevance: float
    theme_relevance: float
    evidence_count: int
    source_ids: tuple[str, ...]
    conflicts: tuple[str, ...] = ()


class ExternalKnowledgeProvider(Protocol):
    def discover(self) -> list[KnowledgeSource]:
        ...

    def load(self, source_id: str) -> str:
        ...


class MockKnowledgeProvider:
    def __init__(self, sources: Iterable[KnowledgeSource], payloads: Mapping[str, str]) -> None:
        self._sources = list(sources)
        self._payloads = dict(payloads)

    def discover(self) -> list[KnowledgeSource]:
        return list(self._sources)

    def load(self, source_id: str) -> str:
        return self._payloads[source_id]


class FileManualImportProvider:
    """Loads sanitized raw knowledge files from a local directory."""

    def __init__(self, raw_root: Path) -> None:
        self.raw_root = raw_root

    def discover(self) -> list[KnowledgeSource]:
        sources: list[KnowledgeSource] = []
        for metadata_path in self.raw_root.glob("*/metadata.json"):
            data = json.loads(metadata_path.read_text(encoding="utf-8"))
            if data.get("sanitized") is not True:
                continue
            sources.append(
                KnowledgeSource(
                    source_id=data["source_id"],
                    source_type=data.get("source_type", "manual_user_input"),
                    title=data.get("title", ""),
                    collected_at=data.get("collected_at"),
                    credibility=data.get("credibility", "unknown"),
                    requires_game_validation=bool(data.get("requires_game_validation", False)),
                    notes=tuple(data.get("notes", [])),
                )
            )
        for raw_path in self.raw_root.glob("*.json"):
            data = json.loads(raw_path.read_text(encoding="utf-8"))
            metadata = data.get("metadata", {})
            if metadata.get("sanitized") is not True:
                continue
            sources.append(
                KnowledgeSource(
                    source_id=metadata["source_id"],
                    source_type=metadata.get("source_type", "manual_user_input"),
                    title=metadata.get("title", ""),
                    author=metadata.get("author", ""),
                    url=str(raw_path),
                    collected_at=metadata.get("collected_at"),
                    published_at=metadata.get("published_at"),
                    game_version=metadata.get("game_version"),
                    maa_version_if_known=metadata.get("maa_version_if_known"),
                    roguelike_theme=metadata.get("roguelike_theme"),
                    difficulty=metadata.get("difficulty"),
                    language=metadata.get("language"),
                    credibility=metadata.get("credibility", "unknown"),
                    requires_game_validation=bool(metadata.get("requires_game_validation", False)),
                    notes=tuple(metadata.get("notes", [])),
                )
            )
        return sources

    def load(self, source_id: str) -> str:
        for raw_path in self.raw_root.glob("*.json"):
            data = json.loads(raw_path.read_text(encoding="utf-8"))
            metadata = data.get("metadata", {})
            if metadata.get("source_id") == source_id and metadata.get("sanitized") is True:
                return raw_path.read_text(encoding="utf-8")
        source_dir = self.raw_root / source_id
        candidates = [source_dir / "recommendations.json", source_dir / "summary.md"]
        for path in candidates:
            if path.exists():
                return path.read_text(encoding="utf-8")
        raise FileNotFoundError(source_id)


class KnowledgeExtractor:
    """Extracts stated recommendations; it does not judge correctness."""

    def extract_json(self, text: str, source_id: str) -> list[OperatorRecommendationEvidence]:
        data = json.loads(text)
        if isinstance(data, list):
            rows = data
        elif isinstance(data, dict):
            rows = data.get("recommendations", [])
        else:
            rows = []
        evidence: list[OperatorRecommendationEvidence] = []
        for row in rows:
            functions = tuple(fn for fn in row.get("functions", []) if fn in ALLOWED_FUNCTIONS)
            if not row.get("operator") or not functions:
                continue
            confidence = max(0.0, min(1.0, float(row.get("confidence", 0.0))))
            evidence.append(
                OperatorRecommendationEvidence(
                    operator=row["operator"],
                    theme=row.get("theme", ""),
                    difficulty=row.get("difficulty"),
                    recommendation_type=row.get("recommendation_type", "functional_pick"),
                    functions=functions,
                    hope_context=row.get("hope_context"),
                    priority_claim=row.get("priority_claim"),
                    reason=row.get("reason", ""),
                    source_id=row.get("source_id", source_id),
                    confidence=confidence,
                    evidence_type=row.get("evidence_type", "community_guide"),
                )
            )
        return evidence


class VersionRelevanceEvaluator:
    def __init__(self, target_theme: str, target_difficulty: str | None = None, target_game_version: str | None = None) -> None:
        self.target_theme = target_theme
        self.target_difficulty = target_difficulty
        self.target_game_version = target_game_version

    def theme_relevance(self, source: KnowledgeSource) -> float:
        if not source.roguelike_theme:
            return 0.7
        return 1.0 if source.roguelike_theme == self.target_theme else 0.35

    def difficulty_relevance(self, source: KnowledgeSource) -> float:
        if not self.target_difficulty or not source.difficulty:
            return 0.75
        return 1.0 if source.difficulty == self.target_difficulty else 0.6

    def version_relevance(self, source: KnowledgeSource) -> float:
        if not self.target_game_version or not source.game_version:
            return 0.7
        return 1.0 if source.game_version == self.target_game_version else 0.55


class EvidenceAggregator:
    def __init__(self, source_weights: Mapping[str, Any], relevance: VersionRelevanceEvaluator) -> None:
        self.source_weights = source_weights
        self.relevance = relevance

    def source_weight(self, source: KnowledgeSource) -> float:
        base = self.source_weights.get("source_type_weights", {}).get(source.source_type, self.source_weights.get("default_weight", 0.3))
        credibility = self.source_weights.get("credibility_multipliers", {}).get(source.credibility, 0.35)
        return float(base) * float(credibility)

    def aggregate(
        self,
        evidence: Iterable[OperatorRecommendationEvidence],
        sources: Mapping[str, KnowledgeSource],
    ) -> dict[str, AggregatedOperatorEvidence]:
        grouped: dict[str, list[OperatorRecommendationEvidence]] = {}
        for item in evidence:
            grouped.setdefault(item.operator, []).append(item)

        result: dict[str, AggregatedOperatorEvidence] = {}
        for operator, items in grouped.items():
            function_scores: dict[str, float] = {}
            total_weight = 0.0
            source_ids = []
            theme_relevance_values = []
            version_relevance_values = []
            conflicts = []
            for item in items:
                source = sources[item.source_id]
                source_ids.append(item.source_id)
                weight = self.source_weight(source) * item.confidence
                weight *= self.relevance.theme_relevance(source)
                weight *= self.relevance.difficulty_relevance(source)
                weight *= self.relevance.version_relevance(source)
                total_weight += weight
                theme_relevance_values.append(self.relevance.theme_relevance(source))
                version_relevance_values.append(self.relevance.version_relevance(source))
                for fn in item.functions:
                    function_scores[fn] = function_scores.get(fn, 0.0) + weight
            if len({tuple(item.functions) for item in items}) > 1 and len(items) > 1:
                conflicts.append("sources differ on functional tags")
            normalized = {fn: min(1.0, value) for fn, value in function_scores.items()}
            result[operator] = AggregatedOperatorEvidence(
                operator=operator,
                recommendation_confidence=min(1.0, total_weight),
                functional_confidence=normalized,
                version_relevance=sum(version_relevance_values) / len(version_relevance_values) if version_relevance_values else 0.0,
                theme_relevance=sum(theme_relevance_values) / len(theme_relevance_values) if theme_relevance_values else 0.0,
                evidence_count=len(items),
                source_ids=tuple(sorted(set(source_ids))),
                conflicts=tuple(conflicts),
            )
        return result


def build_candidate_profile_patch(
    formal_profiles: Mapping[str, Any],
    aggregated: Mapping[str, AggregatedOperatorEvidence],
) -> dict[str, Any]:
    candidate: dict[str, Any] = {}
    for name, agg in aggregated.items():
        current = dict(formal_profiles.get(name, {}))
        functions = dict(current.get("functions", {}))
        for fn, confidence in agg.functional_confidence.items():
            functions[fn] = max(float(functions.get(fn, 0.0)), round(confidence, 3))
        current["functions"] = functions
        current["confidence"] = "candidate"
        evidence = list(current.get("evidence", []))
        evidence.append(
            {
                "type": "external_aggregated",
                "source_ids": list(agg.source_ids),
                "recommendation_confidence": agg.recommendation_confidence,
                "conflicts": list(agg.conflicts),
            }
        )
        current["evidence"] = evidence
        candidate[name] = current
    return candidate
