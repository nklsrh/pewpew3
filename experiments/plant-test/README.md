# Experiment 2 — the plant test

**Question:** can the LLM write a good plant when it doesn't know the payoff?

**Why it matters:** it decides whether the season scheduler can bind payoffs late (flexible,
Score-reactive — the design in dossier §4) or must commit up front (rigid). Architecture
fork, not polish.

Read `PROTOCOL.md` first — it has the conditions, the rubric, and a **pre-registered
decision rule** written before the run so the result can't be rationalised afterwards.

## Run it

```bash
pip install anthropic
export ANTHROPIC_API_KEY=...

python run.py --dry-run     # print prompts, spend nothing
python run.py               # 18 plants + 18 payoffs + 36 judgements, ~$2-3
python report.py            # scores + the decision
python readpack.py          # blinded pairs for a human read
```

## Files

| | |
|---|---|
| `PROTOCOL.md` | Design, rubric, decision rule, threats to validity |
| `fixtures.py` | Six scenarios, the voice brief, and the prompt builders |
| `run.py` | Generation + judging. Every call is stateless and isolated |
| `report.py` | Condition means and the pre-registered verdict |
| `readpack.py` | `readpack.md` (blinded) + `readpack-key.md` |

## Two things to know before trusting the output

**The human read is the real result.** `report.py` is an LLM judging LLM prose — it shares
its own taste, which is exactly the bias that matters here. Read `readpack.md` cold, ideally
with one other person, score it, and only then open the key. If the humans and the table
disagree, the humans are right.

**n=6 per cell buys a direction, not a p-value.** `report.py` prints a CAUTION when any
margin sits within 0.3 of a decision threshold. Honour it — at this sample size that's noise.
