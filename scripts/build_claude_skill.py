#!/usr/bin/env python3
"""Build the Claude .skill archive from the canonical ARC skill."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "advance-reasoning-chain" / "SKILL.md"
OUTPUT = ROOT / "dist" / "advance-reasoning-chain.skill"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as archive:
    archive.write(SOURCE, "advance-reasoning-chain/SKILL.md")
print(OUTPUT)
