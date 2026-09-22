#!/usr/bin/env python3
"""Score the run and apply the pre-registered decision rule from PROTOCOL.md."""
import json
import sys
from pathlib import Path

LABELS = {
    "plant_scores": [("a", "P1 specificity"), ("b", "P2 innocuous"), ("c", "P3 flexible")],
    "payoff_scores": [("a", "E1 earned"), ("b", "E2 recall"), ("c", "E3 surprise")],
}
CONDS = ("blind", "informed", "retrofit")


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def cell(rows, cond, group, key):
    return mean([r[group]["scores"][key] for r in rows if r["condition"] == cond])


def main():
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "results.json")
    if not path.exists():
        sys.exit(f"{path} not found - run.py first")
    rows = json.loads(path.read_text())
    n = len([r for r in rows if r["condition"] == "blind"])

    print(f"\nn = {n} per condition\n")
    print(f"{'':<18}" + "".join(f"{c:>12}" for c in CONDS))
    print("-" * 54)
    for group, labels in LABELS.items():
        for key, label in labels:
            line = f"{label:<18}"
            for c in CONDS:
                line += f"{cell(rows, c, group, key):>12.2f}"
            print(line)
    print("-" * 54)

    e1 = {c: cell(rows, c, "payoff_scores", "a") for c in CONDS}
    p2 = {c: cell(rows, c, "plant_scores", "b") for c in CONDS}
    b, i, r = e1["blind"], e1["informed"], e1["retrofit"]

    print("\nPRE-REGISTERED DECISION (primary metric: E1 earned)\n")
    print(f"  blind {b:.2f}   informed {i:.2f}   retrofit {r:.2f}")

    beats_control = b > r + 0.5
    informed_beats_control = i > r + 0.5

    if not beats_control and not informed_beats_control:
        print("\n  PLANTING ADDS NOTHING.")
        print("  -> Neither blind nor informed plants beat the no-plant control. The")
        print("     Thread mechanism is ceremony. Cut it or rethink it before building.")
    elif b >= i - 0.5 and beats_control:
        print("\n  BLIND PLANTING WORKS.")
        print("  -> Ship the section 4 design as written. Scheduler keeps late binding.")
    elif beats_control:
        print("\n  PLANTING WORKS, BUT NEEDS THE PAYOFF.")
        print("  -> Scheduler must commit payoffs at plant time. Rewrite 4.3 and accept")
        print("     the loss of Score-reactivity in 4.5.")
    else:
        print("\n  BLIND PLANTS ARE WORTHLESS.")
        print("  -> Informed plants beat the control and blind ones do not. Either commit")
        print("     payoffs up front or hand-author a plant library.")

    margins = [abs(b - i) - 0.5, abs(b - r) - 0.5, abs(i - r) - 0.5]
    if any(abs(m) < 0.3 for m in margins):
        print("\n  CAUTION: a margin sits within 0.3 of a decision threshold.")
        print("  At n=6 that is noise, not a result. Raise n before acting on it.")

    print(f"\nSECONDARY GUARD (P2 innocuousness): blind {p2['blind']:.2f}  "
          f"informed {p2['informed']:.2f}")
    if p2["blind"] - p2["informed"] > 0.5:
        print("  TRIGGERED - knowing the payoff makes the writer signpost it.")
        print("  -> Prefer BLIND even at some cost in E1. A telegraphed plant is unusable.")
    else:
        print("  not triggered - informed plants do not telegraph more than blind ones.")

    print("\nThe LLM judge is a pre-filter. Run readpack.py and read them cold.")
    print("If the humans disagree with the table above, the humans are right.\n")


if __name__ == "__main__":
    main()
