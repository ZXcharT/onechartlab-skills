import os
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_release import include
from verify_artifacts import safe_member

REQUIRED = ["README.md","README.en.md","LICENSE","CONTRIBUTING.md","SECURITY.md","CHANGELOG.md",".gitignore","docs/STANDARDS.md","docs/COMPATIBILITY.md","docs/RELEASE.md","docs/RULE-MAPPING.md","scripts/check_repo.py","scripts/policy_harness.py","scripts/build_release.py","scripts/verify_artifacts.py","tests/test_policy.py","tests/test_repository.py","skills/agent-cowork-control/SKILL.md","skills/agent-cowork-control/references/behavior-contract.md"]
EXCLUDED = {".git", "__pycache__", "runs", "dist", "evidence"}
TEXT_EXT = {".md", ".py", ".json", ""}

def text_files(root=ROOT):
    for p in root.rglob("*"):
        if p.is_file() and not set(p.relative_to(root).parts) & EXCLUDED and p.suffix in TEXT_EXT:
            yield p

class RepositoryTests(unittest.TestCase):
    def test_required_structure(self):
        for item in REQUIRED: self.assertTrue((ROOT/item).is_file(), item)
        self.assertEqual(14, len(list((ROOT/"tests/fixtures").glob("T*.json"))))
    def test_frontmatter_and_line_limit(self):
        p = ROOT/"skills/agent-cowork-control/SKILL.md"; t=p.read_text(encoding="utf-8")
        self.assertTrue(t.startswith("---\nname: agent-cowork-control\n"))
        self.assertLess(len(t.splitlines()), 500)
    def test_relative_links_and_single_reference_level(self):
        for p in text_files():
            t=p.read_text(encoding="utf-8")
            for link in re.findall(r"\]\(([^)]+)\)", t):
                if "://" not in link and not link.startswith("#"):
                    self.assertFalse(link.startswith("/"), f"absolute link {p}: {link}")
                    resolved = (p.parent/link).resolve()
                    self.assertTrue(resolved.exists(), f"broken {p}: {link}")
                    if "skills/agent-cowork-control" in str(p):
                        skill_root = (ROOT/"skills/agent-cowork-control").resolve()
                        self.assertTrue(resolved == skill_root or skill_root in resolved.parents, f"Skill link escapes package root {p}: {link}")
        refs=ROOT/"skills/agent-cowork-control/references"
        self.assertFalse(any(x.is_dir() for x in refs.iterdir()))
        self.assertFalse((ROOT/"skills/agent-cowork-control/README.md").exists())
    def test_privacy_patterns_with_context_allowlist(self):
        forbidden = [r"/Users/[A-Za-z0-9_.-]+/", r"sess_[A-Za-z0-9_]{8,}", r"(?im)^\s*(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[^\s'\"]+", r"\b"+"hua"+"zhu"+r"\b", r"\b"+"k"+"g"+r"\b"]
        hits=[]
        for p in text_files():
            t=p.read_text(encoding="utf-8")
            for pat in forbidden:
                if re.search(pat,t): hits.append(f"{p.relative_to(ROOT)}:{pat}")
        self.assertEqual([],hits,"privacy/personalization leak: "+"; ".join(hits))
    def test_archive_allowlist_and_exclusion_rules(self):
        self.assertTrue(include(ROOT/"README.md"))
        self.assertTrue(include(ROOT/"skills/agent-cowork-control/SKILL.md"))
        for rel in ["notes.md", ".cache/x", ".pytest_cache/x", ".mypy_cache/x", ".DS_Store", "logs/run.txt", "docs/debug.log", ".env"]:
            self.assertFalse(include(ROOT/rel), rel)
        for member in ["onechartlab-skills/.cache/x", "onechartlab-skills/.DS_Store", "onechartlab-skills/logs/run.txt", "../escape.txt"]:
            self.assertFalse(safe_member(member), member)

if __name__ == "__main__": unittest.main()
