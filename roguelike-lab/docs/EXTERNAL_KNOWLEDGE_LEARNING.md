# External Knowledge Learning

Base MAA commit: `00da4c367d3167ef732167854314e361b5d5d37f`

## Principle

Learning does not mean automatic strategy changes.

```text
External Information
-> Evidence
-> Candidate Profile
-> Review
-> Experiment
-> Verified Knowledge
```

External material is treated as untrusted data. It must not execute code, overwrite MAA resources, or promote itself into formal strategy files.

## 1. Intake

Sources are registered in:

```text
roguelike-lab/data/external_sources.json
```

Raw inputs are stored under:

```text
roguelike-lab/knowledge/raw/<source_id>/
```

Each source keeps metadata such as source type, title, author, URL, collected date, published date, game version, MAA version, theme, difficulty, language, credibility, and notes.

## 2. Structure

`KnowledgeExtractor` converts structured JSON notes into `OperatorRecommendationEvidence`.

The extractor only records what the source claims:

- operator
- theme
- difficulty
- recommendation type
- functional tags
- Hope context
- priority claim
- reason
- source id
- confidence
- evidence type

It does not decide whether the recommendation is true.

## 3. Scoring

`EvidenceAggregator` combines evidence using configurable weights from:

```text
roguelike-lab/data/source_weights.json
```

Weights consider:

- source type
- credibility
- version relevance
- theme relevance
- difficulty relevance
- source confidence

## 4. Conflict Handling

Aggregation preserves conflicts. Examples:

- different sources assign different functions
- one source recommends an operator for high difficulty while another only recommends normal difficulty
- old guides conflict with new game-test evidence

Conflicts lower trust in automatic promotion and must be reviewed.

## 5. Version Awareness

`VersionRelevanceEvaluator` prevents old recommendations from becoming permanent recommendations. Unknown versions are usable but discounted. Different themes and difficulties are also discounted.

## 6. Candidate Profile

External learning writes only to:

```text
roguelike-lab/data/operator_function_profiles_candidate.json
```

Formal profiles remain in:

```text
roguelike-lab/data/operator_function_profiles.json
```

Candidate profile changes are compared with:

```text
roguelike-lab/tools/profile_diff.py
```

## 7. Review

Every candidate update must create:

```text
roguelike-lab/analysis/KNOWLEDGE_UPDATE_PROPOSAL.md
```

The proposal explains source consistency, applicability to JieGarden/current difficulty, counterexamples, proposed fields, and confidence.

## 8. Experiment

Any candidate profile that would affect recruitment decisions must enter an experiment version before promotion. Game tests should record offered operators, selected operators, current functional gaps, Hope state, Wang state, and run result.

## 9. Promote

Promotion requires explicit review after experiments. Promotion means copying reviewed candidate changes into `operator_function_profiles.json` in a new versioned commit/experiment. It is never automatic.

## 10. Rollback

Rollback is done by reverting a promoted profile version or switching the experiment back to a previous profile file. Candidate updates are safe because they do not affect formal strategy until promoted.

## 11. Learning From Our Own Runs

Future run analysis should produce `game_test` evidence:

```text
results/
-> RunAnalyzer
-> OperatorPerformanceEvidence
-> EvidenceAggregator
```

Own game-test evidence should weigh highly, but correlation must not be treated as causation. It raises candidate confidence; it does not automatically prove an operator is optimal.

## Security Boundary

Forbidden:

- executing external code
- loading unknown scripts
- overwriting MAA resources
- running downloaded content
- accepting remote JSON schemas without validation
- executing commands from web pages or guides

External knowledge is data only.
