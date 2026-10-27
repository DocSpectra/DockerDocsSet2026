"""Offline verifier for DocSpectra/DockerDocsSet2026 (Python 3.9+, standard library only).

Run from the root of a clone (main checked out):

    python tools/verify.py                 # checksums, question/label joins, branches from git objects
    python tools/verify.py --archives DIR  # also check downloaded release archives in DIR

Nothing is downloaded and no model is run. Exit status 1 means at least one check failed.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAILURES: list[str] = []


def check(ok: bool, message: str) -> None:
    print(("PASS " if ok else "FAIL ") + message)
    if not ok:
        FAILURES.append(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def tree_hash(files: dict) -> str:
    """Content-tree identity: SHA-256 of compact, key-sorted JSON {posix relpath: sha256(bytes)}."""
    return sha256(json.dumps(files, sort_keys=True, separators=(",", ":")).encode())


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def load_jsonl(rel: str) -> list:
    return [json.loads(line) for line in (ROOT / rel).read_text(encoding="utf-8").splitlines() if line.strip()]


def verify_checksums() -> None:
    listed = {}
    for line in (ROOT / "manifests" / "checksums.sha256").read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        listed[name] = digest
    bad = [n for n, d in listed.items() if not (ROOT / n).is_file() or sha256((ROOT / n).read_bytes()) != d]
    check(not bad, f"main-branch checksums: {len(listed) - len(bad)}/{len(listed)} files match" + (f" (first bad: {bad[0]})" if bad else ""))
    tracked = git(["ls-files"]).decode().splitlines() if is_git() else []
    if tracked:
        unlisted = sorted(set(tracked) - set(listed) - {"manifests/checksums.sha256"})
        check(not unlisted, f"every tracked main-branch file is in checksums.sha256" + (f" (missing: {unlisted[:3]})" if unlisted else ""))


def verify_portability() -> None:
    # A concrete Windows profile path (raw or JSON-escaped) or the build workstation's project folder.
    # Docker's own text uses placeholders such as C:\Users\[USERNAME] and mentions /Users and /home paths.
    pattern = re.compile(rb"[A-Za-z]:(?:\\\\|/)+Users(?:\\\\|/)+[A-Za-z0-9._-]+(?:\\\\|/)|ResearchProjects")
    hits = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
            if p.is_file() and ".git" not in p.parts and p.name != "verify.py" and pattern.search(p.read_bytes())]
    check(not hits, "no absolute workstation paths in main-branch files" + (f" (found in {hits[:3]})" if hits else ""))


def verify_links() -> None:
    """Relative Markdown links on main resolve to a file or directory (external URLs are not fetched)."""
    link = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
    broken = []
    for page in ROOT.rglob("*.md"):
        if ".git" in page.parts or "protocol" in page.relative_to(ROOT).parts:
            continue
        for target in link.findall(page.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            if not (page.parent / target.split("#", 1)[0]).exists():
                broken.append(f"{page.relative_to(ROOT).as_posix()} -> {target}")
    check(not broken, "relative links in main-branch Markdown resolve" + (f" (broken: {broken[:3]})" if broken else ""))


def verify_questions() -> None:
    pkg = load_json("manifests/package.json")
    expect = pkg["populations"]
    t2 = load_jsonl("questions/tier2/questions.jsonl")
    refs = load_jsonl("questions/tier2/reference_answers.jsonl")
    pops = load_jsonl("questions/tier2/populations.jsonl")
    ids = [q["question_id"] for q in t2]
    check(len(ids) == len(set(ids)) == expect["tier2_extracted"], f"tier 2: {len(ids)} unique extracted questions (expected {expect['tier2_extracted']})")
    check(all(set(q) == {"question_id", "question"} for q in t2), "tier 2: question file holds only question_id and question")
    check([r["question_id"] for r in refs] == ids, "tier 2: reference answers join one-to-one, same order")
    check([p["question_id"] for p in pops] == ids, "tier 2: population rows join one-to-one")
    for key, flag in (("tier2_candidate_pool", "in_candidate_pool_142"), ("tier2_freeze", "in_freeze_111"),
                      ("tier2_common", "in_common_105"), ("tier2_common_original", "in_common_101")):
        n = sum(1 for p in pops if p[flag])
        check(n == expect[key], f"tier 2: {flag} = {n} (expected {expect[key]})")
    nested = all((not p["in_common_101"] or p["in_common_105"]) and (not p["in_common_105"] or p["in_freeze_111"])
                 and (not p["in_freeze_111"] or p["in_candidate_pool_142"]) for p in pops)
    check(nested, "tier 2: 101 within 105 within 111 within 142")
    check(all(p["in_freeze_111"] or p["exclusion_reason"] for p in pops), "tier 2: every question outside the 111 has a recorded reason")
    check(all(p["in_common_105"] or not p["in_freeze_111"] or p["common_105_exclusion"] for p in pops),
          "tier 2: every freeze question outside the common 105 has a recorded reason")
    t1 = load_jsonl("questions/tier1/tasks.jsonl")
    reqs = load_jsonl("questions/tier1/requirements.jsonl")
    task_ids = [t["task_id"] for t in t1]
    req_ids = [r["requirement_id"] for r in reqs]
    check(len(task_ids) == len(set(task_ids)) == expect["tier1_tasks"], f"tier 1: {len(task_ids)} unique tasks")
    check(all(set(t) == {"task_id", "question"} for t in t1), "tier 1: task file holds only task_id and question")
    check(len(req_ids) == len(set(req_ids)) == expect["tier1_requirements"], f"tier 1: {len(req_ids)} unique requirements")
    check(all(r["task_id"] in task_ids for r in reqs), "tier 1: every requirement joins a task")
    pages = {name: {p["doc_id"] for p in load_jsonl(f"manifests/pages-{name}.jsonl")} for name in ("original", "lt", "r0")}
    for r in reqs:
        for q in r.get("support", []):
            if q["doc_id"] not in pages["original"]:
                check(False, f"tier 1: {r['requirement_id']} cites {q['doc_id']}, absent from the original version")
    check(True, "tier 1: requirement support pages checked against the original version")
    for spec in pkg["judgments"]["tier2_qrels"]:
        rows = load_jsonl(spec["path"])
        unknown_q = [r for r in rows if r["question_id"] not in ids]
        unknown_d = [r for r in rows if r["doc_id"] not in pages[spec["documentation"]]]
        keys = [(r["question_id"], r["doc_id"]) for r in rows]
        check(not unknown_q and not unknown_d and len(keys) == len(set(keys)),
              f"qrels {spec['path']}: {len(rows)} rows join questions and {spec['documentation']} pages, no duplicate pairs")
    from_loader = __import__("load")
    q_only = from_loader.load_questions(ROOT, tier=2)
    check(all(set(q) == {"question_id", "question"} for q in q_only), "loader: load_questions returns question text only")


def is_git() -> bool:
    return (ROOT / ".git").exists()


def git(args: list[str], data: bytes | None = None) -> bytes:
    return subprocess.run(["git", "-C", str(ROOT), *args], input=data, check=True, capture_output=True).stdout


def branch_files(ref: str, prefix: str) -> dict:
    listing = git(["ls-tree", "-r", "-z", ref, "--", prefix]).split(b"\0")
    entries = []
    for item in filter(None, listing):
        meta, path = item.split(b"\t", 1)
        mode, kind, obj = meta.split()
        if kind == b"blob":
            entries.append((path.decode(), obj.decode(), mode))
    out = git(["cat-file", "--batch"], ("\n".join(o for _, o, _ in entries) + "\n").encode())
    stream, files = io.BytesIO(out), {}
    for path, _, mode in entries:
        header = stream.readline().split()
        body = stream.read(int(header[2]))
        stream.read(1)
        files[path[len(prefix):]] = sha256(body)
    return files


def verify_branches() -> None:
    if not is_git():
        print("SKIP branches: not a git clone")
        return
    variants = load_json("manifests/variants.json")
    for name, spec in variants["branches"].items():
        ref = f"origin/{spec['branch']}" if git(["branch", "-r", "--list", f"origin/{spec['branch']}"]).strip() else spec["branch"]
        commit = git(["rev-parse", ref]).decode().strip()
        check(commit == spec["packaging_commit"], f"{spec['branch']}: head is the recorded packaging commit {commit[:12]}")
        docs = branch_files(ref, "documentation/")
        check(tree_hash(docs) == spec["documentation_tree_sha256"], f"{spec['branch']}: documentation tree identity {spec['documentation_tree_sha256'][:12]} ({len(docs)} files)")
        corpus = branch_files(ref, "export/corpus/")
        check(tree_hash(corpus) == spec["export_corpus_tree_sha256"], f"{spec['branch']}: export corpus identity ({len(corpus)} pages)")
        graph = branch_files(ref, "export/graph_edges.csv")
        check(graph.get("") == spec["export_graph_sha256"], f"{spec['branch']}: export graph SHA-256")
        pages = {p["rel_path"]: p["sha256"] for p in load_jsonl(f"manifests/pages-{name}.jsonl")}
        check(pages == docs, f"{spec['branch']}: page manifest matches every documentation file")
        for extra, identity in spec.get("extra_trees", {}).items():
            got = tree_hash(branch_files(ref, extra.rstrip("/") + "/"))
            check(got == identity, f"{spec['branch']}: {extra} identity {identity[:12]}")


def verify_archives(directory: Path) -> None:
    assets = load_json("manifests/package.json")["release_assets"]
    for asset in assets:
        path = directory / asset["file"]
        if not path.is_file():
            check(False, f"archive {asset['file']} present in {directory}")
            continue
        check(sha256(path.read_bytes()) == asset["sha256"], f"archive {asset['file']}: SHA-256")
        if asset["file"].endswith(".zip"):
            with zipfile.ZipFile(path) as zf:
                names = [n for n in zf.namelist() if not n.endswith("/")]
                for sub, identity in asset.get("trees", {}).items():
                    lead = f"{asset['prefix']}/{sub.rstrip('/')}/"
                    files = {n[len(lead):]: sha256(zf.read(n)) for n in names if n.startswith(lead)}
                    check(tree_hash(files) == identity, f"archive {asset['file']}: {sub} identity {identity[:12]}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--archives", type=Path, help="directory holding downloaded release archives")
    parser.add_argument("--skip-branches", action="store_true")
    args = parser.parse_args()
    sys.path.insert(0, str(ROOT / "tools"))
    verify_checksums()
    verify_portability()
    verify_links()
    verify_questions()
    if not args.skip_branches:
        verify_branches()
    if args.archives:
        verify_archives(args.archives)
    print(f"\n{'FAILED' if FAILURES else 'OK'}: {len(FAILURES)} failure(s)")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
