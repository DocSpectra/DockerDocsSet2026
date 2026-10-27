# How the LT and R0 refinements were produced

LT and R0 are experimental refinements of the 1,218-page experiment corpus, made on October 19–20, 2026. Each is the output of one automated editing run. They are study variants, not Docker releases, and their inclusion does not imply that they improve the documentation. This page describes the protocol as it was run. The complete per-session records are in [`protocol/refinement/`](../protocol/refinement/), and the study code and evidence are in [DocSpectra/DocSpectraICSC2027](https://github.com/DocSpectra/DocSpectraICSC2027).

## The two arms

Both arms used the same editing agent, the same 25 documentation areas, the same order and the same admission check. Their instructions are identical except for one sentence. Both ask the editor to reorganize the documentation so a reader can find task-specific steps, prerequisites and caveats through clear page structure and links, to preserve every material fact, command, warning, exception and version scope, and to add only navigation text that makes no new factual claim.

- **LT, leaf-and-trunk refinement.** The editor builds toward "specific leaf pages that link one way to shared, abstracted procedure and context pages." Base instruction: [`docker-editor-LT-v1.txt`](../protocol/refinement/prompts/docker-editor-LT-v1.txt).
- **R0, uninformed refinement.** The editor is told: "Do not aim for any prescribed graph morphology." Base instruction: [`docker-editor-R0-v4.txt`](../protocol/refinement/prompts/docker-editor-R0-v4.txt).

Each session prompt was composed from the arm's base instruction and the area's assignment (composition version 2, which also removed a stale sentence about session limits from the base text). Every session prompt used is in [`protocol/refinement/prompts/sessions/`](../protocol/refinement/prompts/sessions/), with its SHA-256 in `sessions.jsonl`. The editor never saw questions, answers, judgments, structural measurements, admission results or the other arm's pages.

## Areas

A survey session divided the corpus into 25 areas (A01–A25) using [`docker-area-selection-v1.txt`](../protocol/refinement/prompts/docker-area-selection-v1.txt). The survey recorded a rationale for each area rather than a title; the short labels in [`areas.jsonl`](../protocol/refinement/areas.jsonl) were written for this package from those rationales. Each row lists the area's original pages and source-path prefixes, its sessions in both arms and the final admission decision.

## Sessions and admission

The runtime was Codex CLI 0.161.0 running `gpt-6.1-sol` at medium reasoning effort in a per-session container (`docspectra/codex-editor:v1`) behind an egress allowlist proxy. Each session was one editor invocation with a 5,400-second wall-clock limit. The editor worked on a copy of the current admitted tree; when it finished, the host checked the result:

- **Structural connectivity (C).** Original anchor pages survive, original main-component pages and every new page stay in the main weakly connected component, every new page has at least one incoming Markdown link from another page (C1b), and the normalized undirected algebraic connectivity on the evaluation set is at least 0.90 of the original value (C2). Version `structural_connectivity_constraint.v1`; the RetrievalArena commit and code hashes are in each receipt.
- **Preservation.** Protected lines (code-fence openers, shell commands, `docker` commands and warning lines) must survive, and the edit must not introduce unresolved links.

An admitted session advanced the arm's tree; a rejected one was rolled back, leaving the area unchanged in that arm. After all 25 area passes, one reconciliation session per arm worked over the whole tree to repair cross-area links and inconsistencies; both reconciliations were admitted. The final checkpoints are LT-r30 and R0-r27.

| Arm | Areas admitted | Final checkpoint | Files modified / added / removed |
| --- | ---: | --- | --- |
| LT | 18 of 25 | LT-r30 `d4cdf7f7d3f9` | 773 / 605 / 0 |
| R0 | 23 of 25 | R0-r27 `a01b9cedb040` | 1,006 / 11 / 0 |

## Protocol changes during the run

The run record lists every change to the host's admission and runtime code, with its timing, in [`run-history.json`](../protocol/refinement/run-history.json). The session table records which fixes were in force for each session; this is inferred from the order of ledger entries and driver commits.

- **Infrastructure and admission fixes.** Sessions that never reached the editor were voided and rerun (LT-r01 for A09, R0-r03 for A19). Three admission-check implementation defects were fixed early on October 19: the resolution of documentation-site URLs, the C2 evaluation set (which now includes formerly isolated pages that an edit joins to the main component), and prompt-line canonicalization for protected lines. Later fixes canonicalized internal whitespace and a code-fence opener with an unclosed attribute brace. Sessions rejected only because of a defect were re-evaluated and admitted under the corrected check (R0-r02 for A21, LT-r14 for A24, LT-r25 for A18 and the LT reconciliation LT-r30). Every LT area admission depends on the corrected C2 evaluation set: under the original computation, C2 scored every LT area as disconnected and no LT area would have been admitted.
- **A21, implementation-defect rerun.** LT's first A21 session (LT-r03) ran before the fixes above took effect and was rejected on defects that were later fixed. The area was reopened and rerun as LT-r15.
- **Incoming-link exemption.** After all 25 area passes in both arms, and before either reconciliation, the author amended C1b. New pages under `content/includes/` that some page includes through a shortcode, and new section `_index.md` pages whose folder holds another page, no longer count against C1b in either arm. The link graph excludes Hugo templating by design, so such pages can never receive a Markdown link. Two LT areas had failed only C1b: A10 (LT-r18) and A12 (LT-r24). They were rerun as LT-r28 and LT-r29. Both reruns were admitted without using the exemption: their admission receipts record no exempted page, so both final versions meet the original incoming-link requirement. R0 never failed C1b. The A10 and A12 reruns are additional passes given after initial results were reviewed; the A21 rerun repaired an implementation defect.

The study reported the structural comparison with and without these additional passes: dropping LT A10, A12 and A21 leaves 15 paired areas instead of 18. The sensitivity results and the full deviation record are in DocSpectra/DocSpectraICSC2027.

## What the editing changed

[`manifests/changes-lt.csv`](../manifests/changes-lt.csv) and [`manifests/changes-r0.csv`](../manifests/changes-r0.csv) list each modified or added file with its original upstream link. No refinement removed or renamed a page. The editing also changed the link structure: the LT export has 5,203 links and the R0 export 4,502, against 2,494 in the original.

## Not included

Editor transcripts, runtime logs, the run ledger and the host's private records are not part of the package. They hold author communications, absolute workstation paths and session credentials material. Their SHA-256 values are preserved in the study's evidence records.
