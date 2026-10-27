"""Minimal loaders for DocSpectra/DockerDocsSet2026 (standard library only).

Question loaders read only the question files, so labels cannot leak into a
question-only pipeline. Labels are loaded by separate, explicitly named calls.

    import sys; sys.path.insert(0, "tools")
    import load
    questions = load.load_questions(".", tier=2)                   # 144 extracted FAQ questions
    freeze = load.load_questions(".", tier=2, population="in_common_105")
    qrels = load.load_qrels(".", arm="LT")                         # final verified support for docs-lt
"""
from __future__ import annotations

import json
from pathlib import Path

QUESTION_FILES = {1: "questions/tier1/tasks.jsonl", 2: "questions/tier2/questions.jsonl"}
POPULATIONS = ("in_candidate_pool_142", "in_freeze_111", "in_common_105", "in_common_101")


def _jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_questions(root, tier: int, population: str | None = None) -> list[dict]:
    """Question text only: [{"question_id"|"task_id", "question"}]. Optional tier-2 population filter."""
    root = Path(root)
    rows = _jsonl(root / QUESTION_FILES[tier])
    if population is None:
        return rows
    if tier != 2 or population not in POPULATIONS:
        raise ValueError(f"population must be one of {POPULATIONS} (tier 2 only)")
    keep = {p["question_id"] for p in _jsonl(root / "questions/tier2/populations.jsonl") if p[population]}
    return [q for q in rows if q["question_id"] in keep]


def load_reference_answers(root) -> dict[str, dict]:
    """Tier-2 FAQ reference answers by question ID (labels; keep away from answering models)."""
    return {r["question_id"]: r for r in _jsonl(Path(root) / "questions/tier2/reference_answers.jsonl")}


def load_requirements(root) -> list[dict]:
    """Tier-1 core requirements with acceptance criteria and supporting quotations (labels)."""
    return _jsonl(Path(root) / "questions/tier1/requirements.jsonl")


def load_qrels(root, arm: str, stage: str = "final-v4") -> list[dict]:
    """Tier-2 support judgments for one study arm (O, S, LT, R0) and stage (c2-v2, pool-v3, final-v4)."""
    root = Path(root)
    package = json.loads((root / "manifests/package.json").read_text(encoding="utf-8"))
    for spec in package["judgments"]["tier2_qrels"]:
        if spec["arm"] == arm and spec["stage"] == stage:
            return _jsonl(root / spec["path"])
    raise ValueError(f"no qrels for arm={arm!r} stage={stage!r}")
