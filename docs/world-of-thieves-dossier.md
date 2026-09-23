# World of Thieves — Product Dossier

**Status:** exploratory design, pre-prototype
**Working logline:** *A next-generation swashbuckling adventure that blends high-stakes thieving with ever-changing, character-driven storylines.*
**Format target:** mobile, portrait, one-handed, 5–10 minute sessions
**Author:** Nik · **Collaborator:** LLM design partner · **Date:** 2026-09-22

---

## 0. How to read this

Section 1 is the pitch you can send a friend cold. Sections 2–7 are the design itself —
pillars, the job loop, the season arc above it, voice, the crew. Section 8 is what we don't know
yet, and Section 9 is what to build first.

Appendix A is the honest record of how we got here: three earlier versions of this idea and
the specific flaw that killed each. It's out of the main line because it's evidence, not
design — but read it before proposing a change, because it's where the dead ends are marked.

---

## 1. The one-pager (shareable)

You are **Nate**, the guy who goes through the window — and the reason you go through it
is that there is something on the other side that nobody has seen in four hundred years. **Mac** is the ageing pilot in the
van who tracks the money and complains about his back. **Tess** drives, hacks, and tells
you when a stunt costs more than it earns.

Each job is a short, readable, choice-driven heist scene: you pick simple physical actions
(*kick the stool*, *grab the rope*, *slide*), and the scene reacts with pulp-action physics —
things break, alarms trip, ceilings collapse. Jobs run 3–5 minutes.

Nothing ever ends in "Game Over". Every job settles into a **Score**: cash, injuries,
police heat, burned clients, stolen artifacts, and new leads. A botched job doesn't restart —
it *bends the story*. You lose the prize, your rival takes it, your pilot ends up in a police
cell on an oxygen drip, and the next job becomes a jailbreak you never planned.

Your crew are not a chorus. They argue, they're often right, and they start moving before
you've decided — so saying nothing is how you end up in someone else's plan. Each of them
wants something from this job they haven't told you.

Recurring characters remember. **Rook** — a competitor with worse luck and worse bosses —
starts as an obstacle, comes back with a sling and a grudge, beats you once, and eventually
gets burned by his own employer badly enough that you have to work with him.

**Everyone in this story wants the same thing.** You want the artifact. Mac wants the money.
The people shooting at you want it too, for exactly those reasons, and usually with a better
boat. Nobody is here for an ideology. It's a race, and the prize is real.

Bigger prizes need bigger outfits. A townhouse job needs a lockpick; a wreck needs divers,
sonar and a boat you can't afford yet — so the hoard isn't a score, it's **capital**, and what
you can go after next is decided by what you came back with.

Jobs are episodes, and twelve of them make a season: a question posed in the first, a
mandatory gut-punch at the midpoint, a showdown in the twelfth, and a cliffhanger into the
next. What you've done along the way decides which *shape* that showdown takes.

**Why it's new:** an LLM runs the world state, the rivals, and the consequences — not the
combat. The mechanics stay tight and deterministic; the *story around them* is what evolves,
run over run, into something that feels authored.

---

## 2. Design pillars

### What everyone wants

The engine of the whole thing, and it is deliberately simple:

| | Wants | Which means in play |
|---|---|---|
| **Nate** | The artifact. The history. To be the one who found it. | Takes the harder route to the real thing |
| **Mac** | Money | Takes the sure thing, and says so out loud |
| **Tess** | Varies — hers are the personal seasons | The exception that proves the rule |
| **The antagonists** | **Exactly the same things, for the same reasons** | Richer backers, more men, a head start |

**Antagonists are competitors, not ideologues.** They want the treasure. They are better
funded than you. The conflict is a *race*, and that is why it works:

- It passes the menace test automatically — what they take from you is the thing you came for.
- It needs no moral scaffolding, no war crime, no cause. Pulp villains want the gold.
- Nate vs Mac — **wonder against money** — is a permanent, renewable source of friction for the
  Push (§6.1). It never needs inventing; it's in the premise.

Moral weight is allowed, and it rides *on the same object as the payday* (§4.2). It is
seasoning. The moment the treasure stops being worth having, the genre is gone.

**The reframe everything hangs off:** the LLM is not a commentator on the action. It is the
*showrunner* of a pulp adventure serial, and the action beats are its set pieces.

### Pillar I — Derailment over failure
No Game Over screen. Every beat has a **mishap**: a snapped rafter, a jammed gun, a keel
giving way, a bought-off mechanic. Bad outcomes bend the world instead of resetting it.
Failure is *content*, not punishment — which is also why it's funny rather than frustrating:
when you break the chandelier, Mac yells at you, and that's half the appeal.

### Pillar II — The Score
*In heist fiction "the score" is the job you pull. Here it's the running total of what
pulling them has cost and won you — the state the crew carries into the next one.*

Every job settles into four persistent meters:

| Meter | What it does |
|---|---|
| **Bankroll** | Cash. Buys gear, bribes, medics, safehouses. Running dry forces low-rent, dangerous side hustles. |
| **Crew state** | Mac and Tess's health, morale and **trust**. Injuries remove capabilities (Mac with the bends = no muscle, no pilot, for 48h). Low trust is worse: they stop asking and act alone (§6.3). |
| **Heat** | Police and syndicate attention. Burns routes, raises bribe costs, seeds ambushes. |
| **Expedition tier** | What the crew can currently *attempt* — see below. The Score's hardest edge. |
| **Leads & artifacts** | Physical breadcrumbs — a medal inscription, a logbook, a decoder — that unlock the next destination. |

**The expedition tier is what makes the Score bite** (and it is the answer to risk #3, which
said the Score might only decorate the debrief). Bigger treasures need bigger outfits, and
the hoard is the capital that buys them:

| Tier | Needs | What's reachable |
|---|---|---|
| **Street** | Nothing but nerve | A townhouse, a museum case, a private collection |
| **Regional** | A vehicle, a fixer, clean papers | A sealed tomb, a bank vault, a country estate |
| **Expedition** | A boat, divers, sonar, a pilot | A wreck, an island, a jungle site |
| **Deep** | All of it, plus a backer you'll regret | Whatever the season has been pointing at |

Two consequences fall straight out of this:

- **The rival is usually a tier above you.** That is *why* they're ahead, and it's a cleaner
  explanation of villain advantage than competence or cruelty. You beat them by being willing
  to do it with less.
- **A Major Loss can cost you a tier**, and dropping from Expedition to Regional is a
  genuine setback that a cash number alone could never express.

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

### Pillar V — The crew competes for the decision
Supporting characters don't comment on the player's choice, they try to win it. Each one
carries a private reason for being on the job that leaks a sentence at a time under
pressure. Crucially a push **sets the default** — the crew member is already acting, so
doing nothing has a direction and overriding a friend costs trust. Detail in §6.

---

## 3. The loop

```
┌─────────────────────────────────────────────────────┐
│ 1. THE VAN — review the Score, decode leads, buy kit│
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
║  Cash: $12,000                                   ║
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

That's one job. The next section is what twelve of them have to add up to.

### Pacing: choice density is an instrument

How often the player is asked to decide is not a constant. It is a dial, and it should track
the act.

| Where | Choices | Why |
|---|---|---|
| Act I, exploring | Every beat, wide options | The player is establishing who Nate is |
| Escalation | Fewer, sharper, worse | Options narrow as the walls close |
| Climax run | **Several beats with none at all** | Momentum *is* the reward. The game drives; the player holds on |
| The turn | Exactly one, enormous | It lands harder for everything that preceded it |

Asking constantly is the failure mode, and it's a seductive one because choice reads as
respect for the player. It isn't. It **flattens tension** — every beat gets weighted the
same, nothing accelerates, and the player stops being a rogue and becomes a committee.

Two rules:

- **Never offer a choice the plot cannot afford to have refused.** If the story has to reach
  Algeciras, don't ask whether to go. Fake choices are worse than none, and the player always
  smells them.
- **At a plot-critical beat, make the choice convergent.** Not *whether* to board the boat —
  *how*. Up the gangway, around the stern, or straight up the anchor chain all reach the same
  scene, and differ in cost, noise, and what it says about Nate. The player still expresses
  character; the plot still moves. An escape-hatch option among them ("get Mac somewhere safe
  first") reads instantly as the fake it is, and costs more trust than offering nothing would.
- **Earn the big one with silence.** A run of authored beats is what makes the next decision
  feel like a decision. Contrast does the work.

This is the Push (§6.1) at the scale of an act: as tension rises, characters and events take
the decisions, and the player's agency concentrates into fewer, heavier moments rather than
being sprayed evenly across the hour.

### Pacing: information must be taken, not given

The genre is pulp adventure. The moment plot starts arriving by telephone, it stops being
one.

**The revelation budget: two talk beats, maximum, then something physical.** This is the
stakes clock's opposite number and it is needed just as badly — a run of reveals feels
productive while you write it and reads as a radio drama.

The deeper rule, and the one that actually fixes it:

> **Every piece of plot should cost something physical to obtain.**

Compare what the same information costs in each mode:

| Free (weak) | Taken (strong) |
|---|---|
| A crew member explains the convoy on the phone | You dive sixty feet onto the wreck and read it off a locker |
| A fence names the buyer | You break into his shop and find the ledger yourself |
| The case is opened in a car park | The case is opened while someone is kicking the door in |

Both deliver the same fact. Only one is a game. **Information handed over is exposition;
information taken is a scene** — and it carries its own consequences, because taking things
goes wrong, and things going wrong is Pillar I.

Practical tests when a beat is being written:

- **What does the player physically do to learn this?** No answer means it's a phone call.
- **Can this reveal happen *during* an action beat** rather than after it? Learning who
  betrayed you while climbing out of a window is better than being told over coffee.
- **Does the action change the plot, or just decorate it?** The best beats in playtest all
  *generated* story: a rafter collapsed and burned the objective, a kicked winch dropped an
  engine and wrecked the escape, a friend drove off and cost the crew its wheels. None of
  that was planned narrative. It was physics with consequences.

**Playtest note.** This section exists because four reveal scenes ran back to back — all of
them well written, all of them delivered by people talking — and the player disengaged. The
fix was not shorter dialogue. It was that nobody had to *do* anything to learn any of it.

---

## 4. The season arc

Individual jobs with recurring faces are a treadmill. What makes a season of television work
is that episode 3 plants something episode 11 detonates — and the writers knew that in
advance, because they broke the season backwards from the finale.

An LLM improvising job to job can only plan *forwards*. Left alone it drifts, opens more
questions than it closes, and never converges on a showdown. So the season is **authored in
shape and generated in flesh**: deterministic code owns the skeleton and the scheduling,
the LLM owns the content that hangs on it. This is the same authoring/generation boundary
as Pillar I, moved up a level.

### 4.1 Shape of a season

**Twelve jobs, three acts.** Not 22 — this is a mobile game played in 5-minute sessions,
and a thread nobody can remember isn't a thread. Twelve is roughly three weeks of casual play.

```
ACT I — SET UP                    ACT II — TURN              ACT III — CONVERGE
┌───┬───┬───┬───┐            ┌───┬───┬───┬───┐           ┌───┬───┬───┬────┐
│ 1 │ 2 │ 3 │ 4 │            │ 5 │ 6 │ 7 │ 8 │           │ 9 │10 │11 │ 12 │
└─▲─┴───┴───┴─▲─┘            └───┴─▲─┴───┴───┘           └───┴───┴───┴─▲──┘
  │           │                    │                                   │
  PREMIERE    MARK REVEAL          MIDPOINT                            FINALE
  poses the   the season's         mandatory Major Loss;               showdown +
  question    antagonist gets      recontextualises the                the Button
              a face and a name    question. Nothing is
                                   the same after it.
  ── no new threads may open after ep 9. Act III only closes them. ──
```

**Escalation budget.** The fixed slots assume escalation arrives on schedule. Emergent play
does not respect that — the Score can drive a finale-grade event into Act I, and then Act II
has nothing left to spend. In playtest, a crew member walked out at episode 4 because trust
hit the floor honestly; that is a midpoint beat at minimum.

Two ways to handle it, and only one of them is right:

| | What it does | Verdict |
|---|---|---|
| **Rate-limit escalation** | Cap how far the meters may move before their scheduled beat. | **No.** The meters stop meaning what they say, and Pillar V only works because they bite. |
| **Re-baseline** | Promote the emergent event into the slot it earned, and raise everything after it. | **Yes.** Harder to write, keeps the player's momentum, keeps the meters honest. |

So the rule is: **the spine's beats are positions, not contents.** If the player's own play
fills the midpoint slot early, the midpoint is now whatever tops it — and the scheduler's job
is to find that, not to hold the player back to protect a plan.

Four **fixed beat slots** — premiere, Mark reveal, midpoint, finale. The other eight episodes
are variable and chosen at runtime (§4.4). The fixed slots are what guarantee convergence;
without them you have a soap opera that never ends.

### 4.2 The season question

Every season poses exactly one question in episode 1 and answers it in episode 12.

> *Season 1: who burned the Medici job, and why do they want the Rossi convoy?*

The question must be (a) answerable with a person, (b) something the crew can be hurt by,
and (c) phrased so the player can say it out loud after two episodes. If the player can't
state the season question, the season has failed regardless of how good the jobs were.

**The menace test.** A Mark is frightening in proportion to what they can take *from the
player*, not to what they have done to strangers. Braga in playtest was polite, patient and
well-motivated, and landed as *mildly interesting* — because his plan destroyed evidence of
a historical crime rather than anything the player wanted or owned. Ask of every Mark: **what
do they take from you in the next hour, and would you miss it?**

**A reveal has to do three things**, and a reveal that only does the third is trivia:

1. **Cost** — it takes something away, or makes something the player already did wrong.
2. **Lock** — after it, walking away is not available. A villain the player can simply
   decline is not a Mark, it's a news item.
3. **Recontextualise** — an earlier scene now means something different.

The test for #2 is blunt: *what happens if the player shrugs and goes to Lisbon instead?*
If the answer is "nothing much", the reveal has failed regardless of how clever it is.
Distance is what kills it — a faceless institution the player met once, offscreen, six weeks
ago has no grip. **The Mark must already be inside the player's life**: their money, their
fence, their routes, their people.

**The objective must be *wanted*, not merely righteous.** This is a pulp adventure and its
engine is greed plus wonder. A season whose goal is *stop a bad thing* has quietly become a
thriller — the player is no longer chasing treasure, they're doing homework.

The test: **put the greed and the conscience on the same object.** If the thing the villain
destroys on Thursday is *also* the thing worth a fortune, the player wants to get there for
their own reasons and the moral weight rides along for free. If the moral stake replaces the
treasure rather than sitting on top of it, engagement falls off a cliff and the player can't
tell you why.

**Playtest, verbatim:** *"I'm no longer chasing valuable treasure."* The season's object had
become a document proving an 88-year-old crime. Worthy. Not wanted.

**Casting the Mark: warmth is the currency.** A betrayal is a *withdrawal*, and the player
can only lose what they were given. A Mark the player has never liked is a name on a page,
however tightly the plot fits. Distance kills a reveal (above) — but so does a stranger
introduced warmly in the same scene that unmasks them. The affection has to have been
banked in Act I, in scenes with no suspicion in them at all.

This is the plant problem (§4.3) in its hardest form. A plant is one detail; a Mark is
**screen time and affection accumulated across episodes**, and it cannot be retrofitted.

It resolves the same way, and the resolution is the important part:

> **Act I casts a warm bench — two or three recurring NPCs who are generous, funny, and
> genuinely useful. The scheduler picks the Mark from that bench, late.**

Late binding survives, because what is bound late is the *selection*, not the seeding. The
candidates must all be planted early and played straight. Whoever isn't chosen becomes an
ally, a victim, or the person who warns you — so none of the investment is wasted.

Rules for the bench:

- **Played entirely straight.** No hints, no shadow across the face, no ominous line. A
  candidate who reads as suspicious in Act I is spent.
- **Give, don't take.** They do the player favours. Generosity is what the reveal cashes in.
- **At least one scene each where they're simply likeable** and the plot isn't moving.
- **Three candidates minimum**, or the player will guess by elimination.

**The cold open — banking late.** A flashback placed immediately before the withdrawal is a
first-class tool, not a consolation prize. Playtested: an Act-I-less Mark was rescued by one
short scene, and the reveal landed. It isn't a weaker version of seeding — it's a
*compression* of it, and the compression works because the contrast is instant. You meet the
man being kind, and two paragraphs later you learn what he is.

Rules, all of them load-bearing:

1. **Place it right before the reveal cashes it.** Banked early it's just a nice scene;
   banked late it's a detonator.
2. **Physical and small.** One object the player's hands remember — a pastry box, a second
   chair pulled up, eight per cent instead of nine. Not a speech about loyalty.
3. **Give, never take.** The scene's only job is generosity.
4. **One line that is innocent then and unbearable now**, and genuinely innocent on its
   face: *"In ten years you will be very good, and you will remember who was kind to you
   when you were nobody."*
5. **Do double duty.** Bank a second thing while you're in there — the same Lisbon scene
   that establishes the fence can put a woman at the tram stop asking for a light.
6. **Under 200 words**, and no suspicion anywhere in it.

The limit: **twice a season, maximum.** Any more and the player learns that a warm memory is
a fuse, and every act of kindness in the game starts reading as a countdown.

**The Mark** is the answer wearing a face — the season's antagonist. Unlike Rook, the Mark
is not a rival thief; they're the power that's been *using* the crew. They get named in
episode 4 and appear in person no more than three times all season. Scarcity is what makes
a finale feel like a finale.

### 4.2b What a first season is for

A betrayal needs a relationship, and a relationship needs seasons. Season one cannot run the
arc where someone the player loves turns — **there hasn't been time to love anyone.**

| Season | Its actual job |
|---|---|
| **One** | Make the player love the crew. One clean, wanted treasure. A Mark who is an *obstacle*, not an intimate. Warm bench planted and left alone. |
| **Two** | Now the betrayal lands, because the credit exists. The Mark comes off the bench. |
| **Three+** | Consequences of season two. Former crew as rivals (§6.5). |

Getting this wrong is how a first season ends up emotionally flat while every individual
scene works. Playtest: *"I only just learned about these characters so there's no emotional
stakes yet."* Correct, and unfixable from inside that season.

**Leave them wanting more.** The finale should land while the player still has appetite, not
when the arc is exhausted. In playtest the natural ending arrived at roughly beat 20 — the
boat, the collection, the delivery to Lisbon — and everything after it was the season
outstaying its welcome. **Twelve episodes is a ceiling, not a target.** If the material peaks
at eight, the season was eight.

### 4.2c Season types

Most seasons are a race for a prize. Some aren't, and the rotation is what stops twelve
episodes of treasure hunting becoming a format.

| Type | How often | Shape |
|---|---|---|
| **The Treasure** | The default. Most seasons. | Find it before they do. Everyone wants it, nobody has a cause. |
| **The Personal** | Occasionally | The prize matters to one of the crew specifically — their family, their history, their name. That crew member gets the Pushes and the mystery box. |
| **The Rescue** | Occasionally | Somebody is taken. The treasure becomes the ransom, which is a good way to make a payday feel like a loss. |

A Personal or Rescue season should still have a prize worth having. The difference is *who
it's for*, not whether it's worth money.

### 4.3 Threads — the anti-drift device

A **Thread** is a tracked, open narrative obligation. It is the single most important data
structure in the game, because it's what stops the LLM from spraying loose ends.

```
THREAD
  id          t_greasemonkey_debt
  opened      ep 5, Tangier
  involves    Yusuf (mechanic, sold you out)
  stakes      he still has the safehouse address
  pays off as betrayal | leverage | rescue
  due by      ep 9
  status      open | cold | paid
```

The rules are strict, and deterministic code enforces them — not the LLM:

- **The LLM may open a thread. It may not decide when one pays.** A scheduler picks the
  episode. This is the whole trick: improvisation forward, convergence backward.
- **Budget: 5 open threads, maximum.** At the cap, no new thread opens until one closes.
  Sprawl is the failure mode; the cap is the fix.
- **Every thread has a due-by episode.** Past due it goes **cold**, and a cold thread costs
  you something concrete and off-screen — the contact is dead, the leverage is gone, the
  favour was called in by someone else. Cold threads are still *content*; they are never
  silently deleted.
- **No thread opens after episode 9.** Act III is for closing only.

### 4.4 Episode types

Eight of the twelve are chosen at runtime from three types. The mix is fixed; which specific
episode lands where is not.

| Type | Count | Job |
|---|---|---|
| **Spine** | 4 | The fixed beats. Advance the season question. Cannot be skipped. |
| **Thread** | 5 | Pay off a specific open Thread. Chosen by the scheduler from what's open. |
| **Standalone** | 3 | A self-contained job. Earns Score, opens one small Thread, and buys breathing room. |

The standalones are load-bearing, not filler-in-the-bad-sense. Constant escalation is
exhausting, and a clean self-contained heist is where the crew gets to be funny.

### 4.5 How the Score chooses what gets set up next

This is where the meta layer earns its keep. The Score doesn't just tune difficulty — **it
selects the genre of the next complication.**

At each episode boundary, code reads the Score, ranks the pressures, and takes the top one or
two. Those *constrain what kind of Thread the LLM is allowed to open.* Deterministic
selection, generated content.

| Score condition | Pressure | Thread genre it opens |
|---|---|---|
| Bankroll low | Desperation | A job you shouldn't take. A lender who isn't a bank. |
| Bankroll high | Attention | Someone wants a cut. The crew disagrees about spending it. |
| Heat high | Pursuit | A cop who gets a name and a face. A safehouse burns. |
| Heat low | Complacency | You're being set up. The Mark moves where you aren't looking. |
| Crew hurt / low morale | Loyalty | Mac or Tess takes a side job. Someone considers leaving. |
| Crew healthy | Ambition | The crew pushes for a bigger target than you planned. |
| Artifacts held | Covet | A buyer, a rival, or a government comes for what's in your bag. |
| Leads cold | Dead end | To move, you must burn a contact or ask an enemy. |

The consequence is that **two players get structurally different seasons from the same spine.**
The one who hoards artifacts and stays clean gets a season about paranoia and being hunted for
what they own. The one who spends recklessly and draws heat gets a season about desperation
and a cop who won't let go. Same Mark, same finale slot, different show.

### 4.6 Finale modes

The finale is one authored confrontation with the Mark, and the Score you arrive in decides
which *shape* it takes. One antagonist, four finales.

| Arrive as | Finale mode | The shape of it |
|---|---|---|
| Rich, low heat, crew healthy | **The Heist** | You're the aggressor. A planned score against the Mark on your terms. |
| Broke, hunted, crew hurt | **The Last Stand** | Cornered. Survive the night and expose the Mark, because you can't beat them. |
| A crew member lost or held | **The Rescue** | Get them back. The money is explicitly secondary, and everyone says so. |
| Artifacts rich, rival still alive | **The Double-Cross** | A temporary alliance with Rook against the Mark. The question is who turns first. |

**Spine beats cannot be failed out of — only failed forward.** You can't lose your way out of
the finale; a botched finale changes which ending you get and what the Button is, never
whether the season resolves.

### 4.7 The Button, and what survives the season

The finale answers the season question. Then, in the last ninety seconds, it does two things
in a fixed order:

1. **Leaves exactly one Thread deliberately unpaid.** Not forgotten — *visibly* unpaid, on
   screen, acknowledged by the crew.
2. **Opens exactly one new Thread** that reframes the Mark upward: the person you just beat
   was working for someone, and that someone now knows your name.

Carryover into the next season is deliberately uneven, because a game where everything
accumulates forever breaks in season three:

| Carries over fully | Partially resets | Why |
|---|---|---|
| Scars, reputation, rivals, who owes whom | — | This is the accumulated legend. It's the reason to keep playing. |
| — | **Bankroll** | Narratively: you spend it, go to ground, or get robbed in the gap. Keeps the economy from inflating out of tension. |
| — | **Heat** | Decays over the time skip between seasons. A season must be able to start quiet. |

So the thing that actually grows across seasons isn't money — it's **how many people know
your name, and what they want from you.** (This is the Hoard idea from the original pitch,
finally sitting in the right place: legend as the currency, not gold.)

### 4.8 Keeping the player oriented

The failure this prevents is specific and it is not boredom. Character friction is the most
engaging thing in the game, and it will happily eat the season spine while the player is
enjoying it. They look up six beats later holding an object whose purpose they can no longer
remember. **Good scenes are what causes this**, which is why it needs a clock rather than
authorial judgement.

Three tiers, and all three are cheap:

**1. The season question lives in the state panel.** Permanently. Every beat. It costs one
line and it is the difference between a heist and a series of rooms.

**2. "Previously on..." at session start.** Three lines, generated from the Score and the
open Threads.

> *Previously: you took the Rossi case off a sunken sub and lost it to Rook in open water.
> Mac's lungs are still bad. Yusuf has your safehouse address and hasn't used it yet.*

This is the fix for coming back after four days. It doubles as a free drift check: if the
recap reads as three disconnected facts rather than a situation, the season has drifted and
the Thread budget is too loose.

**3. The stakes clock — a mid-session refresh.** Count beats since the player was last told
what is at stake. Past the threshold (**6–8 beats**), the next scene must carry a refresh.

The refresh is **always diegetic**. Never a narrator summary, never a lore panel. It is
delivered by a character with a reason to be saying it right now:

| Delivery vehicle | Why it works |
|---|---|
| **Someone who was out of the loop** | Mac in a cell for a day has to be caught up, so the player gets caught up with him. The best one. |
| **Someone who doesn't know yet** | Explaining to Rook why the case matters is explaining to the player. |
| **Someone who needs convincing** | A fence who won't take the job until he hears what it is. |

The tell that it landed: the character has an *emotional* reason to say it, not an
informational one. Mac isn't reciting background — he's frightened, and he's telling Nate
he is holding something that gets people killed.

> **Mac:** "Alright. Sit down, kid, because you've been running for eleven hours and I don't
> think anybody's told you what you're actually holding."

**Playtest note.** This section exists because the rule in §4.2 got broken in play: six
strong episodes ran with no season question ever stated, and the player lost the plot
exactly as §4.2 predicts. The character work was not the problem. The absence of a spine to
hang it on was.

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

### The release valve

The genre's signature isn't the action, it's the **shrug after the action**. Nate Drake gets
thrown through a window and complains about his back. That tonal snap — violence, then
something absurdly ordinary — is most of what separates this from a thriller.

What worked in playtest:

> Then the deck lights come back on and a Spanish deckhand is standing at the stairwell with
> his hand on the breaker, looking at you, at the man on the floor, at the case on the roof.
>
> You give him three hundred euros. He gives you a cigarette. Nobody says anything about it.

Note what that is and isn't. **Nobody made a joke.** No one was witty. The comedy is that an
ordinary person with a job wandered into a thriller and resolved it commercially.

Five sources, ranked by how well they hold up:

1. **The bystander who doesn't care.** A deckhand, a waiter, a border guard who wants the
   form filled in properly. The world has other people in it and they are unimpressed.
2. **Physical indignity.** Landing badly. Bleeding and not knowing where from. Being dragged
   by the wrong arm.
3. **Competence failure.** Rook changing gear with his knee. Not a gag — a man genuinely
   struggling with a steering wheel and a broken collarbone.
4. **The mundane intruding.** Exact change. A phone at 2%. A shutter that needs two hands.
5. **The complainer.** Mac. Use sparingly; it's the easiest and it wears out fastest.

**Quips are in.** Nate is charming and he knows it — the wisecrack under fire is the genre,
not a concession to it. Slapstick and indignity are the *more durable* of the two, because
they survive repetition where relentless wit doesn't, so lean on them when a run needs
lightness. But a Nate who never quips isn't restrained, he's a different character.

### The tone governor

Levity isn't a rate, it's a *response to tension* — and both failure modes showed up in one
playtest, twenty minutes apart. Eight grim beats, then a corrective scene with five jokes in
it at a table where the player was being threatened. Direction wasn't the problem. The
absence of a governor was.

Track one value per scene — **tension** — and let it set the levity budget:

| Tension | The scene | Levity allowed |
|---|---|---|
| **5** | Someone may die in the next ten seconds | **None.** At most one dry word, from a character, never the narrator |
| **4** | Active danger — a fight, a chase, a threat in the room | One, physical only. An indignity, not a joke |
| **3** | Pressure without violence — a negotiation, an infiltration | One, and best from a bystander or a complainer |
| **2** | Travel, regroup, planning | Two. **This is where quips live** |
| **1** | Aftermath, the settlement | Banter is the point of the scene |

Two hard guards, one at each end:

- **Ceiling — one levity beat per scene at tension 3 or above.** Not three, not five. More
  than one and the threat stops being a threat, which costs the scene the thing it was for.
- **Floor — four consecutive beats with no lightness means drift**, whatever the plot is
  doing. Force one at the next tension drop.

And a craft test that catches the rest: **does the joke cost or reveal anything?** Treading
in a stranger's paella is decoration. A rival complaining about the arm you just dragged him
by is characterisation, consequence and a laugh in one line. Decoration is what makes a scene
feel jokey; the same number of *load-bearing* beats doesn't.

The diagnostic from playtest: the levity wasn't bad writing, it was **tension-2 material
deployed in a tension-4 scene.** Right tool, wrong tier.

### Tonal baseline: adventure, not despair

**The default register is buoyant.** Grimness is a visitor, and it leaves. This is the line
that separates the game from the prestige drama it keeps trying to become — a pull worth
naming, because every individual dark choice is defensible and the cumulative drift is not.

The check is mechanical, like the others: **four consecutive beats with no lightness in them
means the tone has drifted**, whatever the plot is doing.

What holds the baseline:

- **Nate enjoys his job.** He is good at this, he likes being good at it, and he is having a
  better time than the situation warrants. A protagonist who is only ever *reacting* to
  misfortune is a victim, and nobody wants to be one for an hour.
- **Competence is fun to watch.** Show him being excellent at something on purpose, not just
  surviving things that happen to him.
- **The stakes can be heavy. The hour cannot be.** Sunken children, a mentor's betrayal — fine,
  but the scene around them still has a deckhand who wants paying and a rival complaining
  about his arm.

**Playtest note.** This exists because the tone drifted grim over about eight beats — crew
scattered, protagonist passive and haunted — and each step was individually justified. The
story had quietly become the thing §Appendix A says v3 rejected. Watch for it.


Placement rules:

- **On the descent from an action beat**, or the climb into one. Never at the emotional peak
  — it deflates what you just spent.
- **Never on top of a real loss.** Nothing funny in the four beats after a friend drives away.
- **Three sentences, maximum.** It's a breath, not a scene.
- **Understate it and move on.** *"Nobody says anything about it"* is the whole technique.
  The moment the prose acknowledges the joke, it dies.

Before (too much):
> You vault the railing and clamp your gloved hands onto the severed winch cable. Friction
> screams through your palms as you slide down in a shower of sparks…

After (right):
> You grab the thick rope.
> The heavy boat shifts and falls the rest of the way.
> **SNAP!**
> The rope pulls tight and yanks you into the air.

---

## 6. The crew, and the Push

The cast are not commentators. They compete for the decision.

| Character | Role | Undisclosed stake |
|---|---|---|
| **Nate** | Player. Athletic, improvisational, allergic to keeping a gun for long. | — the player supplies it |
| **Mac** | Ageing pilot. Cigars, bad back, pragmatic cynic. | Why he really stopped flying |
| **Tess** | Driver, tech, the crew's accountant. | Why she found Nate in the first place |
| **Rook** | Competitor, not mastermind. Same job, worse bosses, worse luck. | Who actually owns his debt |

### 6.1 The Push

At a decision point a crew member advocates. Three rules make it land:

1. **The argument must be genuinely good.** If the player can dismiss it in one beat,
   there's no tension — it's just flavour with a speech bubble. The crew member should be
   right, or right enough that refusing costs something real.
2. **The push sets the default.** They are *already moving* — van in gear, pistol out, door
   handle in hand. Doing nothing now has a direction.
3. **Overriding costs trust.** Not a scolding. A memory.

Point 2 is the whole mechanic. A neutral three-option menu makes every choice free; a crew
member already driving north makes silence into a decision. The player who taps through
ends up living someone else's plan — and that is a characterisation of Nate, not a
failure state.

> **Tess:** "Ninety minutes. We'll be back by four with something worth trading."
> She pulls onto the road. North. She doesn't ask. She doesn't look over.
>
> `1. Say nothing.   2. "Stop the van."   3. "What's in the case, Tess?"`

### 6.2 Cold push and hot moment

Silence is not always a valid move, and the game has to say which kind of scene the player
is in — without a rule they have to remember.

| | **Cold push** | **Hot moment** |
|---|---|---|
| The scene | A dilemma. A friend who is competent and probably right. | A standoff. Two seconds and a live clock. |
| Doing nothing | **Works.** They're good at this; letting them lead is a real strategy. | **The worst branch.** The clock resolving alone is a loss, not a neutral. |
| What it costs | Relational and identity-level. Never tactical. | Everything on the table. |
| Example | The van pulls north. You say nothing. You reach Casablanca — and earn `Tess: knows you'll fold`. | Tess raises the pistol. Three verbs, no time. |

**The legibility rule: the option list is the cue.** A passive option on the menu means
silence is survivable. No passive option means the scene resolves badly without you. The
player never has to be told which mode they're in — they read it off the verbs.

This is what keeps Pillar V from becoming railroading (risk #10). A cold push is a genuine
invitation to let someone else be right, and a player who takes it is playing well, not
failing. A hot moment simply removes the option rather than punishing it.

### 6.2b Invested characters — the player's debts

The single strongest finding of playtest 02, and it overturns an assumption in this document.

We assumed attachment is *authored* — give a character screen time, charm and a backstory.
It mostly isn't. The character the player cared about was **Rook**, who is a comic nuisance
with a broken collarbone and no backstory at all.

He mattered for exactly one reason: **the player chose to drag him out of a firing line.**

> *"The only person I've got some interest is Rook because I saved him."*

Authored investment is weak. **Investment the player manufactures themselves is strong**, and
it is far cheaper — a single choice, not three episodes of charm.

So the game should manufacture debts on purpose:

- **Offer rescues with a cost.** A character the player could walk past and didn't.
- **Offer mercies.** Someone spared who didn't have to be.
- **Let the player give something away.** Handing Tess the decision at Braga's counter did
  more for that relationship than any dialogue had.
- **Then charge for it.** What the player paid for, they will defend.

**The corollary is the sharpest tool in the box:** *kill what the player chose to save.* It
costs one character and it manufactures a villain instantly, with no warm bench required —
because the hatred is already funded by the player's own earlier choice. A murderer of
someone the player rescued is more menacing on their first appearance than a Mark with three
episodes of seeding.

### 6.3 Undisclosed stakes — the mystery box

Every crew member is on the job for a private reason. It surfaces under pressure and never
all at once.

- **One sentence at a time**, and only when the player presses.
- **Pressing is never free** — it costs time, position, or the moment you had.
- **Never fully answered in the scene where it's asked.** The deflection is the content.
- **The answer is not decided in advance.** It gets built out of what the player presses on,
  which is the same late-binding trick as §4.3 and carries the same risk.

The leak is a correction, a flat delivery, a stop that lands louder than the answer:

> **Tess:** "I need what's in it."
> Beat.
> **Tess:** "*We* need what's in it."

### 6.4 Trust, and the cost of silence

Silence is a choice, and the Score records it — not as a number to optimise, but as
something the crew acts on later:

```
Tess: knows you'll fold
```

Trust has a mechanical floor and ceiling:

| Trust | What the crew does |
|---|---|
| High | They ask, then follow your call. |
| Falling | They ask, then do it their way anyway. |
| Low | **They stop asking.** They act alone, off-screen, and you find out afterwards. |
| Floor | **They leave.** See §6.5. |

A crew that stops asking is how a Major Loss arrives without an enemy in the room.

### 6.5 Divergence — when a crew member leaves

Low trust doesn't only change how a crew member behaves in a scene. Past the floor, **they
leave** — geographically, to go pursue the thing they never told you about.

This is the real teeth behind Pillar V. A crew member is a set of capabilities, and losing
one is a mechanical amputation, not a sad cutscene:

| Gone | What you lose |
|---|---|
| **Tess** | The wheel, the scanner, comms, anything that needs a laptop. No warning before a raid. |
| **Mac** | Exits, aircraft, and the person who tells you the job is a bad idea before you take it. |

Four rules make divergence land rather than just punish:

1. **They don't announce it.** They're gone when you reach for them. The first sign is a van
   that isn't where you left it.
2. **They keep acting off-screen.** They're chasing their own stake, and the world updates
   accordingly — their moves show up in later jobs as changed conditions, closed routes, or
   a person who already has what you came for.
3. **Recovery is offered but never guaranteed.** Reconciliation beats appear on the contract
   board. They can fail, and failing costs you something.
4. **Money is not the lever. Their stake is.** You get a crew member back by serving the
   thing they've been hiding, not by improving the split. Which means you have to have been
   paying attention to the leaks in §6.3.

At the far end, divergence is permanent, and a former crew member is exactly the raw
material the Rook track (Pillar III) is built from: someone who knows your methods, has a
grievance, and wants the same object. **The most dangerous rival in the game should be
someone who used to be in the van.**

### 6.6 The three-way tension

Every good decision point pulls in three directions at once — and a scene that only has one
or two of these is a scene worth rewriting:

```
        what the job needs
                 |
   what the crew wants ——— what Nate can live with
```

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
3. **Does the Score actually bite?** Cash and injuries must constrain real choices, not just
   decorate the debrief. Untested.
4. **Cost per session.** Narrative-first means many tokens per play session. Unit economics
   unmodelled.
5. **Does the rival track survive repetition?** The 3-state arc is great once. What's State 4,
   and what does the second rival look like without feeling like a re-skin?
6. **Does the season actually converge?** The Thread budget, due-by dates and the no-new-threads
   rule after ep 9 are the machinery for it, but all of it is untested. The specific failure to
   watch for: a finale that resolves the season question while three cold threads sit in the
   corner making the whole thing feel unfinished.
7. **Is twelve the right number?** Picked by feel, defended by session length, validated by
   nobody. Too short and the midpoint has no room to land; too long and the player forgets the
   question. Test at six before committing to twelve.
8. **Can the LLM write a planted line it doesn't know the payoff of?** Episode 3 must plant
   something episode 11 detonates. The scheduler knows the payoff; at planting time the LLM
   may not. If plants come out generic, the fix is to hand the LLM the payoff up front and
   trust it not to leak — unproven either way.
9. **Can a mystery box survive being improvised?** §6.2 says the crew's private stakes get
   built from what the player presses on. That's the same late-binding bet as the plant
   problem, with a worse failure mode: a reveal that contradicts an earlier leak is a
   continuity break the player will catch, because they're the one who pressed for it.
   Every leak needs recording as a constraint, not just as prose.
10. **Does the Push read as railroading?** A crew member who sets the default and is usually
   right is one bad tuning pass away from feeling like the game playing itself. The line to
   watch: overriding must be *possible and satisfying*, not just expensive.
11. **Skills mismatch, honestly restated.** The audit said: strong at game feel, weak at systems
   and narrative. v4 is a *narrative-first* game. The counter-argument is that the LLM is
   doing the narrative work and the pre-authored derailment shapes are a small, bounded
   systems job — but this is the load-bearing bet of the project and should be named as such.

---

## 9. What to build first

**Experiment 1 — the job loop — is done and passed.** Three hand-played jobs, all three
interesting, systems honed. The Score and the derailment pillar hold up.

**Experiment 2 is running against risk #8, the plant problem**, because it's the one that
forks the architecture: if the LLM can't plant blind, the scheduler must commit payoffs up
front and §4.5's Score-reactivity dies with it. Protocol and harness in
`experiments/plant-test/`, with a decision rule registered before the run.

After that, build the thing that de-risks #1 and #3, and nothing else.

**MVP: a text-first playable — one crew, one six-episode half-season.**

Six rather than three jobs, and that is a deliberate scope increase over the earlier plan.
Three jobs can't test an arc, and the arc is now the thing most likely to be wrong. Six is
the smallest number that still has a premiere, a midpoint Major Loss, and a finale.

- Web page or Discord bot. No engine, no 3D, no art.
- Scene → three options → outcome → Score card. Repeat.
- Ships with: a stated season question, 3 spine beats + 3 variable episodes, the Thread
  table with budget and due-by enforcement, the full Rook 3-state arc, one Major Loss with
  all three regroup branches authored, and two of the four finale modes.
- Persistent state between sessions, and the "Previously on" recap — it's three lines of
  work and it tests convergence for free.

**Success criteria (in priority order):**
1. You play it a second day without being asked to.
2. You can state the season question out loud after episode 2.
3. The Score changes a decision at least once per session.
4. The finale feels earned by episode 3's plant — not just loud.
5. You remember Rook's name a week later.

**Explicitly not in the MVP:** real-time combat, 3D dioramas, gesture inputs, procedural
mission generation, more than one rival, season two, and all four finale modes.

If the text version isn't fun to read and replay, no amount of hitstop saves it. If it is,
the kinetic layer becomes a pure upside bet on the strongest existing skill.

---

## Appendix A — Design history: what we killed and why

The idea went through four versions. The dead ones matter, because each one died of a
specific, nameable flaw.

### v1 — "The Rogue's Hoard": Hitman + Uncharted, LLM narrates combat in real time
**Killed by latency.** Real-time action resolves in milliseconds; an LLM call takes 0.5–2s.
Narration generated mid-fight is either an unreadable text spew during a brawl, or a pause
that kills the game feel. Nobody reads prose while dodging.

**Kept from it:** the Hoard→difficulty scaling idea, and Scars as permanent narrative
consequences. Both survive into the Score.

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
Narrative-first — everything above. Playtested live over several scenes; it held attention
through three full jobs, which is the strongest signal we have.
