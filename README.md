# DockerDocsSet2026: original documentation (`docs-original`)

This branch of [DocSpectra/DockerDocsSet2026](https://github.com/DocSpectra/DockerDocsSet2026) holds one documentation version from the Docker application in the ICSC 2027 submission *Measuring Directed Documentation Structure with Normalized Magnetic Spectra*. The [`main` branch](https://github.com/DocSpectra/DockerDocsSet2026/tree/main) has the dataset documentation, question sets, support judgments, manifests and the offline verifier.

The original Docker documentation pages of the experiment corpus (`docs_scope_v1`, 1,218 pages), byte-identical to docker/docs at the pinned commit. The study's sham control S used this same tree and export, so S has no separate branch.

| Field | Value |
| --- | --- |
| Variant | O, original Docker documentation (also served as the S sham control) |
| Upstream source | [docker/docs](https://github.com/docker/docs) at commit [`274681c`](https://github.com/docker/docs/tree/274681c49355bd951ae60c9208e854ff70f12474) (May 1, 2026) |
| Documentation files | 1,218 |
| Documentation tree identity | `4c5e0499392bb25dd9641ea191ed3e2fff075bbee27ad798fba6deeff731c43c` |
| Experiment corpus export | 1,218 pages, 2,494 directed links |
| Export corpus tree identity | `ebce0bcead737137cce154bf6415413cc60d58e371432ac6c046a312cc1bcadc` |
| Export graph file SHA-256 | `ff89ed48d6318c00c6b2bf5adf5dc0f2fc43ec56f3d11b5a45cf356fa98c3945` |
| Study variant IDs | `v-5d89a3217d52`, `v-9a7d7f0e7b47` |
| Upstream page snapshot | `upstream-pages/`, 1,487 files, identity `7b54d187fa99f9acc09353f6ae114aa9bfa2579d645df3168c9bc0d2043a9445` |
| Historical export | `historical-export/`, 1,263 pages, corpus identity `093304d8ad4e88bfb16dcdee225e8d0587a031f9180574080b7a29e8477eb674` |

Tree identities are content hashes, not Git commit SHAs: the SHA-256 of the compact, key-sorted JSON object that maps each POSIX relative path to the SHA-256 of its bytes. [`VARIANT.json`](VARIANT.json) records the same values in machine-readable form.

## Layout

- `documentation/`: the documentation tree, byte for byte. Only this directory is covered by the documentation tree identity.
- `export/corpus/`: the retrieval corpus used for searching and answering, one Markdown file per page, named by document ID. The exporter writes CRLF line endings.
- `export/graph_edges.csv`: the directed page-to-page link graph extracted from the same pages (`source,target` document IDs).
- `upstream-pages/`: every page-suffix file (`.md`, `.html`, `.txt`) of docker/docs at the pinned commit, as read by the exporter, including the 26 FAQ pages that supply the tier-2 questions. `CLAUDE.md` is a Git symlink upstream and is stored here as a file containing its target, `AGENTS.md`.
- `historical-export/`: the earlier repository-wide export (1,263 pages and its link graph) from which the 144 FAQ questions were extracted.
- `VARIANT.json`: identities, counts and lineage of this branch.
- `LICENSE`, `NOTICE.md`: upstream license and attribution, including the modification notice.

Line-ending conversion is disabled in `.gitattributes`, so a checkout reproduces the recorded bytes.

## Checking the identity

```python
import hashlib, json, pathlib

root = pathlib.Path("documentation")
files = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
         for p in sorted(root.rglob("*")) if p.is_file()}
print(hashlib.sha256(json.dumps(files, sort_keys=True, separators=(",", ":")).encode()).hexdigest())
```

The result should equal `4c5e0499392bb25dd9641ea191ed3e2fff075bbee27ad798fba6deeff731c43c`. `python tools/verify.py` on `main` checks every branch, archive and manifest.

## Commits on this branch

A single packaging commit holds this snapshot. It is not a commit of docker/docs.

## Citation

Cite the package as described in [`CITATION.cff` on `main`](https://github.com/DocSpectra/DockerDocsSet2026/blob/main/CITATION.cff) and the upstream source as Docker documentation (docker/docs, commit `274681c49355bd951ae60c9208e854ff70f12474`).
