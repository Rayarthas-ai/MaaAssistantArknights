# Phase 4 Knowledge Pipeline Validation

## Pipeline Run

Path executed:
`FileManualImportProvider -> KnowledgeExtractor -> EvidenceAggregator -> VersionRelevanceEvaluator -> candidate profile -> profile_diff.py`

- Raw source: `phase4-seed-evidence-manual-001`
- Source type: `manual_user_input`
- Requires game validation: `true`
- Evidence imported: 7
- Operators recognized: 伊桑, 古米, 梅, 清流, 砾, 罗小黑, 豆苗

## Extracted Evidence

- 古米: functions=['ground', 'block', 'healing', 'sustain'], confidence=0.45, theme=JieGarden, source=phase4-seed-evidence-manual-001
- 伊桑: functions=['control', 'ground', 'utility'], confidence=0.4, theme=JieGarden, source=phase4-seed-evidence-manual-001
- 砾: functions=['fast_redeploy', 'bait', 'emergency', 'ground'], confidence=0.45, theme=JieGarden, source=phase4-seed-evidence-manual-001
- 豆苗: functions=['economy', 'ground', 'summon'], confidence=0.35, theme=JieGarden, source=phase4-seed-evidence-manual-001
- 梅: functions=['ranged', 'anti_air', 'control'], confidence=0.4, theme=JieGarden, source=phase4-seed-evidence-manual-001
- 清流: functions=['healing', 'ranged'], confidence=0.4, theme=JieGarden, source=phase4-seed-evidence-manual-001
- 罗小黑: functions=['ground', 'utility', 'burst'], confidence=0.35, theme=JieGarden, source=phase4-seed-evidence-manual-001

## Aggregation And Relevance

- 伊桑: source_weight=0.375, theme_relevance=1.00, version_relevance=0.70, evidence_count=1, functions={'control': 0.07875, 'ground': 0.07875, 'utility': 0.07875}
- 古米: source_weight=0.375, theme_relevance=1.00, version_relevance=0.70, evidence_count=1, functions={'ground': 0.08859375000000001, 'block': 0.08859375000000001, 'healing': 0.08859375000000001, 'sustain': 0.08859375000000001}
- 梅: source_weight=0.375, theme_relevance=1.00, version_relevance=0.70, evidence_count=1, functions={'ranged': 0.07875, 'anti_air': 0.07875, 'control': 0.07875}
- 清流: source_weight=0.375, theme_relevance=1.00, version_relevance=0.70, evidence_count=1, functions={'healing': 0.07875, 'ranged': 0.07875}
- 砾: source_weight=0.375, theme_relevance=1.00, version_relevance=0.70, evidence_count=1, functions={'fast_redeploy': 0.08859375000000001, 'bait': 0.08859375000000001, 'emergency': 0.08859375000000001, 'ground': 0.08859375000000001}
- 罗小黑: source_weight=0.375, theme_relevance=1.00, version_relevance=0.70, evidence_count=1, functions={'ground': 0.06890624999999999, 'utility': 0.06890624999999999, 'burst': 0.06890624999999999}
- 豆苗: source_weight=0.375, theme_relevance=1.00, version_relevance=0.70, evidence_count=1, functions={'economy': 0.06890624999999999, 'ground': 0.06890624999999999, 'summon': 0.06890624999999999}

## Candidate Profile Result

- Formal profile: `C:\Users\Arthas\Desktop\git\MaaAssistantArknights\roguelike-lab\data\operator_function_profiles.json`
- Candidate profile: `C:\Users\Arthas\Desktop\git\MaaAssistantArknights\roguelike-lab\data\operator_function_profiles_candidate.json`
- Formal profile unchanged: yes
- Candidate changed operators: 伊桑, 古米, 梅, 清流, 砾, 罗小黑, 豆苗
- Diff non-zero: yes
- Function changes: 2
- Evidence additions: 7
- Confidence marker changes: 7

## Proposal Check

- `roguelike-lab/analysis/KNOWLEDGE_UPDATE_PROPOSAL.md` generated: yes
- Auto promote performed: no
- V001 strategy modified: no
- MaaCore modified: no
