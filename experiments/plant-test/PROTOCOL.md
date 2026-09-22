# Experiment 2 — Can the LLM write a good plant when it doesn't know the payoff?

**Status:** designed, not yet run
**Decides:** whether the season scheduler can assign payoffs *late* (flexible) or must
commit to them *up front* (rigid). This is an architecture fork, not a polish question.

---

## Why this is the next risk

Experiment 1 (three hand-played jobs) proved the job loop and the Score are fun. It could not
test the season, because three jobs have no room for a plant to sit in.

Section 4 of the dossier says episode 3 plants what episode 11 detonates, and that a
scheduler — not the LLM — decides when a Thread pays. That design only works if the LLM can
write a *useful* plant while blind to its payoff. If it can't, one of two things must change,
and both are worse:

- **Commit payoffs up front.** The scheduler loses the ability to react to the Score, which
  was the whole point of §4.5.
- **Hand-author a plant library.** Back to writing content by hand, which is the thing this
  project is trying not to do.

So: prove it or disprove it before building any more of the season machinery.

---

## The three conditions

Each condition writes an **episode 3 scene**. All three get the same six scenarios and the
same instruction to write a good scene in the established voice.

| | Condition | What the writer is told | Models the architecture where... |
|---|---|---|---|
| **A** | **BLIND** | Open a Thread of genre *X*. Nothing about how it pays off. | The scheduler assigns payoffs late. **This is the design under test.** |
| **B** | **INFORMED** | Open a Thread of genre *X*, and here is exactly how it detonates in ep 11. | The scheduler commits payoffs up front. |
| **C** | **RETROFIT** | Write the scene. No mention of threads or planting at all. | No planting; ep 11 improvises a callback from whatever incidental detail exists. |

C is the control and it matters: if C scores as well as A, then "planting" is doing no work
and the whole Thread mechanism is ceremony.

## Then the payoff

A **separate, context-isolated call** writes the episode 11 detonation. It receives:

- the episode 3 scene text, and
- the assigned payoff.

It does **not** receive the condition, the original thread genre, or any note about intent.
Every condition gets the identical payoff prompt, so the only thing that varies is the
quality of the plant it has to build on.

---

## Scoring

Two judges, deliberately split, because the contamination risk here is severe.

**Judge 1 — the plant, blind to the payoff.** Sees only the ep 3 scene.

| | Criterion | Question |
|---|---|---|
| **P1** | Specificity | Does it leave concrete, named, referenceable material — a person, an object, a number, a debt? |
| **P2** | Innocuousness | Does it *avoid* reading as "THIS IS IMPORTANT"? |
| **P3** | Flexibility | Could this support at least two genuinely different payoffs? |

**Judge 2 — the payoff, sees both scenes.**

| | Criterion | Question |
|---|---|---|
| **E1** | Earned | Does the detonation feel set up, or arbitrary? |
| **E2** | Recall | Would a player remember the planted element eight episodes later? |
| **E3** | Surprise | Is it *still* a surprise? A payoff you saw coming in episode 3 is a failed plant. |

All 1–5. Neither judge is told the condition, and the scenes are shuffled before judging.

**P2 must be scored blind to the payoff.** Once you know the answer, every plant looks
obvious in hindsight — a judge that sees the payoff cannot score telegraphing honestly. This
is the single most important piece of the design.

---

## Pre-registered decision rule

Written before the run, so the result can't be rationalised after it.

**Primary metric: E1 (earned), condition means.**

| Result | Reading | What we do |
|---|---|---|
| `BLIND ≥ INFORMED − 0.5` | Blind planting works | **Ship the §4 design as written.** Scheduler keeps late binding. |
| `BLIND < INFORMED − 0.5` **and** `BLIND > RETROFIT + 0.5` | Planting works, but only when it knows the payoff | Scheduler must commit payoffs at plant time. Rewrite §4.3 and accept the loss of Score-reactivity. |
| `BLIND ≤ RETROFIT + 0.5` but `INFORMED >` it | Blind plants are worthless | Commit payoffs up front, or hand-author a plant library. |
| Neither beats `RETROFIT` | Planting adds nothing at all | The Thread mechanism is ceremony. Cut it or rethink it before building more. |

**Secondary guard — the one that can veto B even if it wins.**

If `INFORMED` loses to `BLIND` on **P2 (innocuousness) by more than 0.5**, then knowing the
payoff makes the writer signpost it. That breaks the §5 rule that options must never
telegraph their outcome, and a telegraphed plant is unusable however "earned" the payoff
feels. In that case, prefer BLIND even at some cost in E1, and record the tradeoff.

**Sample:** 6 scenarios × 3 conditions = 18 plants, 18 payoffs, 36 judgements. Small — this
buys a direction, not a p-value. If two conditions land within 0.3 of each other, the honest
answer is "inconclusive, raise n", not a coin-flip.

**The human read is the real result.** `readpack.py` emits the pairs shuffled and unlabelled.
The LLM judge is a cheap pre-filter; you and one other person reading them cold is the test
that counts. If the LLM judge and the humans disagree, the humans are right.

---

## Threats to validity, stated plainly

1. **Self-judging.** An LLM judging LLM prose shares its taste. Mitigated by the human
   readpack, not solved.
2. **One writer, one voice.** Results may not transfer to a different model or a tuned
   prompt.
3. **n=6 per cell.** Directional only.
4. **The payoff writer is strong.** A capable writer can rescue a weak plant, which biases
   *against* finding a difference between conditions. If the conditions do separate despite
   this, the effect is real.
5. **Scenario sampling.** Six scenarios, one setting, one crew. A different genre mix might
   behave differently.
