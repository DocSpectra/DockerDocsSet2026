# File formats

All JSON Lines files are UTF-8 with one object per line. CSV files are convenience views of the JSON Lines files with the same IDs; nested fields are JSON-encoded. Paths inside the package are POSIX and relative.

## Questions (schema version 1)

| File | Fields | Kind |
| --- | --- | --- |
| `questions/tier1/tasks.jsonl` | `task_id`, `question` | question only |
| `questions/tier1/requirements.jsonl` | `requirement_id` (`<first 12 hex of task_id>-<element_id>`), `task_id`, `element_id`, `requirement`, `acceptance`, `page` {`doc_id`, `rel_path`, `upstream_url`, `sha256`}, `support` [{`doc_id`, `rel_path`, `upstream_url`, `quote`, `quote_sha256`, `origin`}], `author_review` {`decision`, `note`} | labels |
| `questions/tier1/provenance.jsonl` | `task_id`, `origin`, `survey_area_id`, `support_pages`, generator model and effort, prompt/schema/response SHA-256, `generation_record`, `elements_removed_in_review` | provenance |
| `questions/tier2/questions.jsonl` | `question_id`, `question` (the extracted file, byte for byte) | question only |
| `questions/tier2/reference_answers.jsonl` | `question_id`, `answer` (the extracted file, byte for byte) | labels |
| `questions/tier2/sources.jsonl` | `question_id`, `source_path`, `source_doc_id`, `source_file_sha256`, `heading_markdown`, `heading_level`, `source_line`, `upstream_url` (with `#L<line>`), `rendered_anchor_approx`, `extraction_rule`, `question_sha256`, `answer_sha256` | provenance |
| `questions/tier2/populations.jsonl` | `question_id`, `historical_support_label`, `in_candidate_pool_142`, `in_freeze_111`, `in_common_105`, `in_common_101`, `exclusion_reason`, `common_105_exclusion`, `common_101_exclusion`, `duplicate_text_group`, `c2_v2_page_decisions`, `supported_pages_pool_v3`, `supported_pages_final_v4` | derived from labels |
| `questions/tier2/duplicate_text_groups.json` | `rule`, `groups` [{`question_ids`, `in_freeze_111`, `source_paths`}] | metadata |

`task_id` is a 64-hex identifier assigned at generation. `question_id` is the sequential extraction ID.

## Judgments

| File | Fields |
| --- | --- |
| `judgments/tier2/<stage>/<arm>/qrels.jsonl` | `question_id`, `doc_id`, `relevance` (1 supported, 0 not supported), `judgment_id` |
| `judgments/tier2/<stage>/<arm>/page_decisions.jsonl` | `question_id`, `doc_id`, `decision` (`supported`, `not_supported`, `undetermined`), `page_sha256` (SHA-256 of the exported page), `pool_sources` (pool member and rank source counts), `windows_judged`, `answering_windows` |
| `judgments/tier2/<stage>/<arm>/supporting_spans.jsonl` | `question_id`, `doc_id`, `window_id` (`<doc_id>#L<start>-<end>`, or `#page` for whole-page judgments), `supporting_span`, `reason`, `model`, `prompt_sha256` |
| `judgments/tier2/historical-automatic/` | the archived lexical audit (`faq_support_audit.jsonl`) and its top-5 candidate pages (`top5_candidates.json`); not support judgments |
| `judgments/tier2/o1-derived-credit/` | the derived-page credit record described in [judging](judging.md) |

`<stage>` is `c2-v2`, `pool-v3` or `final-v4`; `<arm>` is `O`, `S`, `LT` or `R0`. O and S use `docs-original`, LT uses `docs-lt` and R0 uses `docs-r0`. A `doc_id` in a judgment is a page of that branch's export, and `page_sha256` equals the SHA-256 of `export/corpus/<doc_id>.md` on that branch.

## Manifests

| File | Contents |
| --- | --- |
| `manifests/package.json` | version, upstream pin, population sizes, judgment stage index (`judgments.tier2_qrels`), release assets with SHA-256, related repositories and code pins |
| `manifests/variants.json` | per branch: packaging commit, documentation and export identities, study variant IDs, status counts |
| `manifests/pages-<branch>.jsonl` | `variant`, `rel_path`, `doc_id`, `sha256`, `status` (`unchanged`, `modified`, `added`), `export_file`, `export_sha256`, `upstream_path`/`upstream_url` (unchanged), `derived_from_path`/`derived_from_url`/`derived_from_sha256` (modified), `moved_content` |
| `manifests/changes-<branch>.csv` | modified and added files of a refinement with their original upstream link |
| `manifests/checksums.sha256` | SHA-256 of every other file on `main` |

## Protocol

| File | Contents |
| --- | --- |
| `protocol/refinement/areas.jsonl` | per area: label, survey rationale, source paths, original pages, and per arm the sessions and final admission |
| `protocol/refinement/sessions.jsonl` | per editing session: arm, area, kind, times, start and terminal trees, recorded and final action, reasons, fixes in force, editor identity, C pin, prompt and receipts |
| `protocol/refinement/receipts/<session>/` | admission (`c-admission.json`) and mapping (`mapping.json`) receipts |
| `protocol/refinement/prompts/` | base editor prompts, the area-selection prompt and every composed session prompt |
| `protocol/refinement/run-history.json` | fixes, the incoming-link exemption, reconciliation, exclusion sensitivity and editor runtime |
| `protocol/tier1-generation/` | generation prompt template, response schema and each call's submitted prompt and response |
| `protocol/support-verifier/` | the support verifier prompt text and response schema |
| `protocol/scoring.json` | answering and scoring configurations summarized in [judging](judging.md) |
