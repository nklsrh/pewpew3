#!/usr/bin/env python3
"""Run the plant experiment. See PROTOCOL.md.

Every generation and every judgement is a separate, stateless request. There is no
shared conversation, which is the only honest way to keep the BLIND condition blind.

No API key, no signup:
    python run.py --provider ovh       # ~35 min at 2 RPM, checkpoints as it goes
    python run.py --provider ovh       # re-run to resume where it stopped

With a key:
    ANTHROPIC_API_KEY=... python run.py --provider anthropic
    GROQ_API_KEY=...      python run.py --provider groq
"""
import argparse
import json
import random
import sys
from pathlib import Path

import fixtures as fx
import providers

ANTHROPIC_MODEL = "claude-opus-5"

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "scores": {
            "type": "object",
            "properties": {k: {"type": "integer", "minimum": 1, "maximum": 5}
                           for k in ("a", "b", "c")},
            "required": ["a", "b", "c"], "additionalProperties": False,
        },
        "note": {"type": "string"},
    },
    "required": ["scores", "note"], "additionalProperties": False,
}

JSON_TAIL = ('\n\nReply with ONLY this JSON, nothing else:\n'
             '{"scores": {"a": <1-5>, "b": <1-5>, "c": <1-5>}, "note": "<one sentence>"}')

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
     1 = one rigid reading, 5 = many live options."""

PAYOFF_JUDGE = """\
You are judging a pair of scenes from a pulp heist game: episode 3, then episode 11, where
something planted earlier detonates.

Score 1-5:
  a) EARNED - does the detonation feel set up by episode 3, or arbitrary and bolted on?
     1 = came from nowhere, 5 = inevitable in hindsight.
  b) RECALL - is the planted element specific enough that a player would actually remember
     it eight episodes later? 1 = forgettable detail, 5 = unmistakable.
  c) SURPRISE - is it still a surprise? A payoff you saw coming in episode 3 is a failure
     of the plant. 1 = fully telegraphed, 5 = surprising yet fair."""


class Anthropic:
    name = "anthropic"

    def __init__(self):
        import anthropic
        self.c = anthropic.Anthropic()

    def write(self, system, prompt):
        r = self.c.messages.create(
            model=ANTHROPIC_MODEL, max_tokens=16000, system=system,
            thinking={"type": "adaptive"}, output_config={"effort": "high"},
            messages=[{"role": "user", "content": prompt}])
        return "".join(b.text for b in r.content if b.type == "text").strip()

    def judge(self, system, prompt):
        r = self.c.messages.create(
            model=ANTHROPIC_MODEL, max_tokens=16000, system=system,
            output_config={"effort": "medium",
                           "format": {"type": "json_schema", "schema": JUDGE_SCHEMA}},
            messages=[{"role": "user", "content": prompt}])
        return json.loads(next(b.text for b in r.content if b.type == "text"))


class OpenAICompat:
    def __init__(self, name):
        self.name = name

    def write(self, system, prompt):
        return providers.call(self.name, system, prompt, max_tokens=1200)

    def judge(self, system, prompt):
        raw = providers.call(self.name, system + JSON_TAIL, prompt,
                             max_tokens=600, temperature=0.0)
        return providers.extract_json(raw)


def key(row):
    return f"{row['scenario']}/{row['condition']}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", default="ovh",
                    choices=["ovh", "llm7", "groq", "anthropic"])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out", default=None,
                    help="default: results-<provider>.json, so parallel runs "
                         "on different providers never overwrite each other")
    ap.add_argument("--rpm", type=float, default=None,
                    help="override the provider's request rate")
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()

    if args.dry_run:
        for s in fx.SCENARIOS[:1]:
            for c in fx.CONDITIONS:
                print(f"\n{'='*70}\n{s['id']} / {c}\n{'='*70}")
                print(fx.plant_prompt(s, c))
        print(f"\n{'='*70}\n18 plants + 18 payoffs + 36 judgements = 72 calls.")
        caps = {"llm7": "60 req/hour cap - needs two sittings"}
        for n, p in providers.PROVIDERS.items():
            note = caps.get(n, "no key" if not p["key_env"] else p["key_env"])
            print(f"  {n:<10} {p['rpm']:>4g} RPM -> ~{72/p['rpm']:.0f} min   {note}")
        return

    if args.rpm and args.provider != "anthropic":
        providers.set_rpm(args.provider, args.rpm)
    backend = Anthropic() if args.provider == "anthropic" else OpenAICompat(args.provider)

    out = Path(args.out or f"results-{args.provider}.json")
    rows = json.loads(out.read_text()) if out.exists() else []
    done = {key(r): r for r in rows}
    if done:
        print(f"resuming: {len(done)} scenes already written")

    def save():
        out.write_text(json.dumps(rows, indent=2))

    stalled = 0

    for s in fx.SCENARIOS:
        for c in fx.CONDITIONS:
            k = f"{s['id']}/{c}"
            if k in done and done[k].get("payoff"):
                continue
            print(f"  write {k}", flush=True)
            try:
                plant = backend.write(fx.VOICE, fx.plant_prompt(s, c))
                payoff = backend.write(fx.VOICE, fx.payoff_prompt(s, plant))
            except providers.RateLimited as e:
                stalled += 1
                print(f"    rate limited: {e}")
                if stalled >= 3:
                    print("\n  Three scenes rate-limited in a row - the free pool is "
                          "saturated.\n  Stopping. Progress is saved; re-run later to "
                          "resume, or try\n  --provider groq (free key, 30 RPM) or "
                          "--rpm 0.5 to go slower.")
                    save()
                    return
                continue
            except RuntimeError as e:
                print(f"    failed: {e} - skipping, re-run to retry")
                continue
            stalled = 0
            row = dict(scenario=s["id"], condition=c, plant=plant, payoff=payoff,
                       writer=args.provider)
            rows.append(row)
            done[k] = row
            save()

    # Judge in shuffled order so neither judge can infer condition from position.
    order = list(rows)
    random.Random(args.seed).shuffle(order)
    for i, row in enumerate(order, 1):
        if row.get("payoff_scores"):
            continue
        print(f"  judge {i}/{len(order)}  {key(row)}", flush=True)
        try:
            row["plant_scores"] = backend.judge(
                PLANT_JUDGE, f"--- EPISODE 3 ---\n{row['plant']}")
            row["payoff_scores"] = backend.judge(
                PAYOFF_JUDGE,
                f"--- EPISODE 3 ---\n{row['plant']}\n\n--- EPISODE 11 ---\n{row['payoff']}")
        except (ValueError, RuntimeError) as e:
            print(f"    judge failed ({e}) - left unscored, re-run to retry")
        save()

    unscored = [key(r) for r in rows if not r.get("payoff_scores")]
    missing = 18 - len(rows)
    save()
    print(f"\nwrote {out}  ({len(rows)}/18 scenes, {len(unscored)} unscored)")
    if missing:
        print(f"  {missing} scenes not written yet - re-run to continue")
    if unscored:
        print(f"  unscored: {', '.join(unscored)}  - re-run to retry")
    print(f"  python report.py {out}     # the verdict")
    print(f"  python readpack.py {out}   # the human read, the one that counts")


if __name__ == "__main__":
    main()
