#!/usr/bin/env python3
"""Build a repository ZIP from an explicit allowlist and verify it after extraction."""
import hashlib
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
NAME = "onechartlab-skills"
VERSION = "0.1.1"
ALLOWED_ROOT_FILES = {
    ".gitignore", "AGENTS.md", "CHANGELOG.md", "CONTRIBUTING.md", "LICENSE",
    "README.md", "README.en.md", "SECURITY.md", "TRADEMARKS.md",
}
ALLOWED_DIRS = {"assets", "docs", "scripts", "skills", "tests"}
DENIED_PARTS = {
    ".git", "__pycache__", ".cache", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", ".venv", "venv", "node_modules", ".idea", ".vscode",
    "runs", "dist", "evidence", "logs", "log",
}
DENIED_NAMES = {".DS_Store", ".env", "SHA256SUMS"}
DENIED_SUFFIXES = {".log", ".zip", ".skill", ".pyc", ".pyo", ".tmp", ".swp", ".session"}


def include(path):
    rel = path.relative_to(ROOT)
    if len(rel.parts) == 1:
        return rel.name in ALLOWED_ROOT_FILES
    if rel.parts[0] not in ALLOWED_DIRS:
        return False
    if set(rel.parts) & DENIED_PARTS or path.name in DENIED_NAMES:
        return False
    return path.suffix not in DENIED_SUFFIXES


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    check = subprocess.run([sys.executable, "scripts/check_repo.py"], cwd=ROOT)
    if check.returncode:
        return check.returncode
    archive = OUT / f"{NAME}-{VERSION}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(ROOT.rglob("*")):
            if path.is_file() and include(path):
                bundle.write(path, Path(NAME) / path.relative_to(ROOT))
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    hash_lines = [f"{digest}  {archive.name}"]
    skill_package = OUT / "agent-cowork-control.skill"
    if skill_package.exists():
        skill_digest = hashlib.sha256(skill_package.read_bytes()).hexdigest()
        hash_lines.append(f"{skill_digest}  {skill_package.name}")
    (OUT / "SHA256SUMS").write_text("\n".join(hash_lines) + "\n", encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(archive) as bundle:
            bundle.extractall(tmp)
        extracted = Path(tmp) / NAME
        verify = subprocess.run([sys.executable, "scripts/check_repo.py"], cwd=extracted)
        if verify.returncode:
            return verify.returncode
    print(f"PASS {archive}")
    print(f"SHA256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
