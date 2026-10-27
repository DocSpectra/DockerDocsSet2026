# DockerDocsSet2026: LT experimental refinement (`docs-lt`)

This branch of [DocSpectra/DockerDocsSet2026](https://github.com/DocSpectra/DockerDocsSet2026) holds one documentation version from the Docker application in the ICSC 2027 submission *Measuring Directed Documentation Structure with Normalized Magnetic Spectra*. The [`main` branch](https://github.com/DocSpectra/DockerDocsSet2026/tree/main) has the dataset documentation, question sets, support judgments, manifests and the offline verifier.

An experimental refinement of the original pages, produced area by area by an automated editing agent instructed to build toward specific leaf pages that link one way to shared procedure and context pages, then reconciled across the whole corpus. It is not a Docker release, and its inclusion here does not imply that it improves the documentation.

| Field | Value |
| --- | --- |
| Variant | LT, leaf-and-trunk refinement (experimental) |
| Upstream source | [docker/docs](https://github.com/docker/docs) at commit [`274681c`](https://github.com/docker/docs/tree/274681c49355bd951ae60c9208e854ff70f12474) (May 1, 2026) |
| Documentation files | 1,823 |
| Documentation tree identity | `d4cdf7f7d3f9ddc27696ae397487cd335b70e8ab8687f1e7086bfb1b0d115f74` |
| Experiment corpus export | 1,823 pages, 5,203 directed links |
| Export corpus tree identity | `d4496be66c10e9050ed2467bab12d95277064b62464284d17d448a1c4c79171f` |
| Export graph file SHA-256 | `83d6bcd62df873e1ea7257f5f468f90fa0d50093425c54a719ff8b9fc68a5d0c` |
| Study variant IDs | `v-6337600cdc97` |
| Final checkpoint | session LT-r30, identity `d4cdf7f7d3f9ddc27696ae397487cd335b70e8ab8687f1e7086bfb1b0d115f74` |

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

The result should equal `d4cdf7f7d3f9ddc27696ae397487cd335b70e8ab8687f1e7086bfb1b0d115f74`. `python tools/verify.py` on `main` checks every branch, archive and manifest.

## Commits on this branch

The parent commit is the `docs-original` snapshot, so `git diff docs-original docs-lt -- documentation/` shows every change. Both commits are packaging commits created from the frozen trees; they do not reproduce the editing history, which is described in `protocol/` on `main`.

## Citation

Cite the package as described in [`CITATION.cff` on `main`](https://github.com/DocSpectra/DockerDocsSet2026/blob/main/CITATION.cff) and the upstream source as Docker documentation (docker/docs, commit `274681c49355bd951ae60c9208e854ff70f12474`).
