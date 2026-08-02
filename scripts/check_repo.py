#!/usr/bin/env python3
"""Run repository checks using the Python standard library."""
import subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
cmd=[sys.executable,"-m","unittest","discover","-s","tests","-v"]
print("CHECK", " ".join(cmd))
p=subprocess.run(cmd,cwd=ROOT)
print("PASS" if p.returncode==0 else "FAIL")
raise SystemExit(p.returncode)
