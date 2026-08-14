from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = LAB_ROOT.parent
sys.path.insert(0, str(LAB_ROOT))

from functional_recruitment.knowledge import (  # noqa: E402
    EvidenceAggregator,
    FileManualImportProvider,
    KnowledgeExtractor,
    KnowledgeSource,
    MockKnowledgeProvider,
    VersionRelevanceEvaluator,
    build_candidate_profile_patch,
)
from tools.profile_diff import diff_profiles  # noqa: E402
from tools.run_external_knowledge_pipeline import run_pipeline  # noqa: E402


class Phase4ExternalKnowledgeTests(unittest.TestCase):
    def test_extractor_sanitizes_functions_and_confidence(self) -> None:
        payload = json.dumps(
            {
                "recommendations": [
                    {
                        "operator": "古米",
                        "theme": "JieGarden",
                        "difficulty": "N15",
                        "recommendation_type": "functional_pick",
                        "functions": ["ground", "block", "bad_function"],
                        "hope_context": "zero_hope",
                        "priority_claim": "high",
                        "reason": "covers multiple gaps",
                        "source_id": "guide-a",
                        "confidence": 2.0,
                        "evidence_type": "community_guide",
                    }
                ]
            },
            ensure_ascii=False,
        )
        extracted = KnowledgeExtractor().extract_json(payload, "guide-a")
        self.assertEqual(len(extracted), 1)
        self.assertEqual(extracted[0].functions, ("ground", "block"))
        self.assertEqual(extracted[0].confidence, 1.0)

    def test_aggregator_uses_source_weight_and_relevance(self) -> None:
        source = KnowledgeSource(
            source_id="guide-a",
            source_type="written_guide",
            roguelike_theme="JieGarden",
            difficulty="N15",
            credibility="high",
        )
        payload = json.dumps(
            [
                {
                    "operator": "古米",
                    "theme": "JieGarden",
                    "difficulty": "N15",
                    "recommendation_type": "functional_pick",
                    "functions": ["ground", "healing"],
                    "source_id": "guide-a",
                    "confidence": 0.8,
                    "evidence_type": "community_guide",
                }
            ],
            ensure_ascii=False,
        )
        evidence = KnowledgeExtractor().extract_json(payload, "guide-a")
        weights = json.loads((REPO_ROOT / "roguelike-lab/data/source_weights.json").read_text(encoding="utf-8"))
        agg = EvidenceAggregator(weights, VersionRelevanceEvaluator("JieGarden", "N15")).aggregate(
            evidence,
            {"guide-a": source},
        )
        self.assertIn("古米", agg)
        self.assertGreater(agg["古米"].recommendation_confidence, 0)
        self.assertEqual(agg["古米"].theme_relevance, 1.0)

    def test_candidate_patch_does_not_modify_formal_profile(self) -> None:
        formal = json.loads((REPO_ROOT / "roguelike-lab/data/operator_function_profiles.json").read_text(encoding="utf-8"))
        source = KnowledgeSource(source_id="game-test-a", source_type="game_test", roguelike_theme="JieGarden", credibility="high")
        evidence = KnowledgeExtractor().extract_json(
            json.dumps(
                [
                    {
                        "operator": "古米",
                        "theme": "JieGarden",
                        "recommendation_type": "functional_pick",
                        "functions": ["healing"],
                        "source_id": "game-test-a",
                        "confidence": 0.9,
                        "evidence_type": "game_test",
                    }
                ],
                ensure_ascii=False,
            ),
            "game-test-a",
        )
        weights = json.loads((REPO_ROOT / "roguelike-lab/data/source_weights.json").read_text(encoding="utf-8"))
        agg = EvidenceAggregator(weights, VersionRelevanceEvaluator("JieGarden")).aggregate(evidence, {"game-test-a": source})
        patch = build_candidate_profile_patch(formal, agg)
        self.assertIn("古米", patch)
        self.assertEqual(formal["古米"]["confidence"], "medium")
        self.assertEqual(patch["古米"]["confidence"], "candidate")

    def test_profile_diff_reports_candidate_changes(self) -> None:
        base = {"古米": {"functions": {"ground": 0.6}, "confidence": "medium", "evidence": []}}
        candidate = {
            "古米": {
                "functions": {"ground": 0.6, "healing": 0.8},
                "confidence": "candidate",
                "evidence": [{"type": "external_aggregated"}],
            },
            "清流": {"functions": {"healing": 0.8}},
        }
        diff = diff_profiles(base, candidate)
        self.assertEqual(diff["operators_added"], ["清流"])
        self.assertEqual(len(diff["function_changes"]), 1)
        self.assertEqual(len(diff["evidence_added"]), 1)

    def test_providers_are_data_only(self) -> None:
        source = KnowledgeSource(source_id="mock", source_type="manual_user_input")
        provider = MockKnowledgeProvider([source], {"mock": "{\"recommendations\": []}"})
        self.assertEqual(provider.discover()[0].source_id, "mock")
        self.assertEqual(provider.load("mock"), "{\"recommendations\": []}")

        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / "manual"
            raw.mkdir()
            (raw / "metadata.json").write_text(
                json.dumps({"source_id": "manual", "source_type": "manual_user_input", "sanitized": True}),
                encoding="utf-8",
            )
            (raw / "summary.md").write_text("data only", encoding="utf-8")
            file_provider = FileManualImportProvider(Path(tmp))
            self.assertEqual(file_provider.discover()[0].source_id, "manual")
            self.assertEqual(file_provider.load("manual"), "data only")


    def test_file_provider_reads_standalone_seed_fixture(self) -> None:
        provider = FileManualImportProvider(REPO_ROOT / "roguelike-lab/knowledge/raw")
        sources = {source.source_id: source for source in provider.discover()}
        self.assertIn("phase4-seed-evidence-manual-001", sources)
        source = sources["phase4-seed-evidence-manual-001"]
        self.assertEqual(source.source_type, "manual_user_input")
        self.assertTrue(source.requires_game_validation)

    def test_real_pipeline_changes_candidate_without_formal_promote(self) -> None:
        formal_path = REPO_ROOT / "roguelike-lab/data/operator_function_profiles.json"
        before = formal_path.read_text(encoding="utf-8")
        result = run_pipeline()
        after = formal_path.read_text(encoding="utf-8")
        self.assertEqual(before, after)
        self.assertGreater(sum(len(value) for value in result["diff"].values() if isinstance(value, list)), 0)
        candidate = json.loads(
            (REPO_ROOT / "roguelike-lab/data/operator_function_profiles_candidate.json").read_text(encoding="utf-8")
        )
        self.assertFalse(candidate["metadata"]["promoted"])
        self.assertTrue(candidate["metadata"]["requires_explicit_promote"])

    def test_same_operator_multi_source_evidence_aggregates(self) -> None:
        weights = json.loads((REPO_ROOT / "roguelike-lab/data/source_weights.json").read_text(encoding="utf-8"))
        sources = {
            "a": KnowledgeSource(source_id="a", source_type="manual_user_input", roguelike_theme="JieGarden", credibility="medium"),
            "b": KnowledgeSource(source_id="b", source_type="written_guide", roguelike_theme="JieGarden", credibility="high"),
        }
        payload = json.dumps(
            [
                {"operator": "??", "theme": "JieGarden", "functions": ["healing"], "source_id": "a", "confidence": 0.4},
                {"operator": "??", "theme": "JieGarden", "functions": ["healing"], "source_id": "b", "confidence": 0.4},
            ],
            ensure_ascii=False,
        )
        evidence = KnowledgeExtractor().extract_json(payload, "a")
        agg = EvidenceAggregator(weights, VersionRelevanceEvaluator("JieGarden")).aggregate(evidence, sources)
        self.assertEqual(agg["??"].evidence_count, 2)
        self.assertEqual(agg["??"].source_ids, ("a", "b"))
        self.assertGreater(agg["??"].functional_confidence["healing"], 0.1)

    def test_conflicting_evidence_is_recorded_not_auto_overwritten(self) -> None:
        weights = json.loads((REPO_ROOT / "roguelike-lab/data/source_weights.json").read_text(encoding="utf-8"))
        sources = {
            "a": KnowledgeSource(source_id="a", source_type="manual_user_input", roguelike_theme="JieGarden", credibility="medium"),
            "b": KnowledgeSource(source_id="b", source_type="manual_user_input", roguelike_theme="JieGarden", credibility="medium"),
        }
        payload = json.dumps(
            [
                {"operator": "?", "theme": "JieGarden", "functions": ["anti_air"], "source_id": "a", "confidence": 0.5},
                {"operator": "?", "theme": "JieGarden", "functions": ["control"], "source_id": "b", "confidence": 0.5},
            ],
            ensure_ascii=False,
        )
        evidence = KnowledgeExtractor().extract_json(payload, "a")
        agg = EvidenceAggregator(weights, VersionRelevanceEvaluator("JieGarden")).aggregate(evidence, sources)
        self.assertIn("sources differ on functional tags", agg["?"].conflicts)

    def test_stale_and_different_theme_evidence_are_downweighted(self) -> None:
        weights = json.loads((REPO_ROOT / "roguelike-lab/data/source_weights.json").read_text(encoding="utf-8"))
        fresh = KnowledgeSource(source_id="fresh", source_type="written_guide", roguelike_theme="JieGarden", game_version="v2", credibility="high")
        stale = KnowledgeSource(source_id="stale", source_type="written_guide", roguelike_theme="JieGarden", game_version="v1", credibility="high")
        off_theme = KnowledgeSource(source_id="off-theme", source_type="written_guide", roguelike_theme="Sami", game_version="v2", credibility="high")
        item = {"operator": "??", "theme": "JieGarden", "functions": ["healing"], "confidence": 0.8}
        fresh_ev = KnowledgeExtractor().extract_json(json.dumps([{**item, "source_id": "fresh"}], ensure_ascii=False), "fresh")
        stale_ev = KnowledgeExtractor().extract_json(json.dumps([{**item, "source_id": "stale"}], ensure_ascii=False), "stale")
        off_ev = KnowledgeExtractor().extract_json(json.dumps([{**item, "source_id": "off-theme"}], ensure_ascii=False), "off-theme")
        evaluator = VersionRelevanceEvaluator("JieGarden", target_game_version="v2")
        fresh_score = EvidenceAggregator(weights, evaluator).aggregate(fresh_ev, {"fresh": fresh})["??"].recommendation_confidence
        stale_score = EvidenceAggregator(weights, evaluator).aggregate(stale_ev, {"stale": stale})["??"].recommendation_confidence
        off_score = EvidenceAggregator(weights, evaluator).aggregate(off_ev, {"off-theme": off_theme})["??"].recommendation_confidence
        self.assertLess(stale_score, fresh_score)
        self.assertLess(off_score, fresh_score)


if __name__ == "__main__":
    unittest.main()
