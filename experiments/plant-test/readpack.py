#!/usr/bin/env python3
"""Emit a blinded human reading pack, plus a separate key.

The human read is the real result. Read readpack.md cold - ideally with someone
else - score each pair, then open readpack-key.md.
"""
import json
import random
import sys
from pathlib import Path

rows = json.loads(Path(sys.argv[1] if len(sys.argv) > 1 else "results.json").read_text())
random.Random(1).shuffle(rows)

pack = ["# Reading pack\n",
        "For each pair: does episode 11 feel **earned** by episode 3, 1-5? Was it still a",
        "surprise? Write the number down before moving on. Conditions are hidden.\n"]
key = ["# Key - do not open until scored\n", "| # | scenario | condition |", "|---|---|---|"]

for n, row in enumerate(rows, 1):
    pack += [f"\n---\n\n## Pair {n}\n", "### Episode 3\n", row["plant"],
             "\n### Episode 11\n", row["payoff"], "\n**Earned 1-5: ____  Surprising? ____**\n"]
    key.append(f"| {n} | {row['scenario']} | {row['condition']} |")

Path("readpack.md").write_text("\n".join(pack))
Path("readpack-key.md").write_text("\n".join(key))
print(f"wrote readpack.md ({len(rows)} pairs) and readpack-key.md")
