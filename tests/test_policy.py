import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from policy_harness import run_fixture

class PolicyFixtures(unittest.TestCase):
    def test_t01_to_t14(self):
        fixtures = sorted((ROOT / "tests" / "fixtures").glob("T*.json"))
        self.assertEqual(14, len(fixtures))
        for path in fixtures:
            with self.subTest(path=path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertRegex(data["id"], r"^T(0[1-9]|1[0-4])$")
                self.assertGreaterEqual(len(data["cases"]), 3)
                ok, results = run_fixture(path)
                self.assertTrue(ok, results)
                self.assertTrue(any(case["kind"] == "allow" for case in data["cases"]))
                self.assertTrue(any(case["kind"] == "block" for case in data["cases"]))
                self.assertIn("pass_condition", data)
                self.assertIn("block_condition", data)

if __name__ == "__main__": unittest.main()
