# DockerDocsSet2026

DockerDocsSet2026 contains the Docker documentation, experimental refinements of it, and the question sets and support judgments used for the Docker application in the ICSC 2027 submission *Measuring Directed Documentation Structure with Normalized Magnetic Spectra* (Rocker D'Antonio, Mississippi State University). It lets others inspect the documentation versions the study compared, reuse the questions with or without labels, and check every packaged file against its recorded identity.

The source is [Docker documentation (docker/docs)](https://github.com/docker/docs) at commit [`274681c49355bd951ae60c9208e854ff70f12474`](https://github.com/docker/docs/tree/274681c49355bd951ae60c9208e854ff70f12474) (May 1, 2026). DockerDocsSet2026 is not a Docker, Inc. release.

## What you receive

| Asset | Where | Contents |
| --- | --- | --- |
| Original documentation | branch [`docs-original`](https://github.com/DocSpectra/DockerDocsSet2026/tree/docs-original) | 1,218 pages of the experiment corpus, byte-identical to docker/docs; the retrieval export and link graph; the 1,487-file upstream page snapshot; the earlier 1,263-page export |
| LT refinement (experimental) | branch [`docs-lt`](https://github.com/DocSpectra/DockerDocsSet2026/tree/docs-lt) | 1,823 pages (773 modified, 605 added); export with 5,203 links |
| R0 refinement (experimental) | branch [`docs-r0`](https://github.com/DocSpectra/DockerDocsSet2026/tree/docs-r0) | 1,229 pages (1,006 modified, 11 added); export with 4,502 links |
| Tier-1 tasks | [`questions/tier1/`](questions/tier1/) | 15 complex tasks; 73 core requirements with acceptance criteria and supporting quotations |
| Tier-2 questions | [`questions/tier2/`](questions/tier2/) | 144 FAQ questions with reference answers, source headings and the 142/111/105/101 populations |
| Support judgments | [`judgments/tier2/`](judgments/tier2/) | LLM-verified page support for each documentation version and stage, with supporting spans |
| Protocol records | [`protocol/`](protocol/) | editor and generator prompts, area and session tables, admission receipts, verifier prompt |
| Manifests | [`manifests/`](manifests/) | branch identities, per-page lineage and upstream links, change lists, checksums |
| Tools | [`tools/`](tools/) | `verify.py` (offline checks) and `load.py` (loaders); standard-library Python only |

The two refinements, LT (leaf-and-trunk) and R0 (uninformed), were produced by an automated editing agent during the study. They are experimental variants: their inclusion does not imply that they improve the documentation.

## Download options

- **Clone everything:** `git clone https://github.com/DocSpectra/DockerDocsSet2026.git`, then `git switch docs-lt` (or another branch). Line-ending conversion is disabled in `.gitattributes`, so checked-out files keep their recorded bytes. On Windows, some paths exceed 260 characters; clone with `git clone -c core.longpaths=true …`.
- **Questions only:** `questions/tier1/tasks.jsonl` and `questions/tier2/questions.jsonl` hold question text alone. They are also packaged with no labels as the release archive `DockerDocsSet2026-1.0.0-questions-only.zip`.
- **Release archives** for version 1.0.0: one zip per documentation branch, a questions-and-labels zip, a questions-only zip, the raw support-verification records, and a Git bundle of all branches. [`manifests/package.json`](manifests/package.json) lists their SHA-256 values.

## Loading

```python
import sys
sys.path.insert(0, "tools")
import load

tasks = load.load_questions(".", tier=1)                          # 15 tasks: task_id, question
questions = load.load_questions(".", tier=2, population="in_common_105")
answers = load.load_reference_answers(".")                        # labels: load separately
qrels = load.load_qrels(".", arm="LT", stage="final-v4")          # support judgments for docs-lt
```

The question loaders read only the question files, so a question-only pipeline cannot pick up answers or judgments by accident. [`docs/schema.md`](docs/schema.md) describes every file.

## How the data were made

- **Scope and extraction.** The historical exporter read every `.md`, `.html` and `.txt` page of the pinned commit, skipped underscore-prefixed directories, and set aside the 26 FAQ pages as the question source. The experiment corpus (`docs_scope_v1`) then removed 45 agent-instruction and site-build files, leaving 1,218 pages. Document IDs come from the repository-relative path. See [`docs/provenance.md`](docs/provenance.md).
- **Refinements.** The documentation was divided into 25 areas. For each arm, an editing agent made one pass per area under a structural admission check, followed by one reconciliation pass over the whole corpus. LT ended with 18 admitted areas and R0 with 23. See [`docs/refinement.md`](docs/refinement.md).
- **Questions.** The tier-2 questions are the 144 question headings of Docker's FAQ pages, with the text beneath each heading as its reference answer; they were extracted, not generated. The tier-1 tasks were generated by a language model from exact page excerpts and reviewed requirement by requirement by the author. See [`docs/questions.md`](docs/questions.md).
- **Judgments.** Claude Haiku 5.5 checked pooled candidate passages against each tier-2 reference answer, separately for each documentation version. These are LLM judgments, not human relevance labels; small author spot-checks are summarized with them. See [`docs/judging.md`](docs/judging.md).

## Checking the package

```bash
python tools/verify.py
```

The verifier needs no network access, credentials or other repositories. It checks every file on `main` against `manifests/checksums.sha256`, recomputes the documentation and export identities of each branch from Git objects, and joins every question, requirement and judgment to its documentation version. Add `--archives DIR` to also check downloaded release archives. [`docs/reproduction.md`](docs/reproduction.md) explains how the package relates to the study code.

## Related repositories and the paper

- [DocSpectra/RetrievalArena](https://github.com/DocSpectra/RetrievalArena) is the reusable evaluation framework. Its pooling, verification and scoring components produced the support judgments; the commits used are listed in [`docs/reproduction.md`](docs/reproduction.md).
- [DocSpectra/DocSpectraICSC2027](https://github.com/DocSpectra/DocSpectraICSC2027) holds the study's drivers, configurations, evidence records and analysis code.
- The paper is prepared for ICSC 2027 and has not been published. [`docs/paper.md`](docs/paper.md) gives its title, author, status and relationship to this package; a public manuscript link is not yet available.

## License and attribution

The documentation in the `docs-*` branches is Docker documentation, "Copyright 2013-2026 Docker, Inc., released under the Apache 2.0 license"; each branch carries Docker's `LICENSE`, and the refinement branches carry a modification notice. Terms for the package's own material are in [`LICENSES.md`](LICENSES.md).

## Citation

Cite the dataset with [`CITATION.cff`](CITATION.cff) or the BibTeX in [`CITATION.bib`](CITATION.bib), and cite Docker's documentation and the paper separately:

```bibtex
@misc{dockerdocsset2026,
  author       = {D'Antonio, Rocker},
  title        = {{DockerDocsSet2026}: Docker Documentation Variants, Question Sets and Support Judgments},
  year         = {2026},
  howpublished = {Dataset, GitHub repository},
  url          = {https://github.com/DocSpectra/DockerDocsSet2026},
  note         = {Version 1.0.0. Derived from Docker documentation (docker/docs), commit 274681c49355bd951ae60c9208e854ff70f12474}
}
```
