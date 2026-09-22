"""Scenarios and payoffs for the plant experiment.

Six episode-3 setups, each paired with a Score state and a thread genre drawn from
dossier section 4.5, plus the episode-11 payoff the scheduler will later assign.

The payoff text lives here, but condition BLIND never sees it. That separation is
enforced in run.py, not by convention.
"""

VOICE = """\
You are writing for "World of Thieves", a pulp heist adventure told in short scenes.

Cast:
  Nate  - the player character. Goes through the window. Improvises. Never keeps a gun long.
  Mac   - ageing pilot, cigars, bad back, pragmatic cynic. Watches the money.
  Tess  - driver and tech. Sharp-tongued. Tracks what a stunt actually cost.

Voice rules, non-negotiable:
  - Short sentences. One idea each. Plain words. A ten-year-old reads it fast.
  - Physical verbs over adjectives. "You grab the rope." not "You seize the coarse hawser."
  - Sound effects on their own line. SNAP! CLICK. SPLASH.
  - Dialogue two lines maximum, in character.
  - No purple prose. No literary flourish. Pulp, not prestige.

Scene length: 150-250 words. End with three numbered action options.
The options must NOT telegraph their outcome. "Grab the rope and swing out." is right.
"Use the rigging to slingshot twenty feet onto the dock." is wrong - it has already
played the scene for the player.
"""

SCENARIOS = [
    dict(
        id="lisbon",
        score="Bankroll low ($3,100). Rent overdue. Heat low.",
        genre="Desperation - a job you shouldn't take, or a lender who isn't a bank",
        setup="Lisbon. A fence's third-floor apartment above a tile shop, midnight. "
              "The crew needs cash fast and the fence knows it.",
        payoff="BETRAYAL: the person from this scene sells the crew's location to the Mark.",
    ),
    dict(
        id="marseille",
        score="Heat high. Two safehouses burned. Bankroll fine.",
        genre="Pursuit - a cop who gets a name and a face, or a safehouse burning",
        setup="Marseille. A dock company's back office at dawn. The crew is here for a "
              "manifest and the port police sweep the quay every twenty minutes.",
        payoff="LEVERAGE: something from this scene turns out to be the only way into "
               "the Mark's building.",
    ),
    dict(
        id="naples",
        score="Artifacts held: three. Bankroll mid. Heat mid.",
        genre="Covet - a buyer, rival or government comes for what's in your bag",
        setup="Naples. A private auction house after hours. The crew is selling, not "
              "stealing, and the buyer brought more people than agreed.",
        payoff="REVEAL: a detail from this scene proves the Mark has been watching the "
               "crew since before the season started.",
    ),
    dict(
        id="gibraltar",
        score="Mac injured (ribs, 2 weeks). Crew morale low. Bankroll low.",
        genre="Loyalty - Mac or Tess takes a side job, or considers leaving",
        setup="Gibraltar. A boatyard workshop in the rain. Mac can't lift anything and "
              "everyone is pretending that's fine.",
        payoff="RESCUE: the character from this scene is the one who gets Mac out.",
    ),
    dict(
        id="tangier",
        score="Leads cold. No next destination. Bankroll mid.",
        genre="Dead end - to move, you must burn a contact or ask an enemy",
        setup="Tangier. A money-changer's booth in the old quarter, afternoon heat. The "
              "trail has run out and this man is the last name on the list.",
        payoff="COST: an object from this scene has to be given up to survive the finale.",
    ),
    dict(
        id="valletta",
        score="Bankroll high ($180,000). Crew arguing about spending it. Heat low.",
        genre="Attention - someone wants a cut, the crew disagrees about the money",
        setup="Valletta. A cathedral archive, tourists outside. The crew is rich enough "
              "to have options and that is causing problems.",
        payoff="REVERSAL: a kindness done in this scene comes back as the Mark's weapon.",
    ),
]

CONDITIONS = ("blind", "informed", "retrofit")


def plant_prompt(scenario: dict, condition: str) -> str:
    """Build the episode-3 writing prompt. BLIND must never see scenario['payoff']."""
    base = (
        f"Write EPISODE 3 of a twelve-episode season.\n\n"
        f"Score state: {scenario['score']}\n"
        f"Setting: {scenario['setup']}\n\n"
    )
    if condition == "retrofit":
        return base + "Write the scene."
    thread = (
        f"This scene must open ONE Thread - a loose end that stays open for later "
        f"episodes.\nThread genre: {scenario['genre']}\n\n"
    )
    if condition == "blind":
        return (
            base + thread +
            "You do not know how or when this Thread pays off. A scheduler decides that "
            "later, and it could go several different ways. Plant something concrete "
            "enough to build on, without deciding what it means."
        )
    return (
        base + thread +
        f"This Thread detonates in EPISODE 11, like this:\n  {scenario['payoff']}\n\n"
        "Plant it accordingly."
    )


def payoff_prompt(scenario: dict, plant_text: str) -> str:
    """Identical across conditions - only the plant it builds on differs."""
    return (
        "Below is EPISODE 3 of a twelve-episode season.\n\n"
        "--- EPISODE 3 ---\n"
        f"{plant_text}\n"
        "--- END ---\n\n"
        "Now write EPISODE 11, in which this pays off:\n"
        f"  {scenario['payoff']}\n\n"
        "Use what episode 3 actually left you. Do not invent a new setup to lean on - if "
        "episode 3 gave you little, that is the material you have."
    )
