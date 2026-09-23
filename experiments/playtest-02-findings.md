# Playtest 02 — the Algeciras session

**Format:** live text play, ~30 beats, played in one sitting.
**Scope:** Act I–III of a season, picking up after the Major Loss at the sunken sub.
**Purpose:** not a scripted experiment. We played, and wrote down what broke.

Every rule below was added to the dossier *because it failed first*. That's the value of the
session: eight of the nine findings are things that went wrong while the game was otherwise
going well, which is exactly the class of problem a design doc doesn't catch by inspection.

---

## Findings, in the order they surfaced

### 1. The supporting cast had no will → **Pillar V, §6.1**
Nate was the only character with agency; the crew commented on decisions rather than
contesting them. The fix wasn't more dialogue — it was that **a push sets the default**. Tess
puts the van in gear and drives north, so silence has a direction and overriding a friend
costs something.

### 2. Passivity was uniformly free → **§6.2 cold push / hot moment**
Once silence was a valid strategy, it was valid *everywhere*, including a standoff. The
legibility fix: **the option list is the cue.** A passive option on the menu means silence is
survivable; no passive option means the scene resolves badly without you.

### 3. Trust had no floor → **§6.5 divergence**
Low trust changed behaviour but nothing else. Now it ends in departure: Tess drove off and
took the van, the scanner, the comms and the only person who knew where Mac was. She
announced nothing. Recovery came later, and the lever was her undisclosed stake — not money.

### 4. The player lost the plot → **§4.8 the stakes clock**
Six strong episodes ran with **no season question ever stated**, exactly the failure §4.2
predicts. Character friction is the most engaging thing in the game and it quietly ate the
spine. Fix: the question lives permanently in the state panel, and a diegetic refresh fires
every 6–8 beats. The delivery that worked was Mac, out of the loop in a cell, being told what
he'd missed — so the player was told too.

### 5. Emergent play outran the schedule → **§4.1 escalation budget**
Tess leaving is a midpoint beat and it fired at episode 4, because trust honestly hit the
floor. Rate-limiting the meters would have broken Pillar V. Rule adopted: **spine beats are
positions, not contents** — whatever the player's play puts in a slot, the next beat is now
whatever tops it.

### 6. The Mark reveal landed flat, twice → **§4.2 the three-job test, then the warm bench**
First attempt: a family met once, offscreen, six weeks earlier. No grip — *what happens if
the player shrugs and goes to Lisbon?* Nothing. Second attempt moved the Mark inside the
player's life (their fence of eight years) and still failed, for a deeper reason: **the
player had never met him.** You cannot spend emotional credit you never banked. Fix: Act I
casts a **warm bench** of 2–3 generous, funny, useful NPCs, played entirely straight, and the
scheduler picks the Mark from that bench late.

### 7. The cold open works → **§4.2, promoted**
A single 200-word Lisbon flashback — a second chair pulled up, eight per cent instead of
nine, a pastry pushed across a counter — recovered the reveal. Player verdict: *"good
recovery tool... interesting enough to keep my attention and pay off."* It is not a weaker
version of seeding but a **compression** of it, because the contrast is instant. Limit: twice
a season, or every kindness starts reading as a countdown.

### 8. Four reveal scenes in a row → **§3 information must be taken, not given**
Mac's call, the case opening, Aurélio's call, Tess's call. All well written, all delivered by
people talking, and the player disengaged. The fix was not shorter dialogue: **nobody had to
do anything to learn any of it.** Every piece of plot should cost something physical. The
strongest beats in both playtests all *generated* story — a collapsing rafter burned the
objective, a kicked winch wrecked the escape, a friend driving off cost the crew its wheels.

### 9. Choice was sprayed evenly → **§3 choice density**
Asking every beat flattened tension; a fake escape-hatch option appeared at a plot-critical
moment one beat after the rule forbidding it was written. Choice density is a dial that
tracks the act, and at critical beats the options go **convergent** — not *whether* to board
the boat, but *how*.

### 10. Tone oscillated → **§5 the tone governor**
Eight grim beats (the story had quietly become the prestige drama Appendix A says v3
rejected), then an over-correction with five jokes at a table where the player was being
threatened. Direction was never the problem; there was no governor. Levity is now a response
to scene tension, with a ceiling of one beat at tension 3+ and a floor of four beats without
lightness.

---

## What held up without changes

- **Pillar I — derailment over failure.** Every loss in this session produced better story
  than the win would have. Losing the wreck to save Mac was the strongest beat in the run.
- **The Score selecting complication genre (§4.5).** Trust falling drove the entire middle of
  the session without being steered.
- **Rook's 3-state arc (Pillar III).** It jumped six episodes early because the game needed
  somebody in the passenger seat after Tess left — and that was *correct*, which is the
  escalation-budget rule working before it was written.
- **The Major Loss carry-over.** Injuries and a lost sidearm from the previous session were
  still shaping choices hours later.

## Still untested

- Whether any of this survives a **second** season.
- Whether an LLM can hold the tone governor and the stakes clock **without a human noticing
  the drift and saying so** — which is what happened here, every single time.
- The plant experiment (`experiments/plant-test/`) — still unrun.
