#!/usr/bin/env python3
"""Validate the standalone public marketplace without third-party packages."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLE = ROOT / "examples" / "beginner-note"
TEXT_SUFFIXES = {"", ".json", ".md", ".py", ".svg", ".txt", ".yaml", ".yml"}
FORBIDDEN = (
    re.compile(r"github\.com/team478a/note-monetization-system", re.IGNORECASE),
    re.compile(r"(?:[A-Z]:\\Users\\|/Users/)[^\s<]+", re.IGNORECASE),
    re.compile(r"\b(?:sk|ghp|github_pat)-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)
REQUIRED = (
    ".agents/plugins/marketplace.json",
    "README.md",
    "SUPPORT.md",
    "LICENSE",
    "docs/JAPANESE_FREE_GUIDE.md",
    "examples/beginner-note/README.md",
    "examples/beginner-note/project.json",
    "examples/beginner-note/sources.json",
    "examples/beginner-note/draft.md",
    "examples/beginner-note/draft.manifest.json",
    "examples/beginner-note/sources/article-workflow.md",
    "plugins/source-backed-article-studio/plugin.json",
    "plugins/source-backed-article-studio/legal/PRIVACY.md",
    "plugins/source-backed-article-studio/legal/TERMS.md",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"invalid JSON at {path.relative_to(ROOT).as_posix()}: {error}")
    if not isinstance(value, dict):
        fail(f"JSON root must be an object: {path.relative_to(ROOT).as_posix()}")
    return value


def validate_required_files() -> None:
    missing = [relative for relative in REQUIRED if not (ROOT / relative).is_file()]
    if missing:
        fail(f"required files are missing: {', '.join(missing)}")


def validate_marketplace() -> None:
    marketplace = read_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    if marketplace.get("name") != "ai-maker-lab":
        fail("marketplace name must be ai-maker-lab")
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        fail("marketplace must contain exactly one Plugin")
    source = plugins[0].get("source", {})
    if source.get("path") != "./plugins/source-backed-article-studio":
        fail("unexpected Plugin source path")


def validate_guide() -> None:
    guide = (ROOT / "docs" / "JAPANESE_FREE_GUIDE.md").read_text(encoding="utf-8")
    plugin = read_json(ROOT / "plugins" / "source-backed-article-studio" / "plugin.json")
    version = plugin.get("version")
    required_phrases = (
        f"公開版`{version}`",
        "codex plugin marketplace add team478a/ai-maker-lab-plugins --ref main",
        "codex plugin marketplace upgrade ai-maker-lab",
        "Codex CLI",
        "Codexデスクトップ",
        "MIT License",
        "Privacy Policy",
        "Terms of Use",
        "GitHub Issues",
    )
    missing = [phrase for phrase in required_phrases if phrase not in guide]
    if missing:
        fail(f"guide is missing required content: {', '.join(missing)}")


def validate_example() -> None:
    project = read_json(EXAMPLE / "project.json")
    registry = read_json(EXAMPLE / "sources.json")
    manifest = read_json(EXAMPLE / "draft.manifest.json")
    if not project.get("project_id") or project.get("project_id") != registry.get("project_id"):
        fail("example project IDs do not match")
    if project.get("project_id") != manifest.get("project_id"):
        fail("example manifest project ID does not match")

    sources = registry.get("sources")
    if not isinstance(sources, list) or not sources:
        fail("example must register at least one source")
    source_ids = {source.get("id") for source in sources if isinstance(source, dict)}
    if None in source_ids or "" in source_ids:
        fail("example source IDs must not be empty")
    referenced_ids = set(manifest.get("source_ids", []))
    for fact in project.get("verified_facts", []):
        referenced_ids.add(fact.get("source_id"))
    for claim in manifest.get("claims", []):
        referenced_ids.update(claim.get("source_ids", []))
    unknown = sorted(str(value) for value in referenced_ids - source_ids)
    if unknown:
        fail(f"example references unknown source IDs: {', '.join(unknown)}")

    draft = EXAMPLE / "draft.md"
    normalized_draft = draft.read_text(encoding="utf-8").replace("\r\n", "\n")
    actual_hash = hashlib.sha256(normalized_draft.encode("utf-8")).hexdigest()
    if manifest.get("content_sha256") != actual_hash:
        fail("example draft SHA-256 does not match its manifest")
    if manifest.get("status") != "draft" or "status: draft" not in draft.read_text(encoding="utf-8"):
        fail("example outputs must remain drafts")


def validate_internal_links() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for relative in ("README.md", "docs/JAPANESE_FREE_GUIDE.md", "examples/beginner-note/README.md"):
        path = ROOT / relative
        for target in link_pattern.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("https://", "http://", "#")):
                continue
            clean_target = target.split("#", 1)[0]
            if clean_target and not (path.parent / clean_target).resolve().is_file():
                fail(f"broken internal link in {relative}: {target}")


def scan_public_tree() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if ".git" in path.relative_to(ROOT).parts:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN:
            if pattern.search(text):
                fail(f"private or secret value detected in {path.relative_to(ROOT).as_posix()}")


def main() -> None:
    validate_required_files()
    validate_marketplace()
    validate_guide()
    validate_example()
    validate_internal_links()
    scan_public_tree()
    files = sum(1 for path in ROOT.rglob("*") if path.is_file())
    print(f"Public distribution validation passed: files={files}, example_sources=1")


if __name__ == "__main__":
    main()
