# DockerDocsSet2026: R0 experimental refinement (`docs-r0`)

This branch of [DocSpectra/DockerDocsSet2026](https://github.com/DocSpectra/DockerDocsSet2026) holds one documentation version from the Docker application in the ICSC 2027 submission *Measuring Directed Documentation Structure with Normalized Magnetic Spectra*. The [`main` branch](https://github.com/DocSpectra/DockerDocsSet2026/tree/main) has the dataset documentation, question sets, support judgments, manifests and the offline verifier.

An experimental refinement of the original pages, produced area by area by an automated editing agent given the same reorganization instruction as LT but no prescribed structure, then reconciled across the whole corpus. It is not a Docker release, and its inclusion here does not imply that it improves the documentation.

| Field | Value |
| --- | --- |
| Variant | R0, uninformed refinement (experimental) |
| Upstream source | [docker/docs](https://github.com/docker/docs) at commit [`274681c`](https://github.com/docker/docs/tree/274681c49355bd951ae60c9208e854ff70f12474) (May 1, 2026) |
| Documentation files | 1,229 |
| Documentation tree identity | `a01b9cedb040a7f7c52845a1ea7bd66a5da8f26dc6b78889b21f87a5e3d658d1` |
| Experiment corpus export | 1,229 pages, 4,502 directed links |
| Export corpus tree identity | `bd3ce666479bed1e1d401c9207dc467313a2b75c2e6721174425a396f09f15b5` |
| Export graph file SHA-256 | `a77abe7a9bbdaa995b5d3edaabba89037b3f5c7e39aea1bc6f703f4ef0dd5590` |
| Study variant IDs | `v-c2c2731d2141` |
| Final checkpoint | session R0-r27, identity `a01b9cedb040a7f7c52845a1ea7bd66a5da8f26dc6b78889b21f87a5e3d658d1` |

Tree identities are content hashes, not Git commit SHAs: the SHA-256 of the compact, key-sorted JSON object that maps each POSIX relative path to the SHA-256 of its bytes. [`VARIANT.json`](VARIANT.json) records the same values in machine-readable form.

## Layout

- `documentation/`: the documentation tree, byte for byte. Only this directory is covered by the documentation tree identity.
- `export/corpus/`: the retrieval corpus used for searching and answering, one Markdown file per page, named by document ID. The exporter writes CRLF line endings.
- `export/graph_edges.csv`: the directed page-to-page link graph extracted from the same pages (`source,target` document IDs).
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

The result should equal `a01b9cedb040a7f7c52845a1ea7bd66a5da8f26dc6b78889b21f87a5e3d658d1`. `python tools/verify.py` on `main` checks every branch, archive and manifest.

## Commits on this branch

The parent commit is the `docs-original` snapshot, so `git diff docs-original docs-r0 -- documentation/` shows every change. Both commits are packaging commits created from the frozen trees; they do not reproduce the editing history, which is described in `protocol/` on `main`.

## Citation

Cite the package as described in [`CITATION.cff` on `main`](https://github.com/DocSpectra/DockerDocsSet2026/blob/main/CITATION.cff) and the upstream source as Docker documentation (docker/docs, commit `274681c49355bd951ae60c9208e854ff70f12474`).
