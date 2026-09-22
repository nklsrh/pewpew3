# Experiment 2 — the plant test

**Question:** can the LLM write a good plant when it doesn't know the payoff?

**Why it matters:** it decides whether the season scheduler can bind payoffs late (flexible,
Score-reactive — the design in dossier §4) or must commit up front (rigid). Architecture
fork, not polish.

Read `PROTOCOL.md` first — it has the conditions, the rubric, and a **pre-registered
decision rule** written before the run so the result can't be rationalised afterwards.

## Run it

**No API key, no signup, no pip install** - stdlib only. OVHcloud serves
`gpt-oss-120b` anonymously at 2 requests/minute per IP:

```bash
python run.py --dry-run           # print prompts, spend nothing
python run.py --provider ovh      # 72 calls, ~35 min, checkpoints as it goes
python run.py --provider ovh      # re-run any time to resume where it stopped
python report.py                  # scores + the pre-registered verdict
python readpack.py                # blinded pairs for the human read
```

Every call is checkpointed to `results.json`, so a dropped connection costs one
scene, not the run. Re-running skips finished work.

| `--provider` | Model | Key | Full run |
|---|---|---|---|
| `ovh` (default) | `gpt-oss-120b` | none | ~35 min |
| `llm7` | `gpt-oss:20b` | none | ~7 min, but a 60/hour cap means it needs two sittings |
| `groq` | `gpt-oss-120b` | free `GROQ_API_KEY` | ~2 min |
| `anthropic` | `claude-opus-5` | `ANTHROPIC_API_KEY` | ~$2-3 |

**This will not run from a restricted network.** Both anonymous hosts are blocked
by egress policy in some sandboxes (403 on CONNECT). Run it from your own machine.

## What the free tier does and doesn't answer

Running this on `gpt-oss-120b` answers *"can a cheap open model plant blind?"* - not
*"can the model we ship on plant blind?"* Those come apart if the game ships on a
frontier model.

It is still the more useful question if the game ships on a cheap model, which dossier
risk #4 (cost per session, unmodelled) says is live. A narrative-first game makes a lot
of calls. **If a free model can plant blind, the architecture is safe on any model and
the unit economics get much easier at the same time.** A pass here is strong evidence.
A failure is the weaker result: it would leave open whether a better writer could do it,
and that's the point to re-run with `--provider anthropic`.

`writer` is recorded on every row so results from different models never get mixed.

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
