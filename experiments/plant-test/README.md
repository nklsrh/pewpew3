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
| `ovh` (default) | `gpt-oss-120b` | none | ~70 min at 1 RPM |
| `llm7` | `gpt-oss:20b` | none | ~7 min, but a 60/hour cap means two sittings |
| `groq` | `gpt-oss-120b` | free key | ~2 min - **the reliable one** |
| `anthropic` | `claude-opus-5` | `ANTHROPIC_API_KEY` | ~$2-3 |

Output goes to `results-<provider>.json`, so two providers can run side by side
without overwriting each other. Pass the file to the other scripts:

```bash
python report.py results-ovh.json
python readpack.py results-llm7.json
```

### When the free pool is saturated

The anonymous tiers are shared, so a 429 on the very first call means somebody else
is using the pool - not that you tripped a limit. The runner honours `Retry-After`,
backs off 15s -> 300s with jitter, and gives up on a scene rather than the run. Three
rate-limited scenes in a row stops it cleanly with everything saved.

If OVH keeps refusing:

```bash
python run.py --provider ovh --rpm 0.5     # slower, more patient
python run.py --provider groq              # free key, 30 RPM, same gpt-oss-120b
```

`groq` needs a free key from console.groq.com but runs the **same model** as OVH, so
it is the same experiment - just one that finishes in two minutes instead of stalling.

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
