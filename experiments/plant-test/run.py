#!/usr/bin/env python3
"""Run the plant experiment. See PROTOCOL.md.

Every generation and every judgement is a separate, stateless API call. There is no
shared conversation, which is the only honest way to keep the BLIND condition blind.

    pip install anthropic
    export ANTHROPIC_API_KEY=...
    python run.py --dry-run      # print prompts, spend nothing
    python run.py                # full run, ~$2-3
"""
import argparse
import json
import random
import sys
from pathlib import Path

import fixtures as fx

MODEL = "claude-opus-5"

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "scores": {
            "type": "object",
            "properties": {k: {"type": "integer", "minimum": 1, "maximum": 5}
                           for k in ("a", "b", "c")},
            "required": ["a", "b", "c"],
            "additionalProperties": False,
        },
        "note": {"type": "string", "description": "One sentence. What decided it."},
    },
    "required": ["scores", "note"],
    "additionalProperties": False,
}

PLANT_JUDGE = """\
You are judging one scene from a pulp heist game. It is episode 3 of twelve. Somewhere in
it, the writer may have planted a loose end for a later episode to detonate.

You do NOT know what the payoff is, and you must not guess at one. Judge only what is here.

Score 1-5:
  a) SPECIFICITY - does it leave concrete, named, referenceable material? A person with a
     name, an object, a number, a debt, a face. 1 = nothing to grab, 5 = several solid hooks.
  b) INNOCUOUSNESS - does it AVOID reading as "THIS IS IMPORTANT"? A good plant hides in
     plain sight. 1 = flashing neon signpost, 5 = invisible until it matters.
  c) FLEXIBILITY - could this support at least two genuinely different payoffs?
     1 = one rigid reading, 5 = many live options.
"""

PAYOFF_JUDGE = """\
You are judging a pair of scenes from a pulp heist game: episode 3, then episode 11, where
something planted earlier detonates.

Score 1-5:
  a) EARNED - does the detonation feel set up by episode 3, or arbitrary and bolted on?
     1 = came from nowhere, 5 = inevitable in hindsight.
  b) RECALL - is the planted element specific enough that a player would actually remember
     it eight episodes later? 1 = forgettable detail, 5 = unmistakable.
  c) SURPRISE - is it still a surprise? A payoff you saw coming in episode 3 is a failure
     of the plant. 1 = fully telegraphed, 5 = surprising yet fair.
"""


def gen(client, prompt, system, effort="high"):
    r = client.messages.create(
        model=MODEL, max_tokens=16000, system=system,
        thinking={"type": "adaptive"},
        output_config={"effort": effort},
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(b.text for b in r.content if b.type == "text").strip()


def judge(client, system, payload):
    r = client.messages.create(
        model=MODEL, max_tokens=16000, system=system,
        output_config={"effort": "medium",
                       "format": {"type": "json_schema", "schema": JUDGE_SCHEMA}},
        messages=[{"role": "user", "content": payload}],
    )
    return json.loads(next(b.text for b in r.content if b.type == "text"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="print prompts, call nothing")
    ap.add_argument("--out", default="results.json")
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()

    if args.dry_run:
        for s in fx.SCENARIOS[:1]:
            for c in fx.CONDITIONS:
                print(f"\n{'='*70}\n{s['id']} / {c}\n{'='*70}")
                print(fx.plant_prompt(s, c))
        print(f"\n{'='*70}\n18 plants + 18 payoffs + 36 judgements. Roughly $2-3.")
        return

    try:
        import anthropic
    except ImportError:
        sys.exit("pip install anthropic")
    client = anthropic.Anthropic()

    rows = []
    for s in fx.SCENARIOS:
        for c in fx.CONDITIONS:
            print(f"  plant   {s['id']:<10} {c}", flush=True)
            plant = gen(client, fx.plant_prompt(s, c), fx.VOICE)
            print(f"  payoff  {s['id']:<10} {c}", flush=True)
            payoff = gen(client, fx.payoff_prompt(s, plant), fx.VOICE)
            rows.append(dict(scenario=s["id"], condition=c, plant=plant, payoff=payoff))

    # Judge in shuffled order so neither judge can infer condition from position.
    random.Random(args.seed).shuffle(rows)

    for i, row in enumerate(rows, 1):
        print(f"  judge   {i}/{len(rows)}", flush=True)
        row["plant_scores"] = judge(
            client, PLANT_JUDGE, f"--- EPISODE 3 ---\n{row['plant']}")
        row["payoff_scores"] = judge(
            client, PAYOFF_JUDGE,
            f"--- EPISODE 3 ---\n{row['plant']}\n\n--- EPISODE 11 ---\n{row['payoff']}")

    Path(args.out).write_text(json.dumps(rows, indent=2))
    print(f"\nwrote {args.out}  ->  python report.py")


if __name__ == "__main__":
    main()
