#!/usr/bin/env python3
"""Verify repository ZIP and optional .skill package without extracting unsafely."""
import argparse
import hashlib
import re
import zipfile
from pathlib import PurePosixPath, Path

DENIED_PARTS = {".git", "__pycache__", ".cache", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".venv", "venv", "node_modules", ".idea", ".vscode", "runs", "dist", "evidence", "logs", "log"}
DENIED_NAMES = {".DS_Store", ".env"}
DENIED_SUFFIXES = {".log", ".pyc", ".pyo", ".tmp", ".swp", ".session"}
TEXT_SUFFIXES = {"", ".md", ".py", ".json", ".txt", ".yaml", ".yml"}
PRIVACY_PATTERNS = [
    re.compile(r"/Users/[A-Za-z0-9_.-]+/"),
    re.compile(r"/home/[A-Za-z0-9_.-]+/"),
    re.compile(r"C:\\\\Users\\\\[A-Za-z0-9_.-]+\\\\", re.I),
    re.compile(r"sess_[A-Za-z0-9_]{8,}"),
    re.compile(r"(?im)^\s*(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[^\s'\"]+"),
    re.compile(r"\b" + "hua" + "zhu" + r"\b", re.I),
    re.compile(r"\b" + "mao" + "qiu" + r"\b", re.I),
    re.compile(r"\bkg\b", re.I),
]
SCANNER_ALLOWLIST = {"onechartlab-skills/tests/test_repository.py", "onechartlab-skills/scripts/verify_artifacts.py"}
LINK_RE = re.compile(r"\]\(([^)]+)\)")


def safe_member(name):
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts:
        return False
    if set(path.parts) & DENIED_PARTS or path.name in DENIED_NAMES:
        return False
    return path.suffix not in DENIED_SUFFIXES


def read_text(bundle, name):
    if PurePosixPath(name).suffix not in TEXT_SUFFIXES:
        return None
    try:
        return bundle.read(name).decode("utf-8")
    except UnicodeDecodeError:
        return None


def verify_archive(path, expected_top, skill_links=False):
    errors = []
    with zipfile.ZipFile(path) as bundle:
        names = [name for name in bundle.namelist() if not name.endswith("/")]
        tops = {PurePosixPath(name).parts[0] for name in names if PurePosixPath(name).parts}
        if tops != {expected_top}:
            errors.append(f"unexpected top-level entries: {sorted(tops)}")
        name_set = set(names)
        for name in names:
            if not safe_member(name):
                errors.append(f"forbidden archive member: {name}")
            text = read_text(bundle, name)
            if text is None:
                continue
            if name not in SCANNER_ALLOWLIST:
                for pattern in PRIVACY_PATTERNS:
                    if pattern.search(text):
                        errors.append(f"privacy finding in {name}: {pattern.pattern}")
            if skill_links and name.endswith(".md"):
                base = PurePosixPath(name).parent
                for link in LINK_RE.findall(text):
                    if "://" in link or link.startswith("#"):
                        continue
                    target = base.joinpath(link)
                    normalized = PurePosixPath(*[part for part in target.parts if part != "."])
                    if ".." in normalized.parts or not normalized.parts or normalized.parts[0] != expected_top:
                        errors.append(f"Skill link escapes package: {name} -> {link}")
                    elif str(normalized) not in name_set:
                        errors.append(f"broken Skill link: {name} -> {link}")
    return errors


def read_hashes(path):
    result = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, name = line.split(maxsplit=1)
        result[name.strip()] = digest
    return result


def verify_hash(path, hashes):
    actual = hashlib.sha256(Path(path).read_bytes()).hexdigest()
    expected = hashes.get(Path(path).name)
    return None if actual == expected else f"hash mismatch for {Path(path).name}: {actual} != {expected}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True, dest="repo_zip")
    parser.add_argument("--skill")
    parser.add_argument("--sha256sums", required=True)
    args = parser.parse_args()
    hashes = read_hashes(args.sha256sums)
    errors = verify_archive(args.repo_zip, "onechartlab-skills")
    mismatch = verify_hash(args.repo_zip, hashes)
    if mismatch:
        errors.append(mismatch)
    if args.skill:
        errors.extend(verify_archive(args.skill, "agent-cowork-control", skill_links=True))
        mismatch = verify_hash(args.skill, hashes)
        if mismatch:
            errors.append(mismatch)
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    print("PASS artifact structure, privacy, links and hashes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
