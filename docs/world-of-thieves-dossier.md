# World of Thieves — Product Dossier

**Status:** exploratory design, pre-prototype
**Working logline:** *A next-generation swashbuckling adventure that blends high-stakes thieving with ever-changing, character-driven storylines.*
**Format target:** mobile, portrait, one-handed, 5–10 minute sessions
**Author:** Nik · **Collaborator:** LLM design partner · **Date:** 2026-09-22

---

## 0. How to read this

Section 1 is the pitch you can send a friend cold. Section 2 is the honest record of
how we got here — including the three versions of this idea we killed, and why. Sections
3–7 are the actual design. Section 8 is what we don't know yet. Section 9 is what to build first.

---

## 1. The one-pager (shareable)

You are **Nate**, the guy who goes through the window. **Mac** is the ageing pilot in the
van who tracks the money and complains about his back. **Tess** drives, hacks, and tells
you when a stunt costs more than it earns.

Each job is a short, readable, choice-driven heist scene: you pick simple physical actions
(*kick the stool*, *grab the rope*, *slide*), and the scene reacts with pulp-action physics —
things break, alarms trip, ceilings collapse. Jobs run 3–5 minutes.

Nothing ever ends in "Game Over". Every job settles into a **Ledger**: cash, injuries,
police heat, burned clients, stolen artifacts, and new leads. A botched job doesn't restart —
it *bends the story*. You lose the prize, your rival takes it, your pilot ends up in a police
cell on an oxygen drip, and the next job becomes a jailbreak you never planned.

Recurring characters remember. **Rook** — a competitor with worse luck and worse bosses —
starts as an obstacle, comes back with a sling and a grudge, beats you once, and eventually
gets burned by his own employer badly enough that you have to work with him.

**Why it's new:** an LLM runs the world state, the rivals, and the consequences — not the
combat. The mechanics stay tight and deterministic; the *story around them* is what evolves,
run over run, into something that feels authored.

---

## 2. Design history — what we killed and why

The idea went through four versions. The dead ones matter, because each one died of a
specific, nameable flaw.

### v1 — "The Rogue's Hoard": Hitman + Uncharted, LLM narrates combat in real time
**Killed by latency.** Real-time action resolves in milliseconds; an LLM call takes 0.5–2s.
Narration generated mid-fight is either an unreadable text spew during a brawl, or a pause
that kills the game feel. Nobody reads prose while dodging.

**Kept from it:** the Hoard→difficulty scaling idea, and Scars as permanent narrative
consequences. Both survive into the Ledger.

### v2 — "Rogue's Ledger": turn-based node stealth, LLM as adversarial DM
Better — LLM moved out-of-band to briefing/debrief. But the competitive scan showed the
shape of the trap:

| Reference | Lesson |
|---|---|
| **Nemesis System** (Shadow of Mordor) | Grudges only land if the player *remembers the failure that caused them*. Also: WB patented the architecture; an LLM state layer sidesteps the hardcoded trees. |
| **Invisible, Inc.** | Gold standard for turn-based heist tension — built from strict resource limits and vision cones, with near-zero narrative. |
| **AI Dungeon / AI Roguelite** | The cautionary tale. When the LLM computes outcomes, players realise there are no rules and stop caring. "Squishy." |
| **Shadows of Doubt** | Deep procedural simulation, but the dialogue/narrative is static and formulaic. The gap is real. |

**The identified wedge:** nobody has shipped *strict deterministic mechanics* + *an LLM
operating strictly out-of-band* to drive rivalries, contracts, and consequences.

### v3 — "Breach & Clear": kinetic greybox brawler, LLM as Director issuing rule changes
This came from an honest skills audit:

- **Strong at:** tight, visceral moment-to-moment feel — hitting, shooting, sliding, kicking, throwing.
- **Weak at:** systems thinking, procedural design, narrative authoring.
- **Constraint:** solo dev.
- **Success condition:** *something I'd actually want to play every day.*

v1 and v2 were 90% the things the audit says to avoid. v3 corrected hard toward the strength —
but two objections landed:

1. **"Don't want an arcade game with a light LLM wrapper."** A post-run radio bark is a
   soundboard, not a design. We fixed this by giving the LLM *mechanical leverage*: narrative
   edicts that flip hard binary rules ("No sliding", "Blackout room", "Melee only").
2. **"Micro-hazards won't read on a phone screen."** Correct — tripwires and floor spikes
   are unreadable clutter at 6 inches. That's why edicts became full-screen, high-contrast
   *rules*, not environmental detail.

**Also killed here:** the LLM-as-Handler persona. Too serious, too much of a backseat
driver, and a tired trope. Tone brief replaced it: *Uncharted / Firefly* — a rag-tag crew
who don't take themselves seriously, where watching the world get fleshed out is the pleasure.

### v4 — "World of Thieves" (current)
Narrative-first. Playtested live, over several scenes, and it held attention through three
full jobs — which is the strongest signal in this entire document.

**The reframe that unlocked it:** the LLM is not a commentator on the action. It is the
*showrunner* of a pulp adventure serial, and the action beats are the set pieces.

---

## 3. Design pillars

### Pillar I — Derailment over failure
No Game Over screen. Every beat has a **mishap**: a snapped rafter, a jammed gun, a keel
giving way, a bought-off mechanic. Bad outcomes bend the world instead of resetting it.
Failure is *content*, not punishment — which is also why it's funny rather than frustrating:
when you break the chandelier, Mac yells at you, and that's half the appeal.

### Pillar II — The Living Ledger
Every job settles into four persistent meters:

| Meter | What it does |
|---|---|
| **Bankroll** | Cash. Buys gear, bribes, medics, safehouses. Running dry forces low-rent, dangerous side hustles. |
| **Crew state** | Mac and Tess's health + morale. Injuries remove capabilities (Mac with the bends = no muscle, no pilot, for 48h). |
| **Heat** | Police and syndicate attention. Burns routes, raises bribe costs, seeds ambushes. |
| **Leads & artifacts** | Physical breadcrumbs — a medal inscription, a logbook, a decoder — that unlock the next destination. |

### Pillar III — Recurring characters on a 3-state track
Rivals aren't boss fights; they're episodic continuity. The Rook template:

```
STATE 1 — THE ACCIDENT
  Shows up as an obstacle. Gets physically wrecked by a player stunt.
  (Florence: took a rafter to the collarbone.)

STATE 2 — THE GRUDGE, AND THE WIN
  Returns visibly changed — sling, bandages, a counter-plan.
  CRITICAL: he wins this one. Player is disarmed, robbed, left in the water.
  The player must feel the underdog flip.

STATE 3 — THE TWIST
  Burned by his own boss. Becomes an uneasy, comedic ally against a bigger threat.
```

**The key playtest discovery is in State 2.** In the original draft the player shot Rook and
won; that made him a punchline. Rewriting it so the black-market .45 *jams* and Rook walks
away with the prize is strictly better story. **Design rule: the rival must beat you at least
once, and it must be caused by a decision the player already made** (buying cheap gear,
surfacing too fast) — not by a dice roll.

### Pillar IV — Convergent branching
Choices do **not** fan out infinitely. Each regroup option funnels into a *distinct pulp
sub-genre beat*, pre-authored in shape and improvised in detail. Three paths, three genres,
one authored spine.

---

## 4. The loop

```
┌─────────────────────────────────────────────────────┐
│ 1. THE VAN — review Ledger, decode leads, buy kit   │
└──────────────────────────┬──────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────┐
│ 2. THE JOB — 3–4 simple physical choices in a room  │
│    A mishap fires mid-scene. Plan degrades.         │
└──────────────────────────┬──────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────┐
│ 3. SETTLEMENT — Minor Win / Compromise / MAJOR LOSS │
└──────────────────────────┬──────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────┐
│ 4. REGROUP — pick a recovery posture. Funnels into  │
│    a pre-shaped sub-genre beat.                     │
└─────────────────────────────────────────────────────┘
```

### The Major Loss state
A distinct, named, screen-level event — not just a bad settlement. It locks the current
mission track and forces a change in team composition.

```
╔══════════════════════════════════════════════════╗
║                   MAJOR LOSS                     ║
║  Objective: 1938 Rossi Case ......... LOST       ║
║  Casualties: Mac .......... DECOMPRESSION (48h)  ║
║  Assets: sidearm ditched · boat fuel burned      ║
║  Ledger: $12,000                                 ║
╚══════════════════════════════════════════════════╝
```

Regroup options after a Major Loss, and their pre-authored derailments:

| Option | Setup | Pre-authored derailment | Genre it becomes |
|---|---|---|---|
| **Solo infiltration** | Tess stays with Mac; Nate travels alone, unsupported | Rival's syndicate buys off rail security; carriage doors lock mid-journey | Solo survival set piece on a moving train |
| **Two-man sprint** | Pay a local to watch Mac; Tess drives comms | The local sells you out for the police bounty; Mac is arrested on an oxygen drip | Rescue / jailbreak, loyalty test |
| **The long con** | Heal 48h, ambush the handover | The buyer double-crosses the rival and takes the case without paying | Enemy-of-my-enemy buddy comedy |

Every path costs you the original objective and pays you a *better scene*. That's the whole
design in one table.

---

## 5. Voice and readability

The single most useful piece of playtest feedback: **"I'm losing focus — the prose needs to
be basic enough that a 10-year-old reads it fast."**

Style rules, non-negotiable:

- Short sentences. One idea each. Plain words.
- Physical verbs over adjectives. `You grab the rope.` not `You seize the coarse hawser.`
- Sound effects on their own line. `SNAP!` `CLICK.` `SPLASH.`
- Dialogue in two lines max, in character.
- **Options must not telegraph their outcome.** `Grab the rope and swing out.` — not
  `Use the rigging sling to slingshot twenty feet onto the dock.` The second one has already
  played the scene for the player.
- Three options, always. One safe, one aggressive, one greedy/lateral.

Before (too much):
> You vault the railing and clamp your gloved hands onto the severed winch cable. Friction
> screams through your palms as you slide down in a shower of sparks…

After (right):
> You grab the thick rope.
> The heavy boat shifts and falls the rest of the way.
> **SNAP!**
> The rope pulls tight and yanks you into the air.

---

## 6. Cast

| Character | Role | Function in the system |
|---|---|---|
| **Nate** | Player. Athletic, improvisational, allergic to keeping a gun for long. | The body in the room. Relies on momentum and props. |
| **Mac** | Ageing pilot. Cigars, bad back, pragmatic cynic. | Tactical warnings, exits, the moral/physical baseline. **Mac down = no foundation.** |
| **Tess** | Driver, tech, the crew's accountant. | The bottom line. Reminds you when a stunt cost more than it earned. |
| **Rook** | Competitor, not mastermind. Same job, worse bosses, worse luck. | The mirror. Absorbs the blunt trauma the player dodges — until he doesn't. |

---

## 7. The optional kinetic layer

The playtest showed the narrative layer stands on its own — *"I even don't need any real-time
gameplay."* Action beats are therefore an **enhancement, not a dependency**. If built, they
follow this spec:

**Camera:** fixed isometric "diorama" box, one room, no player camera control
(cf. *Bleak Sword*, *Lara Croft GO*). This removes camera collision, orbiting, and clipping
work entirely — the biggest cost saving available to a solo dev.

**Inputs — four verbs, no virtual sticks:**

| Gesture | Action | Feel |
|---|---|---|
| **Tap** target | Strike | Lunge + 3-frame hitstop |
| **Swipe** direction | Slide / dash | Ducks high attacks, trips enemies, 5% camera punch-in |
| **Hold 0.3s + release** | Heavy kick | Launches bodies and props with physics weight |
| **Drag + flick** | Grab & throw | Environmental kills |

**Special:** two-finger tap → 3s slow-mo, taps become instant executions. Charged by clean
hits, slides under attacks, environmental kills.

**Screen layout (portrait):**
```
┌──────────────────────────────────┐
│ [RADIO: MAC] "Don't miss it!"    │  comms banner
├──────────────────────────────────┤
│                                  │
│        isometric diorama         │
│        one room, one frame       │
│                                  │
├──────────────────────────────────┤
│ FOCUS ▓▓▓▓░░              [>]    │  minimal HUD
└──────────────────────────────────┘
```

Every dev hour here goes into hitstop, sound punch, and ragdoll weight — the identified
strength — not into systems.

---

## 8. Open questions and risks

1. **Does the LLM stay on-voice over 20 jobs?** Playtest ran ~4 scenes. Drift, repetition, and
   escalation fatigue are unproven. Mitigation: a tight system prompt plus a hard-authored
   library of mishap *shapes* the LLM dresses rather than invents.
2. **Authoring vs. generation boundary.** Current answer: derailments and regroup beats are
   pre-shaped (authored), prose and dialogue are generated. This line needs defending — it's
   the whole anti-"squishy" defence.
3. **Does the Ledger actually bite?** Cash and injuries must constrain real choices, not just
   decorate the debrief. Untested.
4. **Cost per session.** Narrative-first means many tokens per play session. Unit economics
   unmodelled.
5. **Does the rival track survive repetition?** The 3-state arc is great once. What's State 4,
   and what does the second rival look like without feeling like a re-skin?
6. **Skills mismatch, honestly restated.** The audit said: strong at game feel, weak at systems
   and narrative. v4 is a *narrative-first* game. The counter-argument is that the LLM is
   doing the narrative work and the pre-authored derailment shapes are a small, bounded
   systems job — but this is the load-bearing bet of the project and should be named as such.

---

## 9. What to build first

Build the thing that de-risks #1 and #3 above, and nothing else.

**MVP: a text-first playable, one crew, one campaign arc, three jobs.**

- Web page or Discord bot. No engine, no 3D, no art.
- Scene → three options → outcome → Ledger card. Repeat.
- Ships with: the full Rook 3-state arc, one Major Loss with all three regroup branches
  authored, and the Ledger visibly changing across jobs.
- Persistent state between sessions so "yesterday's defeat" is testable.

**Success criteria (in priority order):**
1. You play it a second day without being asked to.
2. The Ledger changes a decision at least once per session.
3. You remember Rook's name a week later.

**Explicitly not in the MVP:** real-time combat, 3D dioramas, gesture inputs, procedural
mission generation, more than one rival.

If the text version isn't fun to read and replay, no amount of hitstop saves it. If it is,
the kinetic layer becomes a pure upside bet on the strongest existing skill.
