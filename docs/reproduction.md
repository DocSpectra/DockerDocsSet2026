# Verification and reproduction

## Verify the package offline

From a clone with `main` checked out (Python 3.9 or later, standard library only):

```bash
python tools/verify.py
python tools/verify.py --archives path/to/downloaded/assets
```

The verifier makes no network calls and needs no credentials, model or other repository. It checks:

1. every file on `main` against `manifests/checksums.sha256`, and that no file contains an absolute workstation path;
2. question, requirement and judgment joins: unique IDs, question files holding only question text, the 144/142/111/105/101 tier-2 populations and the 15/73 tier-1 counts, exclusion reasons, and every judged page present in its documentation version;
3. for each `docs-*` branch, read directly from Git objects: the packaging commit, the documentation tree identity, the export corpus identity, the graph file hash, the upstream snapshot and historical export identities on `docs-original`, and that `manifests/pages-<branch>.jsonl` matches every documentation file;
4. with `--archives`, the SHA-256 of each release archive and the tree identities inside it.

Link construction and provenance are checked offline. Whether the upstream URLs currently resolve is a live check the verifier does not perform.

## Rebuild the package

The package was built by `docker_docs_set_26.py` in [DocSpectra/DocSpectraICSC2027](https://github.com/DocSpectra/DocSpectraICSC2027) from the study's frozen artifacts, with no model calls. The builder checks each input against its recorded SHA-256 or tree identity, recomputes the question populations from the frozen judgments, and refuses to overwrite an existing build. Packaging commits use a fixed author and date, so the same inputs give the same branch commits.

## Code and data pins

| Component | Pin |
| --- | --- |
| Upstream documentation | docker/docs `274681c49355bd951ae60c9208e854ff70f12474` |
| Historical exporter (page discovery, document IDs, FAQ extraction, links) | `retrieval_arena_export.py` SHA-256 `1a0f16ae…`; graph code SHA-256 `a6233064…` |
| Embedding model for pooling | `sentence-transformers/all-MiniLM-L6-v2` revision `c9745ed1d9f207416be6d2e6f8de32d1f16199bf` |
| RetrievalArena, C2 pooling and verification | `2f75016924353eabc4b194fc69a6eaca310cb239` |
| RetrievalArena, per-version pooling, verification, RAGAS and ranked scoring | `60af29d31bbb8127cea57a017cad27255f8d89af` |
| RetrievalArena, whole-page re-judgment | `9e68b89721d9b8e9fcd8f5126d5091da7ccd1d56` |
| RetrievalArena, admission check used during editing | `eea1e368a8004021da0f2ffafdb6cdf37b6727dc` |
| Editor runtime | Codex CLI 0.161.0, image `docspectra/codex-editor:v1` (`sha256:893251d3…`) |

[`protocol/scoring.json`](../protocol/scoring.json) lists the remaining image digests and configuration hashes. The study's drivers, evidence records and the analyses that produced the paper's numbers are in DocSpectra/DocSpectraICSC2027; [DocSpectra/RetrievalArena](https://github.com/DocSpectra/RetrievalArena) holds the reusable framework at the commits above.

## What is not included

Full answer traces, scorer outputs, editor transcripts and runtime logs, the run ledger, blinding keys and model caches are not part of this dataset. The study's evidence records in DocSpectra/DocSpectraICSC2027 preserve their SHA-256 values. Transcripts, logs, the ledger and keys also contain author communications, workstation paths or session material.
