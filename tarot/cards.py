"""
Complete 78-card Rider-Waite Tarot deck with full meanings,
keywords, reversed meanings, and card imagery URLs.
"""

# Image URLs — Rider-Waite deck (public domain, Wikimedia Commons)
_IMG_BASE = "https://upload.wikimedia.org/wikipedia/commons/thumb"

TAROT_DECK = [
    # ------------------------------------------------------------------ #
    #  MAJOR ARCANA (0–21)
    # ------------------------------------------------------------------ #
    {
        "name": "The Fool",
        "number": "0",
        "arcana": "major",
        "suit": None,
        "keywords": ["beginnings", "innocence", "spontaneity", "free spirit"],
        "keywords_reversed": ["naivety", "recklessness", "foolishness", "risk"],
        "meaning_short": "A leap of faith into the unknown. New beginnings beckon.",
        "meaning_upright": (
            "The Fool marks the start of a new journey — unburdened by past experience, "
            "full of optimism and open to possibility. You are being called to step off "
            "the familiar cliff's edge and trust the universe. Take the leap. "
            "Embrace spontaneity and the magic of beginner's mind."
        ),
        "meaning_reversed": (
            "Look before you leap. Reversed, The Fool warns of naivety crossing into "
            "recklessness — risks taken without thought, opportunities squandered through "
            "carelessness. Have you considered the consequences? Pause before you act."
        ),
        "element": "Air",
        "planet": "Uranus",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg",
    },
    {
        "name": "The Magician",
        "number": "I",
        "arcana": "major",
        "suit": None,
        "keywords": ["willpower", "manifestation", "resourcefulness", "power"],
        "keywords_reversed": ["manipulation", "trickery", "wasted potential"],
        "meaning_short": "You have all the tools you need. Channel your will into action.",
        "meaning_upright": (
            "The Magician stands at the altar of creation — before him lie the four suits, "
            "representing all elements at his command. As above, so below: the energy of "
            "the universe flows through you. You have everything required to manifest your "
            "desires. Focus, intention, and action are your instruments."
        ),
        "meaning_reversed": (
            "Power misused, or potential left dormant. Reversed, The Magician may point to "
            "manipulation — yours or another's — or to skills and gifts going to waste. "
            "Are you deceiving yourself about your readiness, or allowing others to deceive you?"
        ),
        "element": "Air",
        "planet": "Mercury",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg",
    },
    {
        "name": "The High Priestess",
        "number": "II",
        "arcana": "major",
        "suit": None,
        "keywords": ["intuition", "mystery", "the subconscious", "inner knowing"],
        "keywords_reversed": ["secrets", "disconnection", "repressed intuition"],
        "meaning_short": "Be still. The answer lives in your silence, not your logic.",
        "meaning_upright": (
            "The High Priestess guards the threshold between conscious and unconscious. "
            "She does not speak — she knows. This is a card of deep intuition and sacred "
            "mystery. Trust the wisdom rising from within you. Not everything needs to be "
            "understood to be real. Sit with the not-knowing."
        ),
        "meaning_reversed": (
            "Something is being hidden — perhaps from you, or by you. Reversed, the High "
            "Priestess points to suppressed intuition, secrets surfacing, or a disconnect "
            "from your inner voice. You may be overriding gut instinct with rationalisation."
        ),
        "element": "Water",
        "planet": "Moon",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/88/RWS_Tarot_02_High_Priestess.jpg",
    },
    {
        "name": "The Empress",
        "number": "III",
        "arcana": "major",
        "suit": None,
        "keywords": ["fertility", "abundance", "nurturing", "nature", "creativity"],
        "keywords_reversed": ["dependence", "smothering", "creative block", "neglect"],
        "meaning_short": "Abundance is yours. Nurture what you're growing.",
        "meaning_upright": (
            "The Empress is the great mother — fertile, abundant, and deeply connected to "
            "the natural world. She governs creativity, sensuality, and the steady unfolding "
            "of growth. What you have been tending is ready to bloom. Lean into pleasure, "
            "beauty, and the patient rhythms of nature."
        ),
        "meaning_reversed": (
            "Creative energy blocked or misdirected. Reversed, The Empress may indicate "
            "smothering others or being smothered, neglecting self-care, or a creative dry "
            "spell. Reconnect with your body, with nature, with the simple act of creating."
        ),
        "element": "Earth",
        "planet": "Venus",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d3/RWS_Tarot_03_Empress.jpg",
    },
    {
        "name": "The Emperor",
        "number": "IV",
        "arcana": "major",
        "suit": None,
        "keywords": ["authority", "structure", "stability", "leadership", "father"],
        "keywords_reversed": ["domination", "rigidity", "control", "inflexibility"],
        "meaning_short": "Build structure. Embrace authority — yours and others'.",
        "meaning_upright": (
            "The Emperor commands from a place of hard-won stability. He is discipline, "
            "strategy, and the architecture of lasting things. This card asks you to lead "
            "with confidence, establish firm foundations, and take responsibility for the "
            "order — or disorder — in your domain."
        ),
        "meaning_reversed": (
            "Control taken too far — or not exercised enough. Reversed, The Emperor may "
            "represent authoritarianism, a domineering figure in your life, or your own "
            "resistance to necessary structure. Examine where power dynamics are out of balance."
        ),
        "element": "Fire",
        "planet": "Aries / Mars",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg",
    },
    {
        "name": "The Hierophant",
        "number": "V",
        "arcana": "major",
        "suit": None,
        "keywords": ["tradition", "institutions", "spiritual wisdom", "conformity"],
        "keywords_reversed": ["rebellion", "subversion", "unorthodoxy", "challenging norms"],
        "meaning_short": "Seek wisdom in tradition — or question it entirely.",
        "meaning_upright": (
            "The Hierophant is the keeper of sacred tradition, spiritual institutions, and "
            "inherited wisdom. He asks: are you drawing on the knowledge of those who came "
            "before? There is wisdom in the established — in ritual, in study, in mentorship. "
            "This may be a time to work within a system, not against it."
        ),
        "meaning_reversed": (
            "The old rules no longer serve you. Reversed, The Hierophant signals a break "
            "from convention — you may be chafing against institutions, organised religion, "
            "or inherited belief systems. This can be liberating or destabilising. Which is it for you?"
        ),
        "element": "Earth",
        "planet": "Taurus",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8d/RWS_Tarot_05_Hierophant.jpg",
    },
    {
        "name": "The Lovers",
        "number": "VI",
        "arcana": "major",
        "suit": None,
        "keywords": ["love", "union", "choices", "alignment", "values"],
        "keywords_reversed": ["disharmony", "imbalance", "misalignment", "bad choices"],
        "meaning_short": "A meaningful choice stands before you. Act from your values.",
        "meaning_upright": (
            "The Lovers are not only about romantic love — they are about the choices that "
            "define us and the unions that reflect our deepest values. What are you choosing "
            "between? This card asks you to align your decisions with who you truly are, "
            "not just what seems convenient."
        ),
        "meaning_reversed": (
            "Disharmony in relationships or within yourself. Reversed, The Lovers points to "
            "choices made from fear or desire rather than values, relationships out of "
            "alignment, or internal conflict between what you want and what you believe."
        ),
        "element": "Air",
        "planet": "Gemini",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/TheLovers.jpg",
    },
    {
        "name": "The Chariot",
        "number": "VII",
        "arcana": "major",
        "suit": None,
        "keywords": ["determination", "control", "victory", "willpower", "direction"],
        "keywords_reversed": ["lack of control", "aggression", "no direction"],
        "meaning_short": "Harness opposing forces and drive forward with iron will.",
        "meaning_upright": (
            "The Chariot is victory won through sheer determination. Two sphinx pull in "
            "opposite directions — yet the charioteer steers them both by will alone. "
            "You are capable of mastering conflicting impulses and external obstacles. "
            "The path ahead demands discipline and forward momentum. Don't brake now."
        ),
        "meaning_reversed": (
            "The reins have slipped. Reversed, The Chariot suggests a loss of control, "
            "aggression untempered by reason, or a journey that has stalled. Are you "
            "forcing things instead of steering them? Check what's pulling you off course."
        ),
        "element": "Water",
        "planet": "Cancer",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9b/RWS_Tarot_07_Chariot.jpg",
    },
    {
        "name": "Strength",
        "number": "VIII",
        "arcana": "major",
        "suit": None,
        "keywords": ["courage", "patience", "compassion", "inner strength", "taming"],
        "keywords_reversed": ["self-doubt", "weakness", "raw emotion", "insecurity"],
        "meaning_short": "True strength is gentle. Tame the beast with compassion, not force.",
        "meaning_upright": (
            "Strength shows a figure closing a lion's jaws — not with brute force, but with "
            "calm, loving authority. Your greatest power lies in patience, courage, and the "
            "ability to meet your own wildness with grace. This is the long game. "
            "Endure with compassion rather than domination."
        ),
        "meaning_reversed": (
            "Inner doubt is louder than your courage right now. Reversed, Strength points "
            "to self-sabotage, raw emotion overwhelming reason, or a situation where you're "
            "forcing instead of flowing. What would change if you softened your approach?"
        ),
        "element": "Fire",
        "planet": "Leo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f5/RWS_Tarot_08_Strength.jpg",
    },
    {
        "name": "The Hermit",
        "number": "IX",
        "arcana": "major",
        "suit": None,
        "keywords": ["solitude", "soul-searching", "introspection", "inner guidance"],
        "keywords_reversed": ["isolation", "loneliness", "withdrawal", "lost"],
        "meaning_short": "Withdraw from the noise. The light you seek is already within.",
        "meaning_upright": (
            "The Hermit climbs the mountain alone, lantern raised — not to show others the way, "
            "but to illuminate his own path. This is a card of deliberate solitude and deep "
            "inner work. Step back from the world's noise. Answers won't come from outside "
            "consultation but from honest time with yourself."
        ),
        "meaning_reversed": (
            "Isolation that has become unhealthy — or a refusal to look inward when you must. "
            "Reversed, The Hermit warns of excessive withdrawal, loneliness mistaken for "
            "wisdom, or avoiding the soul work that's overdue. Are you hiding, or genuinely resting?"
        ),
        "element": "Earth",
        "planet": "Virgo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/RWS_Tarot_09_Hermit.jpg",
    },
    {
        "name": "Wheel of Fortune",
        "number": "X",
        "arcana": "major",
        "suit": None,
        "keywords": ["fate", "cycles", "turning points", "luck", "destiny"],
        "keywords_reversed": ["bad luck", "resistance to change", "breaking cycles"],
        "meaning_short": "The wheel turns. Ride the change — don't grip the spokes.",
        "meaning_upright": (
            "The Wheel of Fortune marks a significant turning point — cycles completing and "
            "beginning, fate in motion. What rises must fall; what falls must rise again. "
            "There's an element of luck here, but also of karma: the wheel turns in response "
            "to everything that has come before. Go with the change, not against it."
        ),
        "meaning_reversed": (
            "Resistance to inevitable change, or a run of misfortune. Reversed, the Wheel "
            "suggests you may be fighting a cycle that must complete, or experiencing the "
            "downturn of a cycle. What patterns are repeating in your life? It may be time to "
            "break them rather than endure them."
        ),
        "element": "Fire",
        "planet": "Jupiter",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg",
    },
    {
        "name": "Justice",
        "number": "XI",
        "arcana": "major",
        "suit": None,
        "keywords": ["fairness", "truth", "law", "cause and effect", "accountability"],
        "keywords_reversed": ["injustice", "dishonesty", "avoidance", "bias"],
        "meaning_short": "Truth and accountability. The scales don't lie.",
        "meaning_upright": (
            "Justice holds sword and scales with equal steadiness. This is the card of "
            "cause and effect, of honest reckoning. A decision or outcome will be fair — "
            "but only if you are honest about all factors involved. Legal matters, "
            "ethical dilemmas, and accountability all fall under this card's domain."
        ),
        "meaning_reversed": (
            "Something is out of balance — and you may know why. Reversed, Justice points "
            "to an unfair outcome, dishonesty (yours or another's), or avoidance of a truth "
            "that needs facing. The scales tip when the weights are wrong. Examine your biases."
        ),
        "element": "Air",
        "planet": "Libra",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/RWS_Tarot_11_Justice.jpg",
    },
    {
        "name": "The Hanged Man",
        "number": "XII",
        "arcana": "major",
        "suit": None,
        "keywords": ["suspension", "surrender", "new perspective", "sacrifice", "waiting"],
        "keywords_reversed": ["stalling", "martyrdom", "indecision", "resistance"],
        "meaning_short": "Hang there willingly. Surrender unlocks the view you need.",
        "meaning_upright": (
            "The Hanged Man dangles from a tree by one foot — yet his face is serene. "
            "This is voluntary suspension: a pause chosen for the sake of a deeper view. "
            "You cannot solve this by pushing harder. Surrender. Let things be upside down "
            "for a while. A new perspective will arrive when you stop struggling."
        ),
        "meaning_reversed": (
            "Stalling when action is needed, or refusing a necessary sacrifice. Reversed, "
            "The Hanged Man suggests you are either martyring yourself for no reason, or "
            "stubbornly refusing the pause that would help you most. Which is it — waiting wisely, or hiding?"
        ),
        "element": "Water",
        "planet": "Neptune / Pisces",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2b/RWS_Tarot_12_Hanged_Man.jpg",
    },
    {
        "name": "Death",
        "number": "XIII",
        "arcana": "major",
        "suit": None,
        "keywords": ["transformation", "endings", "transition", "letting go", "change"],
        "keywords_reversed": ["resistance to change", "stagnation", "fear of endings"],
        "meaning_short": "Something must end for something new to live. Let it go.",
        "meaning_upright": (
            "Death rarely means physical death in a reading — it is the most profound of "
            "transformations, the stripping away of what is no longer needed so that renewal "
            "can occur. What phase of your life is ending? What identity, relationship, or "
            "belief is ready to be composted? This ending is necessary and even sacred."
        ),
        "meaning_reversed": (
            "Clinging to what is already gone. Reversed, Death points to resistance against "
            "an inevitable transformation — fear of letting go keeping you stagnant. "
            "The change will come whether you accept it or not. Consider what you're losing "
            "by refusing to release what's already finished."
        ),
        "element": "Water",
        "planet": "Scorpio / Pluto",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/RWS_Tarot_13_Death.jpg",
    },
    {
        "name": "Temperance",
        "number": "XIV",
        "arcana": "major",
        "suit": None,
        "keywords": ["balance", "moderation", "patience", "alchemy", "integration"],
        "keywords_reversed": ["imbalance", "excess", "lack of long-term vision"],
        "meaning_short": "Blend carefully. The right alchemy requires patience.",
        "meaning_upright": (
            "Temperance shows an angel pouring water between two cups — neither vessel "
            "overflows. This is the card of patient integration, of finding the middle path "
            "that doesn't sacrifice one thing for another. You are in a process of "
            "alchemical refinement. Don't rush it. True synthesis takes time."
        ),
        "meaning_reversed": (
            "Out of balance — too much of something, or a total mismatch of energies. "
            "Reversed, Temperance asks: where are you overindulging or under-investing? "
            "Extremes are costly. What would a more measured approach look like?"
        ),
        "element": "Fire",
        "planet": "Sagittarius",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f8/RWS_Tarot_14_Temperance.jpg",
    },
    {
        "name": "The Devil",
        "number": "XV",
        "arcana": "major",
        "suit": None,
        "keywords": ["bondage", "addiction", "materialism", "shadow self", "patterns"],
        "keywords_reversed": ["releasing chains", "freedom", "reclaiming power", "detachment"],
        "meaning_short": "What has you chained? The chains are looser than they look.",
        "meaning_upright": (
            "The Devil is not an external force — it is the shadow within. The figures "
            "in this card wear chains they could remove, yet they don't. This card speaks "
            "to addiction, unhealthy attachments, materialism, and the lies we tell ourselves "
            "to justify staying in harmful patterns. What have you convinced yourself you can't live without?"
        ),
        "meaning_reversed": (
            "Breaking free from what had you bound. Reversed, The Devil is one of the "
            "more positive reversals — it signals release from addiction, toxic relationships, "
            "or destructive patterns. The chains are loosening. You are beginning to see "
            "your own power to choose differently."
        ),
        "element": "Earth",
        "planet": "Capricorn / Saturn",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/55/RWS_Tarot_15_Devil.jpg",
    },
    {
        "name": "The Tower",
        "number": "XVI",
        "arcana": "major",
        "suit": None,
        "keywords": ["upheaval", "sudden change", "revelation", "chaos", "destruction"],
        "keywords_reversed": ["avoidance of disaster", "delayed upheaval", "internal collapse"],
        "meaning_short": "What is built on false ground will fall. This is grace.",
        "meaning_upright": (
            "The Tower is struck by lightning — its false crown shattered, figures falling "
            "from its heights. This is the card of sudden, unavoidable upheaval. Structures "
            "built on shaky foundations do not survive this force. But there is mercy in "
            "this destruction: what falls was never truly stable. Clearing makes space for the real."
        ),
        "meaning_reversed": (
            "Disaster averted — or merely delayed. Reversed, The Tower may indicate a "
            "near-miss, or a slow-building internal collapse that hasn't yet erupted externally. "
            "It can also suggest resistance to an inevitable dismantling. The longer the fall is "
            "delayed, the harder it lands."
        ),
        "element": "Fire",
        "planet": "Mars",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/53/RWS_Tarot_16_Tower.jpg",
    },
    {
        "name": "The Star",
        "number": "XVII",
        "arcana": "major",
        "suit": None,
        "keywords": ["hope", "renewal", "faith", "healing", "inspiration"],
        "keywords_reversed": ["despair", "hopelessness", "faithlessness", "disconnection"],
        "meaning_short": "After the storm, you are held. Healing is already in motion.",
        "meaning_upright": (
            "The Star follows The Tower — and what a relief it is. A naked figure pours "
            "water in gentle offering, stars blazing above. This is the card of hope after "
            "devastation, of renewed faith in life's goodness. You are being restored. "
            "Trust the healing that is quietly taking place."
        ),
        "meaning_reversed": (
            "Hope feels distant, or faith has run dry. Reversed, The Star points to "
            "despair, disconnection from a sense of purpose, or loss of trust in the future. "
            "This is a gentle card even reversed — it asks you to reconnect with what once "
            "inspired you, even in small ways."
        ),
        "element": "Air",
        "planet": "Aquarius",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/db/RWS_Tarot_17_Star.jpg",
    },
    {
        "name": "The Moon",
        "number": "XVIII",
        "arcana": "major",
        "suit": None,
        "keywords": ["illusion", "fear", "the unconscious", "dreams", "confusion"],
        "keywords_reversed": ["clarity returning", "releasing fear", "unveiling deception"],
        "meaning_short": "Not everything you see is real. Trust your deeper knowing.",
        "meaning_upright": (
            "The Moon illuminates a strange landscape — two howling creatures, a path that "
            "winds into darkness. This is the territory of dreams, illusions, and things "
            "not clearly seen. You may be in a confused or fearful state. The Moon does not "
            "reveal truth clearly — it distorts. Be careful of projections and what hides in shadow."
        ),
        "meaning_reversed": (
            "Light beginning to break through confusion. Reversed, The Moon suggests "
            "illusions dissolving, fears losing their grip, or secrets coming to light. "
            "A period of bewilderment may be ending. Trust your intuition over what you think you see."
        ),
        "element": "Water",
        "planet": "Pisces",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/RWS_Tarot_18_Moon.jpg",
    },
    {
        "name": "The Sun",
        "number": "XIX",
        "arcana": "major",
        "suit": None,
        "keywords": ["joy", "vitality", "success", "optimism", "clarity"],
        "keywords_reversed": ["sadness", "pessimism", "blocked joy", "burnout"],
        "meaning_short": "Bask in this. You have earned the light.",
        "meaning_upright": (
            "The Sun is the most purely joyful card in the Major Arcana. A child rides "
            "triumphantly, sunflowers blazing behind them — this is unguarded happiness, "
            "creative success, and the simple miracle of being alive. Celebrate. "
            "Allow yourself to feel good without looking for what might go wrong."
        ),
        "meaning_reversed": (
            "Joy is present but obscured — or you're refusing to see what's working. "
            "Reversed, The Sun may indicate temporary pessimism, burnout, or a period "
            "where positivity feels forced. The light is still there. What's blocking you from receiving it?"
        ),
        "element": "Fire",
        "planet": "Sun",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/17/RWS_Tarot_19_Sun.jpg",
    },
    {
        "name": "Judgement",
        "number": "XX",
        "arcana": "major",
        "suit": None,
        "keywords": ["rebirth", "reckoning", "awakening", "absolution", "calling"],
        "keywords_reversed": ["self-doubt", "refusing the call", "judgement of others"],
        "meaning_short": "Answer the call. This is your moment of reckoning and renewal.",
        "meaning_upright": (
            "Judgement shows figures rising from coffins as an angel sounds the trumpet — "
            "this is awakening, not punishment. A moment of profound reckoning is at hand. "
            "You are being called to a new level of awareness and accountability. "
            "Forgive what needs forgiving. Rise into who you are becoming."
        ),
        "meaning_reversed": (
            "Refusing the call to rise, or harsh self-judgement blocking growth. Reversed, "
            "Judgement suggests you may be holding yourself back through guilt, fear, or "
            "an inability to forgive yourself or others. The trumpet is sounding. Will you answer?"
        ),
        "element": "Fire",
        "planet": "Pluto",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/RWS_Tarot_20_Judgement.jpg",
    },
    {
        "name": "The World",
        "number": "XXI",
        "arcana": "major",
        "suit": None,
        "keywords": ["completion", "wholeness", "integration", "accomplishment", "travel"],
        "keywords_reversed": ["incompletion", "shortcuts", "delays", "unfinished business"],
        "meaning_short": "You have arrived. Savour the completion before the next cycle begins.",
        "meaning_upright": (
            "The World is the final card of the Major Arcana — a dancer within a wreath of "
            "laurels, held by the four elements. A cycle is complete. You have journeyed "
            "through, learned, endured, and grown. This is not an ending so much as a "
            "wholeness achieved. Celebrate before beginning again."
        ),
        "meaning_reversed": (
            "Something remains unfinished, or you're rushing toward the next thing "
            "without integrating what this one taught you. Reversed, The World asks: "
            "what loose ends are you carrying forward? What would true completion require?"
        ),
        "element": "Earth",
        "planet": "Saturn",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/ff/RWS_Tarot_21_World.jpg",
    },

    # ------------------------------------------------------------------ #
    #  MINOR ARCANA — WANDS (Fire)
    # ------------------------------------------------------------------ #
    {
        "name": "Ace of Wands",
        "number": "Ace",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["new passion", "inspiration", "creative spark", "potential"],
        "keywords_reversed": ["delays", "lack of motivation", "false starts"],
        "meaning_short": "A creative spark ignites. Seize this energy before it fades.",
        "meaning_upright": "The Ace of Wands is pure creative potential — a gift of fire from the universe. A new passion, project, or drive is arriving. The energy is electric and fleeting; channel it into action before the moment passes.",
        "meaning_reversed": "Creative energy blocked or misdirected. A project stalls before it begins, or inspiration arrives but with no clear path. What obstacle is dampening your fire?",
        "element": "Fire",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/11/Wands01.jpg",
    },
    {
        "name": "Two of Wands",
        "number": "2",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["planning", "future vision", "decisions", "expansion"],
        "keywords_reversed": ["fear of the unknown", "bad planning", "playing it safe"],
        "meaning_short": "The world is in your hands. Plan boldly.",
        "meaning_upright": "You stand on the precipice of something big, globe in hand. You have a vision — now comes the planning. Long-range thinking and ambitious decisions are favoured. Don't limit yourself to what's immediately visible.",
        "meaning_reversed": "Fear of expansion keeps you rooted. You may be choosing comfort over possibility, or planning without follow-through. What are you afraid to commit to?",
        "element": "Fire",
        "planet": "Mars in Aries",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Wands02.jpg",
    },
    {
        "name": "Three of Wands",
        "number": "3",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["expansion", "foresight", "enterprise", "progress"],
        "keywords_reversed": ["delays", "obstacles", "lack of foresight"],
        "meaning_short": "Your ships are setting sail. Watch the horizon with patience.",
        "meaning_upright": "The Three of Wands shows early success and the view from higher ground. Things you set in motion are now moving — partnerships, collaborations, and ventures are gaining momentum. Keep watch. Progress is real.",
        "meaning_reversed": "Plans hit unforeseen obstacles or delays. Something that should be moving isn't. Reassess your strategy rather than simply pushing harder.",
        "element": "Fire",
        "planet": "Sun in Aries",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Wands03.jpg",
    },
    {
        "name": "Four of Wands",
        "number": "4",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["celebration", "homecoming", "community", "harmony", "milestone"],
        "keywords_reversed": ["instability at home", "delayed celebration", "conflict"],
        "meaning_short": "Celebrate! A milestone deserves marking.",
        "meaning_upright": "The Four of Wands is the tarot's party card — a moment of genuine celebration, homecoming, and communal joy. A foundation has been built, a milestone reached. Gather your people and let yourself feel proud.",
        "meaning_reversed": "Joy disrupted by conflict at home, or a celebration that feels hollow. Something that should be stable isn't. What's unsettled beneath the surface?",
        "element": "Fire",
        "planet": "Venus in Aries",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Wands04.jpg",
    },
    {
        "name": "Five of Wands",
        "number": "5",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["conflict", "competition", "tension", "disagreement", "chaos"],
        "keywords_reversed": ["avoiding conflict", "resolution", "compromise"],
        "meaning_short": "Competing energies clash. Not all battles deserve your energy.",
        "meaning_upright": "Five figures swing wands at each other — it's chaotic, but no one appears seriously hurt. This is the energy of competition, debate, and productive conflict. You may be in a scrum of competing ideas or personalities. Hold your ground, but choose your battles.",
        "meaning_reversed": "Conflict avoided to the point of stagnation, or a dispute finally resolving. Are you suppressing necessary friction, or finding genuine peace?",
        "element": "Fire",
        "planet": "Saturn in Leo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Wands05.jpg",
    },
    {
        "name": "Six of Wands",
        "number": "6",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["victory", "public recognition", "success", "pride", "acclaim"],
        "keywords_reversed": ["failure", "lack of recognition", "ego inflation"],
        "meaning_short": "Victory lap. You've earned this recognition — receive it.",
        "meaning_upright": "The Six of Wands is a triumphant procession. You have succeeded, and others see it. Accept praise gracefully — you've worked for this. Public recognition, awards, or social validation are likely.",
        "meaning_reversed": "Success delayed, or recognition withheld. You may be chasing external validation at the expense of inner satisfaction. Or pride is curdling into arrogance.",
        "element": "Fire",
        "planet": "Jupiter in Leo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Wands06.jpg",
    },
    {
        "name": "Seven of Wands",
        "number": "7",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["defence", "perseverance", "challenge", "holding your ground"],
        "keywords_reversed": ["giving up", "overwhelm", "exhaustion"],
        "meaning_short": "Hold your position. You have more high ground than you think.",
        "meaning_upright": "A figure defends a hilltop against many opponents. You are being challenged from multiple directions — but you have the advantage of position. Don't concede what you've earned. Perseverance and conviction will see you through.",
        "meaning_reversed": "Exhaustion is real. You may be fighting battles that aren't worth the energy, or surrender is beginning to feel more attractive than it should. Choose your battles more carefully.",
        "element": "Fire",
        "planet": "Mars in Leo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Wands07.jpg",
    },
    {
        "name": "Eight of Wands",
        "number": "8",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["speed", "movement", "swift action", "momentum", "news"],
        "keywords_reversed": ["delays", "frustration", "resisting movement", "haste"],
        "meaning_short": "Move fast. Everything is in motion — don't hesitate now.",
        "meaning_upright": "Eight wands fly through the air with remarkable speed. After a period of waiting, things are suddenly moving very quickly. Act fast, communicate clearly, and don't overthink. This window won't stay open long.",
        "meaning_reversed": "Things are stuck, or moving so fast there's no time to think. Delays frustrate progress. Alternatively — rushing causes errors. Which applies?",
        "element": "Fire",
        "planet": "Mercury in Sagittarius",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Wands08.jpg",
    },
    {
        "name": "Nine of Wands",
        "number": "9",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["resilience", "persistence", "last stand", "defensiveness", "fatigue"],
        "keywords_reversed": ["paranoia", "giving up just before success", "exhaustion"],
        "meaning_short": "Battered but not broken. One more push.",
        "meaning_upright": "The Nine of Wands shows a weary but undefeated figure. You've taken hits. You're tired. But you're still standing — and you are so close to the finish. The strength to continue is already inside you. Hold on.",
        "meaning_reversed": "Either paranoia and hyper-vigilance are wearing you down, or you're abandoning the fight just before the breakthrough arrives. Rest if you must — but don't quit.",
        "element": "Fire",
        "planet": "Moon in Sagittarius",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Tarot_Nine_of_Wands.jpg",
    },
    {
        "name": "Ten of Wands",
        "number": "10",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["burden", "overextension", "responsibility", "struggle", "completion"],
        "keywords_reversed": ["delegation", "release of burden", "collapse under weight"],
        "meaning_short": "You're carrying too much. What can you put down?",
        "meaning_upright": "A figure staggers under the weight of ten wands, back bent, nearly home. You have taken on too much — but the destination is close. Assess what genuinely requires your energy and what you've been carrying out of habit.",
        "meaning_reversed": "Total burnout, or finally releasing a burden. Reversed, this card asks: what are you unable to put down even when it's destroying you? Delegation is not failure.",
        "element": "Fire",
        "planet": "Saturn in Sagittarius",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Wands10.jpg",
    },
    {
        "name": "Page of Wands",
        "number": "Page",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["enthusiasm", "exploration", "discovery", "free spirit", "news"],
        "keywords_reversed": ["immaturity", "lack of direction", "scattered energy"],
        "meaning_short": "Follow the spark. Enthusiasm is its own kind of wisdom.",
        "meaning_upright": "The Page of Wands is pure, unfiltered enthusiasm — a young adventurer ready to chase every exciting thing. New creative ventures, exciting messages, or a burst of inspiration. Don't let 'readiness' stop you from starting.",
        "meaning_reversed": "All spark, no follow-through. Creative energy scattered or immature. Or: a message that's been delayed, or news that disappoints.",
        "element": "Fire",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Wands11.jpg",
    },
    {
        "name": "Knight of Wands",
        "number": "Knight",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["action", "adventure", "impulsiveness", "passion", "drive"],
        "keywords_reversed": ["recklessness", "haste", "scattered", "hot-headed"],
        "meaning_short": "Charge forward — but know where you're going.",
        "meaning_upright": "The Knight of Wands tears across the landscape on a rearing horse, armour flaming. This is passionate, decisive, sometimes reckless action. A drive so strong it can't be stopped. Just make sure the destination is worth the gallop.",
        "meaning_reversed": "Charging headlong into disaster, or all the fire burning out before the task is done. Impulsiveness without strategy. Where is your passion taking you?",
        "element": "Fire",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/16/Wands12.jpg",
    },
    {
        "name": "Queen of Wands",
        "number": "Queen",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["courage", "confidence", "independence", "social", "warmth"],
        "keywords_reversed": ["jealousy", "demanding", "self-centred", "burnout"],
        "meaning_short": "Burn bright. Your confidence and warmth command the room.",
        "meaning_upright": "The Queen of Wands radiates self-assurance — independent, charismatic, and deeply capable. She holds a sunflower because she turns toward light naturally. Lead with warmth. You have the magnetism to bring people to your cause.",
        "meaning_reversed": "Energy turned inward becomes possessiveness or jealousy. Or the fire that usually drives you is simply exhausted. The Queen of Wands reversed can also indicate someone who demands more than they give.",
        "element": "Fire",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Wands13.jpg",
    },
    {
        "name": "King of Wands",
        "number": "King",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["leadership", "vision", "boldness", "entrepreneurship", "honour"],
        "keywords_reversed": ["arrogance", "impulsiveness", "domineering", "unreliability"],
        "meaning_short": "Lead with vision. The King of Wands builds empires from passion.",
        "meaning_upright": "The King of Wands is the visionary leader — bold, charismatic, and willing to take the risks that smaller minds avoid. He sees the big picture and inspires others to follow. Step into that authority. Claim your creative kingdom.",
        "meaning_reversed": "Vision without discipline becomes domination. The reversed King of Wands may be reckless, arrogant, or using force where inspiration would serve better.",
        "element": "Fire",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Wands14.jpg",
    },

    # ------------------------------------------------------------------ #
    #  MINOR ARCANA — CUPS (Water)
    # ------------------------------------------------------------------ #
    {
        "name": "Ace of Cups",
        "number": "Ace",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["new love", "compassion", "creative flow", "emotional awakening"],
        "keywords_reversed": ["emotional blockage", "emptiness", "repressed feelings"],
        "meaning_short": "The heart opens. A new emotional chapter is beginning.",
        "meaning_upright": "The Ace of Cups is an overflow of emotion — love, compassion, creativity, and spiritual connection pouring freely. A new relationship, emotional breakthrough, or creative awakening is arriving. Let it in.",
        "meaning_reversed": "The cup is empty or turned away. Emotional numbness, a blockage in love or creativity, or repressed feelings demanding acknowledgment.",
        "element": "Water",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Cups01.jpg",
    },
    {
        "name": "Two of Cups",
        "number": "2",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["partnership", "mutual attraction", "connection", "unity"],
        "keywords_reversed": ["disconnection", "imbalance", "broken bonds"],
        "meaning_short": "A profound meeting of equals. Honour this connection.",
        "meaning_upright": "Two people exchange cups in a gesture of mutual offering — this is the card of deep partnership, whether romantic, business, or spiritual. A connection of genuine reciprocity. Cherish what is being built.",
        "meaning_reversed": "A partnership out of balance, communication broken down, or a union that has run its course. What has shifted between you?",
        "element": "Water",
        "planet": "Venus in Cancer",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Cups02.jpg",
    },
    {
        "name": "Three of Cups",
        "number": "3",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["friendship", "community", "celebration", "collaboration", "joy"],
        "keywords_reversed": ["overindulgence", "gossip", "isolation", "cliques"],
        "meaning_short": "Your people are your medicine. Celebrate with them.",
        "meaning_upright": "Three figures dance and raise cups in joyful community. This is the card of friendship, celebration, and the nourishment of chosen family. Don't miss the gathering. Show up for the people who show up for you.",
        "meaning_reversed": "Celebration turning into excess, isolation from community, or toxic group dynamics. Are you part of something nourishing or something draining?",
        "element": "Water",
        "planet": "Mercury in Cancer",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Cups03.jpg",
    },
    {
        "name": "Four of Cups",
        "number": "4",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["contemplation", "apathy", "withdrawal", "missed opportunities"],
        "keywords_reversed": ["emerging from apathy", "new motivation", "seizing opportunity"],
        "meaning_short": "A gift is being offered. Look up before it passes.",
        "meaning_upright": "A figure sits beneath a tree, arms crossed, staring at three cups — while a fourth is offered from a cloud above, unnoticed. This is withdrawal, boredom, or apathy causing you to miss what's right in front of you. What are you not seeing?",
        "meaning_reversed": "Emerging from a funk. Motivation and interest are returning. You're beginning to notice opportunities that were there all along.",
        "element": "Water",
        "planet": "Moon in Cancer",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/35/Cups04.jpg",
    },
    {
        "name": "Five of Cups",
        "number": "5",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["loss", "grief", "regret", "disappointment", "mourning"],
        "keywords_reversed": ["acceptance", "moving on", "finding what remains"],
        "meaning_short": "Grieve what's spilled. Two cups still stand behind you.",
        "meaning_upright": "A cloaked figure stares at three spilled cups, oblivious to the two full ones still upright behind them. Loss and grief are real — don't rush past them. But when you're ready, turn around. Not everything is gone.",
        "meaning_reversed": "The worst of grief is passing. You are beginning to release regret and find what still remains. Acceptance is a form of courage.",
        "element": "Water",
        "planet": "Mars in Scorpio",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Cups05.jpg",
    },
    {
        "name": "Six of Cups",
        "number": "6",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["nostalgia", "innocence", "childhood", "reunion", "simplicity"],
        "keywords_reversed": ["living in the past", "naivety", "unrealistic idealism"],
        "meaning_short": "Look to the past for warmth — but don't live there.",
        "meaning_upright": "Two children among cups filled with flowers — a scene of uncomplicated joy and innocence. This card speaks to nostalgia, reunion with people or places from the past, or reconnecting with the part of you that once found joy easily.",
        "meaning_reversed": "Romanticising the past at the expense of the present. Stuck in nostalgia, or returning to something outgrown. The past cannot be your permanent address.",
        "element": "Water",
        "planet": "Sun in Scorpio",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/17/Cups06.jpg",
    },
    {
        "name": "Seven of Cups",
        "number": "7",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["fantasy", "illusion", "wishful thinking", "choices", "daydreaming"],
        "keywords_reversed": ["clarity", "realistic choices", "focus returning"],
        "meaning_short": "So many beautiful options. Which one is real?",
        "meaning_upright": "A figure stands before seven cups filled with fantastical visions — treasures, monsters, castles, serpents. This is the card of too many options, wishful thinking, or being seduced by illusion. Ground yourself before committing to any one path.",
        "meaning_reversed": "The fog is clearing. You can finally see which options are real and which were fantasy. This is a welcome return of discernment.",
        "element": "Water",
        "planet": "Venus in Scorpio",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Cups07.jpg",
    },
    {
        "name": "Eight of Cups",
        "number": "8",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["walking away", "disillusionment", "abandonment", "seeking deeper meaning"],
        "keywords_reversed": ["staying despite unhappiness", "fear of change", "stagnation"],
        "meaning_short": "It takes courage to walk away. The path forward is through leaving.",
        "meaning_upright": "A figure turns their back on eight carefully arranged cups and walks into a dark mountain landscape beneath the moon. Something that once satisfied you no longer does. The emotional journey ahead is unknown, but staying is worse than going.",
        "meaning_reversed": "Staying in a situation out of fear, habit, or sunk-cost thinking. You know you should go — what keeps you?",
        "element": "Water",
        "planet": "Saturn in Pisces",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/60/Cups08.jpg",
    },
    {
        "name": "Nine of Cups",
        "number": "9",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["satisfaction", "contentment", "wish fulfilment", "gratitude", "pleasure"],
        "keywords_reversed": ["overindulgence", "greed", "dissatisfaction", "materialism"],
        "meaning_short": "The wish card. What you've hoped for is within reach.",
        "meaning_upright": "Known as the 'wish card' — a satisfied figure sits before nine cups arranged in triumph. Emotional contentment, satisfaction, and pleasure are yours or arriving. Don't dismiss this moment as luck. You earned this comfort. Enjoy it.",
        "meaning_reversed": "Contentment curdled into complacency or overindulgence. You have what you wanted but it doesn't feel the way you expected. What's missing that material comfort can't provide?",
        "element": "Water",
        "planet": "Jupiter in Pisces",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/24/Cups09.jpg",
    },
    {
        "name": "Ten of Cups",
        "number": "10",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["happy family", "emotional fulfilment", "harmony", "lasting joy"],
        "keywords_reversed": ["broken home", "conflict", "dysfunction", "misaligned values"],
        "meaning_short": "True happiness, shared. This is what it's all for.",
        "meaning_upright": "A family stands beneath a rainbow of cups — this is the card of lasting emotional fulfilment, of love that's become home. Whether literal or metaphorical, the family you've built (chosen or born) is a blessing. Acknowledge it.",
        "meaning_reversed": "Harmony disrupted beneath the surface. A seemingly perfect situation that doesn't match reality. What's broken that needs tending?",
        "element": "Water",
        "planet": "Mars in Pisces",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/84/Cups10.jpg",
    },
    {
        "name": "Page of Cups",
        "number": "Page",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["curiosity", "sensitivity", "emotional messages", "creativity", "wonder"],
        "keywords_reversed": ["emotional immaturity", "creative blocks", "delusion"],
        "meaning_short": "Stay open to the unexpected. Magic arrives in strange vessels.",
        "meaning_upright": "The Page of Cups peers into their cup — from which a fish has unexpectedly appeared. This is sensitivity, wonder, and emotional openness. Creative messages, sweet surprises, and intuitive flashes. Stay curious. Stay soft.",
        "meaning_reversed": "Emotional immaturity or escapism. Or creative energy gone into fantasy rather than expression. Ground your imagination before it disconnects from reality.",
        "element": "Water",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Cups11.jpg",
    },
    {
        "name": "Knight of Cups",
        "number": "Knight",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["romance", "charm", "imagination", "invitation", "following the heart"],
        "keywords_reversed": ["moodiness", "unrealistic", "heartbreak", "manipulation"],
        "meaning_short": "Follow where beauty leads — but keep one eye on reality.",
        "meaning_upright": "The Knight of Cups rides calmly, cup outstretched — this is the romantic idealist, the poet, the seducer of hearts. An invitation, a romantic opportunity, or a creative calling. Follow your heart, but not off a cliff.",
        "meaning_reversed": "Romantic disappointment, emotional manipulation, or someone whose charm conceals self-absorption. Or: your own unrealistic emotional expectations are setting you up for hurt.",
        "element": "Water",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Cups12.jpg",
    },
    {
        "name": "Queen of Cups",
        "number": "Queen",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["compassion", "calm", "empathy", "intuition", "emotional intelligence"],
        "keywords_reversed": ["martyrdom", "insecurity", "emotional manipulation"],
        "meaning_short": "Hold space with compassion — including for yourself.",
        "meaning_upright": "The Queen of Cups holds an ornate, covered cup — her emotional world is vast but contained. She embodies deep empathy, intuitive wisdom, and nurturing calm. This may be a call to care for others — or to let someone care for you.",
        "meaning_reversed": "Empathy turned inward into martyrdom, or emotional manipulation masking as care. Boundaries are as important as compassion. Are you giving from fullness or depletion?",
        "element": "Water",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Cups13.jpg",
    },
    {
        "name": "King of Cups",
        "number": "King",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["emotional balance", "wisdom", "diplomacy", "generosity", "calm authority"],
        "keywords_reversed": ["emotional manipulation", "moodiness", "coldness"],
        "meaning_short": "Lead with the heart, not from it. Wisdom and warmth in balance.",
        "meaning_upright": "The King of Cups sits steady on a churning sea — emotionally attuned and unswayed by the storm around him. He governs with compassion and wisdom. Lead through emotional intelligence. Your steadiness is your strength.",
        "meaning_reversed": "Emotional volatility disguised as control, or coldness masking as wisdom. The King reversed may use emotional intelligence for manipulation. Is someone managing rather than connecting with you?",
        "element": "Water",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/04/Cups14.jpg",
    },

    # ------------------------------------------------------------------ #
    #  MINOR ARCANA — SWORDS (Air)
    # ------------------------------------------------------------------ #
    {
        "name": "Ace of Swords",
        "number": "Ace",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["clarity", "truth", "mental breakthrough", "new ideas", "justice"],
        "keywords_reversed": ["confusion", "brutality", "mental fog", "misinformation"],
        "meaning_short": "A sword of clarity cuts through. Truth arrives sharply.",
        "meaning_upright": "The Ace of Swords is raw intellectual power — a breakthrough, the piercing clarity of truth, the force of a great idea. Use this mental sharpness well. Clarity can cut both ways.",
        "meaning_reversed": "Confusion, misinformation, or an idea used destructively. Clarity is available — but you may be avoiding it. Or: too much mental force being applied where gentleness would serve.",
        "element": "Air",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Swords01.jpg",
    },
    {
        "name": "Two of Swords",
        "number": "2",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["stalemate", "indecision", "blocked emotions", "difficult choices"],
        "keywords_reversed": ["confusion", "information overload", "stalemate broken"],
        "meaning_short": "You're blindfolded at a crossroads. Listen inward.",
        "meaning_upright": "A blindfolded figure holds two crossed swords — a defensive stalemate, neither advancing nor retreating. A decision is being avoided, information is being withheld, or an emotional wall has been erected. The truth won't arrive until you lower the blades.",
        "meaning_reversed": "A stalemate finally broken — but perhaps by force or information arriving messily. The decision can no longer be deferred.",
        "element": "Air",
        "planet": "Moon in Libra",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Swords02.jpg",
    },
    {
        "name": "Three of Swords",
        "number": "3",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["heartbreak", "sorrow", "grief", "loss", "painful truth"],
        "keywords_reversed": ["recovery", "releasing pain", "forgiveness", "optimism"],
        "meaning_short": "This pain is real. Feel it completely — then let it transform you.",
        "meaning_upright": "Three swords pierce a heart — there is no comfortable interpretation here. Heartbreak, grief, and painful truths are at the centre of this card. Do not bypass the hurt. Experiencing it fully is the only path through.",
        "meaning_reversed": "Healing is underway. Grief slowly releasing. Or: holding onto pain past its usefulness. The wound is real, but you don't have to keep reopening it.",
        "element": "Air",
        "planet": "Saturn in Libra",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Swords03.jpg",
    },
    {
        "name": "Four of Swords",
        "number": "4",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["rest", "recovery", "solitude", "contemplation", "retreat"],
        "keywords_reversed": ["restlessness", "burnout", "re-entering the world"],
        "meaning_short": "Rest is not inaction. Withdrawal now is strategy.",
        "meaning_upright": "A knight lies in effigy, swords silent on the wall — this is the rest that precedes action. The Four of Swords commands you to stop, recover, and be still. Mental exhaustion requires genuine retreat, not just a Netflix binge.",
        "meaning_reversed": "Rest interrupted before it's complete, or re-emerging into the world after a healing period. Are you resting deeply enough, or forcing yourself back before you're ready?",
        "element": "Air",
        "planet": "Jupiter in Libra",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Swords04.jpg",
    },
    {
        "name": "Five of Swords",
        "number": "5",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["conflict", "defeat", "betrayal", "winning at a cost", "dishonour"],
        "keywords_reversed": ["reconciliation", "moving past conflict", "regret"],
        "meaning_short": "You may have won. But look at what it cost.",
        "meaning_upright": "A smirking figure gathers swords while defeated opponents walk away. This is victory that comes at the cost of dignity — conflict, betrayal, or a win that tastes hollow. Was it worth it? What are you willing to do to get what you want?",
        "meaning_reversed": "Moving past conflict, seeking reconciliation, or reckoning with the damage done. What needs to be repaired?",
        "element": "Air",
        "planet": "Venus in Aquarius",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Swords05.jpg",
    },
    {
        "name": "Six of Swords",
        "number": "6",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["transition", "moving on", "calm after storm", "travel", "healing"],
        "keywords_reversed": ["stuck in the past", "unable to move on", "rough transition"],
        "meaning_short": "Moving toward calmer waters. The worst is behind you.",
        "meaning_upright": "A ferryman guides two passengers across still water — the turbulent shore recedes behind them. A necessary transition is underway. You are moving from stormy conditions to calmer ones, even if the journey feels slow or reluctant.",
        "meaning_reversed": "Stuck on the shore. Unable or unwilling to leave the turbulence behind. Or: the transition itself is harder than expected, with no calm yet in sight.",
        "element": "Air",
        "planet": "Mercury in Aquarius",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/29/Swords06.jpg",
    },
    {
        "name": "Seven of Swords",
        "number": "7",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["deception", "strategy", "stealth", "cunning", "getting away with it"],
        "keywords_reversed": ["coming clean", "conscience", "caught out", "truth emerging"],
        "meaning_short": "Someone is not being fully honest — including, perhaps, yourself.",
        "meaning_upright": "A figure sneaks away with five swords, leaving two behind — a classic image of deception and strategic cunning. Someone may be withholding information, acting in bad faith, or taking shortcuts. Or: this is you being called to be shrewder in how you navigate a situation.",
        "meaning_reversed": "Secrets surfacing, someone caught in deception, or a guilty conscience demanding honesty. The truth has a way of arriving regardless.",
        "element": "Air",
        "planet": "Moon in Aquarius",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Swords07.jpg",
    },
    {
        "name": "Eight of Swords",
        "number": "8",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["imprisonment", "self-limiting beliefs", "fear", "powerlessness"],
        "keywords_reversed": ["release", "freedom", "seeing clearly", "empowerment"],
        "meaning_short": "The cage is made of thoughts. The door is unlocked.",
        "meaning_upright": "A blindfolded figure stands surrounded by swords, loosely bound — yet they don't move. This is the paralysis of self-limiting beliefs and fear. You have more freedom than you think. The greatest prison is the one you build in your own mind.",
        "meaning_reversed": "Waking from the self-imposed trap. Beliefs are shifting, clarity is arriving, and you are beginning to see options you previously couldn't.",
        "element": "Air",
        "planet": "Jupiter in Gemini",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Swords08.jpg",
    },
    {
        "name": "Nine of Swords",
        "number": "9",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["anxiety", "nightmares", "despair", "worry", "dark night of the soul"],
        "keywords_reversed": ["hope returning", "releasing anxiety", "professional help"],
        "meaning_short": "The 3am thoughts are lying. Morning will come.",
        "meaning_upright": "A figure sits bolt upright in bed, head in hands, swords lining the dark wall. This is the card of anxiety, nightmares, and the distortions that suffering brings at its worst. The fears feel absolute and true — they are not. Reach for help.",
        "meaning_reversed": "Anxiety lifting, hope creeping back. The worst of the night is passing. Seeking support was the right call.",
        "element": "Air",
        "planet": "Mars in Gemini",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Swords09.jpg",
    },
    {
        "name": "Ten of Swords",
        "number": "10",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["painful endings", "betrayal", "deep wounds", "rock bottom", "crisis"],
        "keywords_reversed": ["recovery", "regeneration", "resisting the inevitable end"],
        "meaning_short": "Rock bottom is still ground. And the sky behind you is dawn.",
        "meaning_upright": "A figure lies face down with ten swords in their back — it's bleak, but notice: the sky at the horizon is lightening. This is the card of absolute endings, defeat, and painful betrayal. But the worst is already done. The only direction from here is up.",
        "meaning_reversed": "Resisting an inevitable ending, prolonging the suffering. Or: recovery beginning after a devastating experience. What would it mean to finally accept this is over?",
        "element": "Air",
        "planet": "Sun in Gemini",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Swords10.jpg",
    },
    {
        "name": "Page of Swords",
        "number": "Page",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["curiosity", "wit", "new ideas", "vigilance", "communication"],
        "keywords_reversed": ["gossip", "haste", "deception", "all talk"],
        "meaning_short": "Ask the sharp questions. Truth-seeking is an honourable pursuit.",
        "meaning_upright": "The Page of Swords holds their sword aloft, wind whipping around them — this is the sharp, curious mind, the truth-seeker, the one who asks the uncomfortable questions. Mental agility is your gift. Use it ethically.",
        "meaning_reversed": "Sharp tongue without wisdom. Gossip, manipulation, or ideas that don't make it past talk. Mind the gap between clever and kind.",
        "element": "Air",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Swords11.jpg",
    },
    {
        "name": "Knight of Swords",
        "number": "Knight",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["ambition", "action", "drive", "focus", "fearlessness"],
        "keywords_reversed": ["aggression", "recklessness", "burnout", "rushing"],
        "meaning_short": "Charge with intellect. But check your blind spots first.",
        "meaning_upright": "The Knight of Swords races ahead at full gallop — driven by idea and ambition, unstoppable. This is brilliant, fast, direct action. Just make sure you're charging at the right thing. Speed without direction is just wind.",
        "meaning_reversed": "Aggression or recklessness causing collateral damage. Moving so fast that nothing gets finished, or decisions made without enough thought.",
        "element": "Air",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b0/Swords12.jpg",
    },
    {
        "name": "Queen of Swords",
        "number": "Queen",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["clarity", "directness", "independence", "truth", "keen perception"],
        "keywords_reversed": ["bitterness", "cruelty", "cold", "manipulation"],
        "meaning_short": "See clearly. Speak honestly. Compassion and truth are not enemies.",
        "meaning_upright": "The Queen of Swords sits erect on her throne, sword raised — this is a woman who has known pain and transmuted it into wisdom. She speaks plainly, sees clearly, and holds no illusions. Trust her perception. Emulate her clarity.",
        "meaning_reversed": "Bitterness hardened into cruelty. Sharp perception used as a weapon. Or cold detachment masking grief. What would it cost you to soften without losing your clarity?",
        "element": "Air",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Swords13.jpg",
    },
    {
        "name": "King of Swords",
        "number": "King",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["authority", "intellectual power", "truth", "discipline", "ethics"],
        "keywords_reversed": ["manipulation", "tyranny", "misuse of power", "abuse"],
        "meaning_short": "Command with integrity. The sword of truth is double-edged.",
        "meaning_upright": "The King of Swords commands from a position of intellectual mastery — analytical, principled, and authoritative. His decisions are made from reason and ethics, not emotion. Lead with clear thinking. Be the voice of reason in the room.",
        "meaning_reversed": "Intellectual power used for manipulation, control, or cruelty. A figure who distorts logic to serve their own ends. Or: becoming tyrant to yourself through harsh self-judgement.",
        "element": "Air",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/33/Swords14.jpg",
    },

    # ------------------------------------------------------------------ #
    #  MINOR ARCANA — PENTACLES (Earth)
    # ------------------------------------------------------------------ #
    {
        "name": "Ace of Pentacles",
        "number": "Ace",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["opportunity", "prosperity", "new beginnings", "manifestation"],
        "keywords_reversed": ["missed opportunity", "lack of planning", "greed"],
        "meaning_short": "A material opportunity arrives. Plant it with care.",
        "meaning_upright": "The Ace of Pentacles is the seed of material abundance — an opportunity in business, finance, health, or the physical world. Plant it. Tend it. The harvest depends on the care you give it now.",
        "meaning_reversed": "A golden opportunity squandered through lack of planning, or greed that poisons a good thing. What is preventing you from acting on what's available to you?",
        "element": "Earth",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Pents01.jpg",
    },
    {
        "name": "Two of Pentacles",
        "number": "2",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["balance", "adaptability", "juggling priorities", "flexibility"],
        "keywords_reversed": ["imbalance", "disorganisation", "overwhelm"],
        "meaning_short": "Keep all the balls in the air — but know your limits.",
        "meaning_upright": "A figure juggles two pentacles amid turbulent seas — this is the art of managing competing demands with grace and adaptability. You are handling multiple priorities. Keep going — but check which balls actually need to be in the air.",
        "meaning_reversed": "Too many things in the air, and they're starting to drop. Disorganisation, financial strain, or the inability to prioritise is taking a toll. Something needs to be set down.",
        "element": "Earth",
        "planet": "Jupiter in Capricorn",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Pents02.jpg",
    },
    {
        "name": "Three of Pentacles",
        "number": "3",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["teamwork", "collaboration", "skill", "craftsmanship", "planning"],
        "keywords_reversed": ["poor teamwork", "lack of cohesion", "working alone"],
        "meaning_short": "Great work is built together. Respect the skills each person brings.",
        "meaning_upright": "An apprentice works on a cathedral while architects review plans — this is collaboration at its finest. Each person's skill is valued, the whole exceeds any individual. Seek collaboration. Bring your craft to the collective.",
        "meaning_reversed": "Team dysfunction, credit disputes, or working in isolation when collaboration would serve you better. Who are you refusing to work with, and why?",
        "element": "Earth",
        "planet": "Mars in Capricorn",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Pents03.jpg",
    },
    {
        "name": "Four of Pentacles",
        "number": "4",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["security", "control", "hoarding", "stability", "conservatism"],
        "keywords_reversed": ["generosity", "releasing control", "financial insecurity"],
        "meaning_short": "Hold what matters. Release what keeps you from growing.",
        "meaning_upright": "A figure clutches pentacles to their chest, crown, and feet — nothing can be lost, nothing can flow. Security becomes imprisonment. Stability is wise; hoarding is fear. What are you gripping too tightly to allow anything new in?",
        "meaning_reversed": "Finally letting go — of material control, old security blankets, or the fear of financial loss. Or: the opposite — reckless spending from anxiety. Check which is true.",
        "element": "Earth",
        "planet": "Sun in Capricorn",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/35/Pents04.jpg",
    },
    {
        "name": "Five of Pentacles",
        "number": "5",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["hardship", "poverty", "insecurity", "isolation", "worry"],
        "keywords_reversed": ["recovery", "spiritual wealth", "accepting help"],
        "meaning_short": "Help is closer than the cold makes it feel. Look up.",
        "meaning_upright": "Two figures trudge through snow past a lit church window — cold, injured, and alone when warmth is right there. Financial hardship, physical difficulty, or a sense of being left out in the cold. The help exists — are you too proud or too exhausted to seek it?",
        "meaning_reversed": "Recovery from hardship. Beginning to see that wealth isn't only material. Or finally accepting the help that was always available.",
        "element": "Earth",
        "planet": "Mercury in Taurus",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/96/Pents05.jpg",
    },
    {
        "name": "Six of Pentacles",
        "number": "6",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["generosity", "giving", "receiving", "charity", "fairness"],
        "keywords_reversed": ["strings attached", "power imbalance", "debt", "selfishness"],
        "meaning_short": "Give what you can. Receive without shame.",
        "meaning_upright": "A wealthy figure distributes coins — some kneel to receive, the merchant holds scales. This is the card of generosity and the balance of giving and receiving. Are you in a position to give? Do so freely. Are you in need? Allow yourself to receive.",
        "meaning_reversed": "Generosity with strings attached, charity that disempowers, or a power imbalance masking as benevolence. Who benefits from the arrangement, and who is made dependent?",
        "element": "Earth",
        "planet": "Moon in Taurus",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Pents06.jpg",
    },
    {
        "name": "Seven of Pentacles",
        "number": "7",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["patience", "investment", "long-term view", "assessment", "growth"],
        "keywords_reversed": ["impatience", "lack of reward", "poor investment"],
        "meaning_short": "You're tending something that takes time. Keep going.",
        "meaning_upright": "A gardener pauses to look at their growing crop — still not harvest time, but real progress is visible. The Seven of Pentacles honours the long game. Assess what's growing and what isn't. Redirect effort where needed. Your investment is real.",
        "meaning_reversed": "Working hard with no visible return, or investing in the wrong thing. Or impatience causing you to harvest too early. What needs to be given more time — or cut entirely?",
        "element": "Earth",
        "planet": "Saturn in Taurus",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Pents07.jpg",
    },
    {
        "name": "Eight of Pentacles",
        "number": "8",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["diligence", "mastery", "skill-building", "dedication", "craftsmanship"],
        "keywords_reversed": ["perfectionism", "lack of focus", "poor quality", "cutting corners"],
        "meaning_short": "Mastery comes through repetition. Do the work.",
        "meaning_upright": "An apprentice works alone on pentacle after pentacle — this is the satisfaction of craft, of skill built slowly through diligence. You are in a period of learning or deep work. Focus. The mastery is coming through the repetition, not despite it.",
        "meaning_reversed": "Cutting corners, perfectionism so paralyzing nothing gets done, or scattered energy preventing skill development. Where is quality being sacrificed?",
        "element": "Earth",
        "planet": "Sun in Virgo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Pents08.jpg",
    },
    {
        "name": "Nine of Pentacles",
        "number": "9",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["abundance", "self-sufficiency", "luxury", "independence", "refinement"],
        "keywords_reversed": ["dependency", "financial setback", "overindulgence"],
        "meaning_short": "You built this. Enjoy what your discipline has created.",
        "meaning_upright": "An elegant figure stands amid a prosperous garden, falcon on wrist — this is earned abundance and self-possession. You have created material security through effort and discernment. Don't diminish this. Enjoy the fruits of your own making.",
        "meaning_reversed": "Financial dependency, setbacks undermining security, or luxury that covers an inner emptiness. What is the quality of your self-sufficiency?",
        "element": "Earth",
        "planet": "Venus in Virgo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Pents09.jpg",
    },
    {
        "name": "Ten of Pentacles",
        "number": "10",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["legacy", "family wealth", "long-term security", "inheritance", "roots"],
        "keywords_reversed": ["family conflict", "financial failure", "broken legacy"],
        "meaning_short": "What you build now will outlast you. Build accordingly.",
        "meaning_upright": "An elder surrounded by family and dogs in a prosperous courtyard — this is the pinnacle of material and familial fulfilment. Legacy, generational wealth, and the security that comes from deep roots. What are you building that will last?",
        "meaning_reversed": "Family conflict over money or legacy, financial foundations crumbling, or inherited dysfunction. What cycle are you being asked to break?",
        "element": "Earth",
        "planet": "Mercury in Virgo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Pents10.jpg",
    },
    {
        "name": "Page of Pentacles",
        "number": "Page",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["study", "ambition", "practicality", "new opportunities", "diligence"],
        "keywords_reversed": ["procrastination", "lack of progress", "learning blocked"],
        "meaning_short": "Apply yourself with patience. Great things start as study.",
        "meaning_upright": "The Page of Pentacles gazes intently at a golden coin — steady, curious, ambitious in the most grounded sense. This is the student, the apprentice, the person who builds their future one careful step at a time. Learn well. Apply what you learn.",
        "meaning_reversed": "Procrastination, failure to put learning into practice, or ambition that can't get off the ground. What's blocking you from beginning the work?",
        "element": "Earth",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Pents11.jpg",
    },
    {
        "name": "Knight of Pentacles",
        "number": "Knight",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["reliability", "hard work", "responsibility", "routine", "steadiness"],
        "keywords_reversed": ["laziness", "obsession with routine", "stubbornness", "stagnation"],
        "meaning_short": "Slow, steady, and relentless. Dependability is a superpower.",
        "meaning_upright": "The Knight of Pentacles sits still on a powerful horse — not charging ahead, but methodical and completely reliable. This knight finishes what they start. Patient effort, strong work ethic, and total trustworthiness. Be this person. Or appreciate one who is.",
        "meaning_reversed": "Stuck in routine to the point of stagnation. Or the opposite — commitments dropped, laziness replacing discipline. Is your steadiness serving you or limiting you?",
        "element": "Earth",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Pents12.jpg",
    },
    {
        "name": "Queen of Pentacles",
        "number": "Queen",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["nurturing", "practical", "financial security", "home", "generosity"],
        "keywords_reversed": ["smothering", "financial insecurity", "neglect of self"],
        "meaning_short": "Create abundance and comfort — for yourself as much as others.",
        "meaning_upright": "The Queen of Pentacles sits amid lush garden abundance, a rabbit leaping at her feet — this is practical nourishment, financial wisdom, and the creation of genuine safety and comfort. Provide for yourself and others with the same warmth. Your home is your sanctuary.",
        "meaning_reversed": "Smothering others while neglecting yourself, financial insecurity creating anxiety, or prioritising material comfort over emotional depth.",
        "element": "Earth",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/88/Pents13.jpg",
    },
    {
        "name": "King of Pentacles",
        "number": "King",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["abundance", "security", "ambition", "discipline", "financial mastery"],
        "keywords_reversed": ["corruption", "materialism", "financial failure", "stubbornness"],
        "meaning_short": "Build the empire. Manage it with both wisdom and warmth.",
        "meaning_upright": "The King of Pentacles sits on a throne adorned with bulls and vines — this is material mastery, entrepreneurial success, and the security that comes from discipline over time. He gives generously because he has built well. Be the steward of what you've created.",
        "meaning_reversed": "Wealth pursued at the cost of ethics or relationships. Stubbornness preventing adaptation. Or financial difficulty despite effort — what structural issue is being missed?",
        "element": "Earth",
        "planet": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Pents14.jpg",
    },
]
