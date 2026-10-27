# Support judgments and answer scoring

This page separates two activities: verifying which documentation pages support each tier-2 question (packaged here), and scoring the answers produced in the study (summarized here; the answers and scores themselves are in DocSpectra/DocSpectraICSC2027). All judges were language models. None of them is described as calibrated or independently validated, and none of their labels are human ground truth. The author's small spot-checks are listed at the end with their scope.

## Tier-2 support verification

### Pooling

Judging every page for every question was too expensive, so candidate pages were pooled per question. The pool is the union of (1) the top 20 pages from a lexical (BM25) passage search and the top 20 from an embedding passage search (`all-MiniLM-L6-v2`, revision `c9745ed1`), both queried with the reference answer over 12-line windows with a 6-line stride; (2) the top 10 pages of each of three fixed retrievers (lexical, embedding, graph expansion); and, for the per-version stages, (3) pages the answering agent read or cited. For each pooled page, the two best-matching windows from each generator were judged. Pooling followed RetrievalArena's `pooled_support_pool_v1` rule.

### Verifier

Each window was judged once by Claude Haiku 5.5 (`claude-haiku-5-5`, thinking disabled, low effort, 512 output tokens) with the prompt [`pooled_support_verifier.v1`](../protocol/support-verifier/pooled_support_verifier.v1.txt) and its [response schema](../protocol/support-verifier/pooled_support_verifier.v1.response-schema.json). The prompt's SHA-256, `df4424c1…`, was recomputed from RetrievalArena source at all three commits used. The verifier sees the question, the reference answer and one window, and returns:

- `answers`: the window states the answer or a necessary part of it. It must copy the shortest supporting span verbatim; a span that is not found in the window makes the judgment `span_invalid`, never a silent no.
- `not_answer`: the window is about something else or shares only topic words.
- `insufficient`: the window is cut off or ambiguous.

### From windows to pages

| Page decision | Rule | In qrels |
| --- | --- | --- |
| `supported` | at least one window judged `answers` with a valid span | relevance 1 |
| `not_supported` | every judged window is `not_answer` | relevance 0 |
| `undetermined` | otherwise (an `insufficient` or failed window) | absent |
| unjudged | the page was not in the question's pool | absent |

Undetermined and unjudged pages are different states, and neither is a rejection. A question enters a qrels file only if at least one page is `supported`.

### Stages

| Stage | Documentation | What changed | RetrievalArena commit |
| --- | --- | --- | --- |
| `c2-v2` | original (O) | full verification of the 142-question pool over the original corpus | `2f75016` |
| `pool-v3` | O, S, LT, R0 | pool completion: pages new to each version's pool were judged; earlier judgments at the same page bytes were reused | `60af29d` |
| `final-v4` | O, S, LT, R0 | whole-page re-judgment: each `undetermined` page was judged once on the whole page (input cap 400,000 bytes instead of 16,000) | `9e68b89` |

`final-v4` is the final support for each version; `pool-v3` defines the common-101 population. The re-judgment changed only pages that had been undetermined. After it, some pages remain undetermined (for the 111 freeze questions: O 39, S 40, LT 52, R0 33); the study scored them as misses and, in a sensitivity analysis, as hits.

Each stage directory under [`judgments/tier2/`](../judgments/tier2/) has `qrels.jsonl`, `page_decisions.jsonl` (every decision on this version's page bytes) and `supporting_spans.jsonl` (the verbatim span and one-sentence reason for each `answers` window of a supported page). RetrievalArena also carries forward decisions on earlier page bytes from the original version's pool; those rows are omitted from the page-decision files here, as from RetrievalArena's own qrels, and kept in the raw records archive. The archive `DockerDocsSet2026-1.0.0-support-verification-records.zip` has the raw judgments (with model responses), page decisions, qrels manifests, pools and window texts for every stage.

### Derived-page credit (O1)

The study also ran a sensitivity analysis, O1, that credits a refined page when it was derived from an original supported page: it survives, holds the moved content of a removed page, or shares at least one distinctive new content unit (30 characters or more, found in at most three original pages). O1 uses text overlap and makes no model call, so it is lexical provenance, not verification. Beyond identical pages it credits 1,075 LT pages and 36 R0 pages. [`credited-pages-in-top10.json`](../judgments/tier2/o1-derived-credit/credited-pages-in-top10.json) lists the derived-only credited pages that appeared in a retriever's top 10, with their direct decisions. Direct verification and O1 credit should not be mixed.

## Answer scoring in the study (summary)

| Measure | Judge | Configuration | Notes |
| --- | --- | --- | --- |
| Tier-1 task grades (primary) | `gpt-6-luna`, medium effort | answer-quality scorer prompt v2 (`53800547…`) and schema v2 (`f781faba…`); five 1–5 measures (correctness, fit, completeness, caveats, clarity); two passes with different blinding orders | Grades answers written by the same model. Its pilot ended `needs_revision` (ranking stability 11/20 cells against a 0.80 threshold); no human agreement was collected. |
| Tier-1 requirement judgments (secondary) | `qwen3:14b` via Ollama (digest `bdbd181c…`), temperature 0 | one verdict per core requirement: satisfied, missing, contradicted or uncertain; `satisfied` needs an exact answer span, scored under `quote_match_relaxed_v1` | One pass; 478 of 479 packets valid (one timeout kept as a failure). An earlier calibration on constructed answers admitted no judge. |
| Tier-2 RAGAS | `claude-haiku-5-5`, medium effort | FactualCorrectness (F1 mode) as the main number; Faithfulness and ContextRecall descriptive; one run per unit | In qualification, only FactualCorrectness passed the control checks; repeat checks on real units failed. |
| Tier-2 retrieval and navigation | none (deterministic) | ranked metrics against `final-v4` qrels with `ir-measures` 0.4.3 | |

The answering agent was `gpt-6-luna` at medium effort with a fixed operator prompt and tool budget; no model snapshot beyond the name was recorded. [`protocol/scoring.json`](../protocol/scoring.json) records the full configurations, hashes and image digests.

## Author spot-checks

| Check | Sample | Result | Scope |
| --- | --- | --- | --- |
| C2 verifier spot-check | 70 windows from the original version (35 verifier-yes, 35 verifier-no), one reviewer | precision 29/34 definite, misses 0/33 definite | windows, not whole pages; `c2-v2` only; the later stages were not spot-checked |
| Tier-1 requirement review | 75 proposed requirements | 63 accept, 10 revise, 2 reject | requirements, not answers or grades |
| Factual review of edited pages | 20 pages per refinement, blinded to arm | LT 20/20 and R0 20/20 no problem | reviewed after structural results were known |
| Lost-support check | 14 items where a question lost all verified support on a refined version | 3 still answer, 4 answer moved, 0 lost, 7 unsure; 7/14 agreement with the whole-page re-judgment | one item exposed the model verdict |
| Disputed derived pages | 16 pages credited by O1 but rejected by direct judgment, plus 4 controls | 4 of 16 answer, 3 partly, 9 do not | blind to verifier decision, not to arm |

A planned blinded review of tier-1 answer pairs was not carried out; no labels from it exist.
