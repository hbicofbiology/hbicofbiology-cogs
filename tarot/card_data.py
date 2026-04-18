"""
Tarot card data: all 78 cards of the Rider-Waite-Smith deck.
Each card has upright/reversed keywords, short meaning, full meaning, and an image URL.
Images sourced from the public domain Rider-Waite deck via Wikipedia.
"""

CARDS = [
    # ── MAJOR ARCANA ─────────────────────────────────────────────────────────
    {
        "id": 0,
        "name": "The Fool",
        "arcana": "major",
        "suit": None,
        "number": "0",
        "keywords_upright": ["beginnings", "innocence", "spontaneity", "free spirit"],
        "keywords_reversed": ["naivety", "foolishness", "recklessness", "risk-taking"],
        "meaning_short": "A leap into the unknown. New beginnings, pure potential, and the courage to start.",
        "meaning_full": (
            "The Fool stands at the precipice, one step from the edge, unburdened by experience or fear. "
            "This card heralds new chapters — a journey not yet mapped, a self not yet shaped. "
            "There is power in not-knowing: the Fool carries only what matters and leaves the rest behind. "
            "Embrace curiosity over caution. Trust the path even when you cannot see it. "
            "The universe rewards those who dare to begin."
        ),
        "meaning_reversed_short": "Caution needed. Recklessness, poor planning, or naivety leading you astray.",
        "meaning_reversed_full": (
            "Reversed, the Fool's freedom tips into foolishness. Leaps are taken without looking; "
            "risks are romanticised rather than weighed. There may be a refusal to grow up, "
            "a clinging to chaos dressed as spontaneity. Ask yourself: is this freedom — or avoidance? "
            "Ground yourself before moving forward."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg",
        "flavour": "The edge of everything is the beginning of something.",
    },
    {
        "id": 1,
        "name": "The Magician",
        "arcana": "major",
        "suit": None,
        "number": "I",
        "keywords_upright": ["willpower", "skill", "manifestation", "resourcefulness"],
        "keywords_reversed": ["manipulation", "untapped talent", "illusion", "wasted potential"],
        "meaning_short": "All tools are in your hands. Channel your will and make it real.",
        "meaning_full": (
            "The Magician commands the four elements — wand, cup, sword, pentacle — spread before him. "
            "He is the bridge between inspiration and action. Where the Fool dreams, the Magician does. "
            "This card speaks to your full capability: you already have what you need. "
            "Focus, intention, and skilled effort will transform potential into reality. "
            "The universe is listening; speak clearly."
        ),
        "meaning_reversed_short": "Talent unused or misused. Beware manipulation — yours or another's.",
        "meaning_reversed_full": (
            "Reversed, the Magician's gifts curdle. Skills exist but go to waste; potential sits idle "
            "while excuses multiply. Alternatively, there is trickery — someone (perhaps you) is using "
            "knowledge to deceive rather than create. Check your intentions. Are you building something "
            "real, or constructing an illusion to impress?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg",
        "flavour": "As above, so below. As within, so without.",
    },
    {
        "id": 2,
        "name": "The High Priestess",
        "arcana": "major",
        "suit": None,
        "number": "II",
        "keywords_upright": ["intuition", "mystery", "inner knowledge", "the unconscious"],
        "keywords_reversed": ["secrets", "disconnection from intuition", "repression", "confusion"],
        "meaning_short": "Be still. The answer lives in the silence between thoughts.",
        "meaning_full": (
            "The High Priestess sits between two pillars — light and dark, known and unknown. "
            "She does not act; she perceives. This card is a call to go inward, to trust the quiet knowing "
            "that logic cannot reach. Your intuition is not a soft suggestion — it is intelligence in another form. "
            "Pause. Listen to what your body and dreams are already telling you. "
            "Not all wisdom arrives as words."
        ),
        "meaning_reversed_short": "You're ignoring your gut. Secrets surface, intuition is blocked.",
        "meaning_reversed_full": (
            "Reversed, the High Priestess signals a severance from your inner voice. "
            "The noise of the outside world has drowned out what you know to be true. "
            "There may be hidden information being withheld — by others or yourself. "
            "Reconnect with stillness. Journaling, meditation, or simply resting may restore "
            "access to the deep knowledge you've been drowning out."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/88/RWS_Tarot_02_High_Priestess.jpg",
        "flavour": "She does not speak. She remembers.",
    },
    {
        "id": 3,
        "name": "The Empress",
        "arcana": "major",
        "suit": None,
        "number": "III",
        "keywords_upright": ["fertility", "abundance", "nurturing", "nature", "creativity"],
        "keywords_reversed": ["creative block", "dependence", "smothering", "neglect"],
        "meaning_short": "Abundance and growth. Nurture yourself and watch things bloom.",
        "meaning_full": (
            "The Empress reclines in a lush garden, crowned with stars, robed in fertility. "
            "She is the embodiment of creative life force — not just children, but art, projects, "
            "relationships, and the slow patience of growing things. This card asks you to tend, to nourish, "
            "to trust the organic pace of becoming. Beauty, sensuality, and pleasure are not distractions — "
            "they are fuel. Let yourself receive as generously as you give."
        ),
        "meaning_reversed_short": "Creative drought or smothering. Something is over-tended or abandoned.",
        "meaning_reversed_full": (
            "Reversed, the Empress's abundance becomes stagnation or excess. Creative blocks loom; "
            "projects wither from neglect or suffocation. There may be co-dependency — giving so much "
            "that both giver and receiver are diminished. Reclaim your creative autonomy. "
            "Nurture is not control. Growth requires space as much as care."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d3/RWS_Tarot_03_Empress.jpg",
        "flavour": "From the earth, everything. From patience, everything.",
    },
    {
        "id": 4,
        "name": "The Emperor",
        "arcana": "major",
        "suit": None,
        "number": "IV",
        "keywords_upright": ["authority", "structure", "stability", "discipline", "leadership"],
        "keywords_reversed": ["rigidity", "domination", "stubbornness", "loss of control"],
        "meaning_short": "Build the structure your vision needs. Authority, discipline, and order.",
        "meaning_full": (
            "The Emperor sits on a stone throne — immovable, deliberate, commanding. "
            "This card speaks to the power of order, of foundations laid with intention. "
            "Your ideas need architecture. Dreams require frameworks. Leadership here is not domination "
            "but responsibility — the willingness to hold the structure so others can build within it. "
            "Be the mountain. Be reliable. Create systems that outlast the moment."
        ),
        "meaning_reversed_short": "Control becomes tyranny. Rigidity or chaos where discipline is needed.",
        "meaning_reversed_full": (
            "Reversed, the Emperor's strength calcifies into inflexibility. Rules exist for their own sake; "
            "authority is exercised without wisdom. There may be a father figure or institution creating harm "
            "through excessive control. Alternatively, the opposite: a total collapse of structure, "
            "an inability to impose necessary discipline. Find the middle path between iron and collapse."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg",
        "flavour": "The throne is not a prize. It is a responsibility.",
    },
    {
        "id": 5,
        "name": "The Hierophant",
        "arcana": "major",
        "suit": None,
        "number": "V",
        "keywords_upright": ["tradition", "conformity", "morality", "guidance", "institutions"],
        "keywords_reversed": ["rebellion", "subversiveness", "new approaches", "questioning dogma"],
        "meaning_short": "Tradition and shared wisdom. Seek a mentor, or honour established paths.",
        "meaning_full": (
            "The Hierophant presides over ritual, tradition, and the transmission of received wisdom. "
            "This card can indicate seeking guidance from established institutions — religion, academia, "
            "cultural tradition — or the value of learning from those who have walked before you. "
            "There is power in shared meaning and collective ritual. Sometimes the old ways hold genuine insight. "
            "A teacher, mentor, or structured system may be exactly what is needed now."
        ),
        "meaning_reversed_short": "Rejecting convention. Question what you've been taught.",
        "meaning_reversed_full": (
            "Reversed, the Hierophant invites you to question dogma. The rules you've inherited may not serve you; "
            "institutions may be failing in their mandate. There is wisdom in rebellion when rebellion is honest. "
            "This may be a call to forge your own spiritual or moral path — not out of arrogance, "
            "but out of genuine seeking. What do YOU believe, separate from what you were told to believe?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8d/RWS_Tarot_05_Hierophant.jpg",
        "flavour": "The map is not the territory. But maps still have value.",
    },
    {
        "id": 6,
        "name": "The Lovers",
        "arcana": "major",
        "suit": None,
        "number": "VI",
        "keywords_upright": ["love", "union", "alignment", "choices", "values"],
        "keywords_reversed": ["disharmony", "imbalance", "misalignment", "poor choices"],
        "meaning_short": "A meaningful choice about love, values, or union. Alignment is key.",
        "meaning_full": (
            "The Lovers stand beneath an angel — a card of choices made from the deepest part of yourself. "
            "Yes, this can be romantic love, but more broadly it speaks to alignment: between your actions "
            "and your values, between what you want and what you choose. A fork in the road approaches "
            "or has arrived. The decision cannot be made with logic alone. "
            "What does your whole self — not just your mind — want?"
        ),
        "meaning_reversed_short": "Misalignment in love or values. A poor choice made from fear or desire.",
        "meaning_reversed_full": (
            "Reversed, the Lovers signal disharmony — within a relationship or within yourself. "
            "Choices may have been made that conflict with your core values; "
            "a relationship may be out of balance. There may be temptation to take the easy path "
            "rather than the true one. Revisit your commitments. Where have you abandoned yourself "
            "in order to keep something else?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/TheLovers.jpg",
        "flavour": "The heart is not irrational. It speaks a different language.",
    },
    {
        "id": 7,
        "name": "The Chariot",
        "arcana": "major",
        "suit": None,
        "number": "VII",
        "keywords_upright": ["control", "willpower", "victory", "assertion", "determination"],
        "keywords_reversed": ["lack of control", "aggression", "no direction", "scattered energy"],
        "meaning_short": "Drive forward. Victory comes through focused will and self-mastery.",
        "meaning_full": (
            "The Charioteer drives two sphinxes — one dark, one light — forward through sheer force of will. "
            "They do not pull in the same direction, yet the chariot moves. This is the paradox of control: "
            "not the absence of conflicting forces, but the mastery of them. "
            "You are capable of more than you think. Forward momentum requires discipline, not perfection. "
            "Harness your contradictions and drive."
        ),
        "meaning_reversed_short": "Loss of direction or control. Aggression or scattered force working against you.",
        "meaning_reversed_full": (
            "Reversed, the Chariot's opposing forces overwhelm the driver. Forward motion stalls; "
            "ambition turns aggressive or collapses entirely. Energy is scattered without purpose. "
            "There may be a need to slow down and reassert direction before charging ahead. "
            "Where are you forcing movement that needs to be paused and recalibrated?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9b/RWS_Tarot_07_Chariot.jpg",
        "flavour": "Victory is not the absence of resistance — it is moving through it.",
    },
    {
        "id": 8,
        "name": "Strength",
        "arcana": "major",
        "suit": None,
        "number": "VIII",
        "keywords_upright": ["courage", "patience", "compassion", "inner strength", "influence"],
        "keywords_reversed": ["self-doubt", "weakness", "raw emotion", "insecurity"],
        "meaning_short": "Gentle mastery. True strength is patience and compassion, not force.",
        "meaning_full": (
            "A woman closes a lion's mouth — not by overpowering it, but by soothing it. "
            "Strength here is not brute force but the quiet authority of someone fully at peace with themselves. "
            "The wild, instinctive self is not to be destroyed — it is to be befriended. "
            "You have more inner resources than you credit yourself with. "
            "Approach this challenge with calm, compassion, and patience. You are already strong enough."
        ),
        "meaning_reversed_short": "Self-doubt or raw emotion overpowering your better judgment.",
        "meaning_reversed_full": (
            "Reversed, Strength signals that fear, insecurity, or uncontrolled instinct is in the driver's seat. "
            "You may be doubting yourself precisely when you most need self-trust. "
            "Alternatively, you may be repressing emotion rather than integrating it — forcing calm "
            "rather than finding it. The lion inside needs acknowledgement, not a cage."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f5/RWS_Tarot_08_Strength.jpg",
        "flavour": "The quietest power in the room is often the most absolute.",
    },
    {
        "id": 9,
        "name": "The Hermit",
        "arcana": "major",
        "suit": None,
        "number": "IX",
        "keywords_upright": ["solitude", "introspection", "guidance", "inner wisdom", "contemplation"],
        "keywords_reversed": ["isolation", "loneliness", "withdrawal", "lost", "rejection of guidance"],
        "meaning_short": "Withdraw and listen inward. The light you need is already within you.",
        "meaning_full": (
            "The Hermit walks alone on a mountaintop, lantern raised — not searching the dark for others, "
            "but illuminating his own next step. This is a card of chosen solitude, of the productive retreat "
            "that allows deep reflection. Not every question can be answered by looking outward. "
            "Some truths only emerge in the quiet. Seek your own counsel. Go inward. "
            "The answers you seek are patient — they are waiting for you to be still enough to hear them."
        ),
        "meaning_reversed_short": "Isolation becoming unhealthy. Refusing guidance or retreating from life.",
        "meaning_reversed_full": (
            "Reversed, the Hermit's solitude has curdled into loneliness or stubborn isolation. "
            "You may be cutting yourself off from help that is genuinely being offered, "
            "or using contemplation as a way to avoid action. There is wisdom in solitude, "
            "but also a time to descend the mountain. Consider: is this retreat replenishing you, "
            "or keeping you stuck?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/RWS_Tarot_09_Hermit.jpg",
        "flavour": "The lantern does not light the whole path. Only the next step.",
    },
    {
        "id": 10,
        "name": "Wheel of Fortune",
        "arcana": "major",
        "suit": None,
        "number": "X",
        "keywords_upright": ["fate", "cycles", "luck", "turning point", "change"],
        "keywords_reversed": ["bad luck", "resistance to change", "breaking cycles", "no control"],
        "meaning_short": "The wheel turns. A pivotal change arrives — embrace the cycle.",
        "meaning_full": (
            "The Wheel spins — creatures rise and fall at its rim while the sphinx at the top holds still. "
            "Everything is in motion. What was low rises; what was high descends. "
            "A significant turning point is at hand — the kind that feels fated, like the universe is shifting "
            "a gear. You cannot stop the wheel, but you can choose where you stand in relation to it. "
            "Adapt. The change coming is larger than one decision."
        ),
        "meaning_reversed_short": "Resisting inevitable change. Breaking a cycle, or trapped in one.",
        "meaning_reversed_full": (
            "Reversed, the Wheel signals stagnation or bad luck — a cycle that repeats despite your desire "
            "for change, or a refusal to accept that everything is impermanent. "
            "You may be gripping something that was never meant to last. "
            "Alternatively, this is the moment to consciously break a pattern. "
            "What cycle in your life is it time to step off of?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg",
        "flavour": "The only constant is the spinning.",
    },
    {
        "id": 11,
        "name": "Justice",
        "arcana": "major",
        "suit": None,
        "number": "XI",
        "keywords_upright": ["fairness", "truth", "cause and effect", "law", "accountability"],
        "keywords_reversed": ["injustice", "dishonesty", "avoidance", "unfair outcome"],
        "meaning_short": "Truth and accountability. Causes have consequences — face them clearly.",
        "meaning_full": (
            "Justice sits between two pillars, scales balanced, sword raised. "
            "This is not blind justice — the figure sees everything clearly. "
            "What you have sown, you will reap. What is true will surface. "
            "This card calls for absolute honesty — with others and, most critically, with yourself. "
            "A decision or outcome requires clear-eyed fairness. "
            "Do not let wishful thinking distort what the scales are already showing you."
        ),
        "meaning_reversed_short": "Injustice or dishonesty. Avoiding accountability or distorting truth.",
        "meaning_reversed_full": (
            "Reversed, Justice signals that truth is being obscured — by you, by others, or by broken systems. "
            "An outcome may feel deeply unfair. You may be avoiding responsibility, "
            "or someone else is escaping consequences they earned. "
            "This does not always mean you can fix it. Sometimes injustice is the uncomfortable reality "
            "you must accept before you can move beyond it."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/RWS_Tarot_11_Justice.jpg",
        "flavour": "Truth does not need defending. It simply needs witnessing.",
    },
    {
        "id": 12,
        "name": "The Hanged Man",
        "arcana": "major",
        "suit": None,
        "number": "XII",
        "keywords_upright": ["pause", "surrender", "new perspective", "sacrifice", "waiting"],
        "keywords_reversed": ["delays", "resistance", "stalling", "indecision"],
        "meaning_short": "Stop. Surrender the struggle. A new perspective will free you.",
        "meaning_full": (
            "The Hanged Man is suspended willingly — upside down, at peace, seeing the world inverted. "
            "This is not a card of defeat but of chosen surrender. Some situations cannot be forced; "
            "they must be waited through. The pause you resist may be the very thing that shifts everything. "
            "Let go of the need to act. Suspend yourself in the uncertainty and let a new perspective arrive. "
            "What looks like a sacrifice may be the only true path forward."
        ),
        "meaning_reversed_short": "Stalling instead of surrendering. Resistance to necessary pause.",
        "meaning_reversed_full": (
            "Reversed, the Hanged Man's suspension is no longer chosen — it is imposed, or worse, prolonged "
            "beyond its usefulness. You may be delaying a decision that is already made in your heart, "
            "or you may be finally ready to cut yourself down and act. "
            "Has the waiting served its purpose? It may be time to move."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2b/RWS_Tarot_12_Hanged_Man.jpg",
        "flavour": "There is a wisdom that only arrives when you stop trying to reach it.",
    },
    {
        "id": 13,
        "name": "Death",
        "arcana": "major",
        "suit": None,
        "number": "XIII",
        "keywords_upright": ["endings", "transformation", "transition", "letting go", "change"],
        "keywords_reversed": ["resistance to change", "stagnation", "inability to move on"],
        "meaning_short": "Something must end for something to begin. Let it go.",
        "meaning_full": (
            "Death rides slowly — not threatening but inevitable. In his wake, the sun rises. "
            "This card almost never means physical death. It means the end of a chapter: a relationship, "
            "an identity, a phase of life. And endings, however painful, are the price of transformation. "
            "What needs to die so that you can live more fully? "
            "Grief is appropriate. So is trust in what comes next. "
            "The caterpillar does not survive the cocoon — and that is exactly the point."
        ),
        "meaning_reversed_short": "Refusing an ending. Stagnation from clinging to what is already over.",
        "meaning_reversed_full": (
            "Reversed, Death's transformation is blocked. You are holding onto something that has already ended, "
            "prolonging decay out of fear of the unknown. The refusal to let go is costing you more "
            "than the letting go would. There may also be a slow, grinding change happening beneath the surface "
            "that has not yet become visible. Either way — the ending is coming. "
            "The question is only how much you suffer on the way."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/RWS_Tarot_13_Death.jpg",
        "flavour": "Every ending is a threshold.",
    },
    {
        "id": 14,
        "name": "Temperance",
        "arcana": "major",
        "suit": None,
        "number": "XIV",
        "keywords_upright": ["balance", "moderation", "patience", "purpose", "integration"],
        "keywords_reversed": ["imbalance", "excess", "lack of long-term vision", "conflict"],
        "meaning_short": "Blend, balance, and integrate. Patience is the practice here.",
        "meaning_full": (
            "The angel of Temperance pours water between two cups — endlessly, without spilling. "
            "One foot on land, one in water. This card is the art of integration: "
            "combining opposites into something greater, moving slowly enough to do it right. "
            "The answer you seek is not in extremes. It is in the careful, patient blending "
            "of what seems incompatible. Long-term vision over short-term impulse. "
            "You are being refined — trust the process."
        ),
        "meaning_reversed_short": "Imbalance or excess. Something is out of proportion.",
        "meaning_reversed_full": (
            "Reversed, Temperance's balance is lost — to excess, to conflict, or to a lack of patience "
            "with the long work of integration. There may be internal conflict between opposing desires "
            "or values that has not yet found resolution. Slow down. "
            "What is the extreme you keep swinging to, and what would the middle look like?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f8/RWS_Tarot_14_Temperance.jpg",
        "flavour": "The most powerful alchemy is the patient kind.",
    },
    {
        "id": 15,
        "name": "The Devil",
        "arcana": "major",
        "suit": None,
        "number": "XV",
        "keywords_upright": ["bondage", "addiction", "materialism", "shadow self", "restriction"],
        "keywords_reversed": ["release", "breaking free", "reclaiming power", "shadow work"],
        "meaning_short": "Something binds you — and you have more power to leave than you think.",
        "meaning_full": (
            "The Devil looms above two chained figures — but look closely: the chains are loose. "
            "They could leave. They choose to stay. This is the nature of the Devil's power: "
            "it relies on our belief in our own captivity. Addiction, toxic patterns, materialism, "
            "destructive relationships — all are chains we can remove, but don't. "
            "What are you telling yourself you cannot escape? "
            "The first step to freedom is naming the thing that holds you."
        ),
        "meaning_reversed_short": "Breaking free. Reclaiming power from an addiction, pattern, or influence.",
        "meaning_reversed_full": (
            "Reversed, the Devil's chains loosen. You are beginning to see the illusion for what it is — "
            "to reclaim agency you surrendered. This is profound work, and it is not comfortable. "
            "Confronting your shadow, your desires, your role in your own captivity — "
            "this is some of the most important inner work there is. You are stronger than what held you."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/55/RWS_Tarot_15_Devil.jpg",
        "flavour": "The cage was never locked.",
    },
    {
        "id": 16,
        "name": "The Tower",
        "arcana": "major",
        "suit": None,
        "number": "XVI",
        "keywords_upright": ["sudden change", "upheaval", "chaos", "revelation", "awakening"],
        "keywords_reversed": ["avoidance of disaster", "fear of change", "delayed collapse"],
        "meaning_short": "Something built on a false foundation must fall. Chaos precedes clarity.",
        "meaning_full": (
            "Lightning strikes the Tower. Figures fall. The crown is blasted from the top. "
            "The Tower is the most feared card in the deck — and one of the most necessary. "
            "What is built on false foundations cannot stand; the lightning only accelerates the inevitable. "
            "This upheaval, however devastating, is also revelation. "
            "What you lose in the collapse was never truly stable. "
            "Something real can only be built once the illusion is rubble."
        ),
        "meaning_reversed_short": "Narrowly avoiding disaster, or delaying an inevitable collapse.",
        "meaning_reversed_full": (
            "Reversed, the Tower's destruction is delayed or averted — or happening slowly rather than all at once. "
            "You may be in denial about a crumbling structure in your life, "
            "propping up what needs to fall with enormous effort. "
            "Alternatively, you have just avoided catastrophe. "
            "Either way: what needs to change so you are not here again?"
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/53/RWS_Tarot_16_Tower.jpg",
        "flavour": "The lightning does not destroy. It reveals.",
    },
    {
        "id": 17,
        "name": "The Star",
        "arcana": "major",
        "suit": None,
        "number": "XVII",
        "keywords_upright": ["hope", "faith", "renewal", "inspiration", "serenity"],
        "keywords_reversed": ["despair", "hopelessness", "disconnection", "lack of faith"],
        "meaning_short": "After the storm, the star appears. Hope is not naive — it is necessary.",
        "meaning_full": (
            "A woman kneels at the water's edge beneath a canopy of stars, pouring water freely — "
            "giving and receiving in perfect ease. After the Tower, comes the Star: healing, hope, "
            "the slow beautiful process of renewal. This is not the dramatic joy of the Sun "
            "but the quiet, steady faith that things can and will be well. "
            "Rest. Allow yourself to be nourished. The universe is replenishing what was lost."
        ),
        "meaning_reversed_short": "Hopelessness or disconnection from faith in the future.",
        "meaning_reversed_full": (
            "Reversed, the Star's light dims — not gone, but obscured. "
            "Despair, pessimism, or a deep disconnection from any sense of hope or purpose may be present. "
            "You may have been through too much to believe in renewal right now. "
            "That is valid. But the star itself has not moved. "
            "Seek small signs of light rather than demanding the sky be clear."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/db/RWS_Tarot_17_Star.jpg",
        "flavour": "Hope is not a feeling. It is a practice.",
    },
    {
        "id": 18,
        "name": "The Moon",
        "arcana": "major",
        "suit": None,
        "number": "XVIII",
        "keywords_upright": ["illusion", "fear", "the unconscious", "confusion", "the unknown"],
        "keywords_reversed": ["release of fear", "repressed emotion", "confusion lifting"],
        "meaning_short": "The path is unclear. Trust your instincts through the dark.",
        "meaning_full": (
            "Under a full moon, a dog and wolf howl from either shore. A crayfish emerges from the deep. "
            "The path winds between two towers into an unknown beyond. "
            "The Moon rules the unconscious — the fears, dreams, and unresolved things that surface in the dark. "
            "Things are not as they appear. Illusion distorts. "
            "Navigate carefully: use intuition, not logic. "
            "The confusion is real, but it is not permanent. The moon always wanes."
        ),
        "meaning_reversed_short": "Confusion lifting. Hidden fears or repressed truths surfacing.",
        "meaning_reversed_full": (
            "Reversed, the Moon's fog begins to clear. What was hidden — perhaps repressed fears, "
            "unconscious patterns, or hidden information — is coming to light. "
            "This can feel disorienting, but it is ultimately liberating. "
            "Face what the dark has been concealing. The light of clarity is worth the discomfort of seeing."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/RWS_Tarot_18_Moon.jpg",
        "flavour": "The dark is not the absence of light. It is a different kind of seeing.",
    },
    {
        "id": 19,
        "name": "The Sun",
        "arcana": "major",
        "suit": None,
        "number": "XIX",
        "keywords_upright": ["joy", "success", "optimism", "vitality", "clarity"],
        "keywords_reversed": ["temporary depression", "blocked success", "inner child repression"],
        "meaning_short": "Pure joy and clarity. Success, vitality, and radiant well-being.",
        "meaning_full": (
            "A child rides a white horse beneath the blazing sun, arms wide, face open. "
            "Nothing is hidden here; nothing is ambiguous. The Sun is the simplest and most unambiguous "
            "good card in the deck — joy, vitality, success, and the freedom that comes with it. "
            "You are allowed to be this happy. You are allowed to succeed, to be seen, to feel this alive. "
            "Do not diminish it. Let the warmth in."
        ),
        "meaning_reversed_short": "Joy is blocked or dimmed. Seek the light you're avoiding.",
        "meaning_reversed_full": (
            "Reversed, the Sun's light is partially eclipsed. Joy feels just out of reach; "
            "success is delayed or undercut by self-doubt. There may be a suppression of the inner child — "
            "a refusal to allow playfulness or delight. "
            "What is keeping you from fully stepping into the warmth available to you? "
            "The sun hasn't moved. You have stepped into shadow."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/17/RWS_Tarot_19_Sun.jpg",
        "flavour": "Some moments deserve to be simple and full.",
    },
    {
        "id": 20,
        "name": "Judgement",
        "arcana": "major",
        "suit": None,
        "number": "XX",
        "keywords_upright": ["reflection", "reckoning", "awakening", "absolution", "calling"],
        "keywords_reversed": ["self-doubt", "refusing the call", "harsh self-judgment"],
        "meaning_short": "A moment of reckoning. Rise to answer the call of your higher self.",
        "meaning_full": (
            "Figures rise from their graves at the angel's trumpet call — not in fear, but in joy. "
            "Judgement is the moment of spiritual reckoning: a summons from something deeper than circumstance, "
            "an invitation to shed the old self and step into a new becoming. "
            "This card asks: who have you been, and who are you ready to become? "
            "Your past is not your prison. It is your data. "
            "Rise. Something is calling you, and it has your name."
        ),
        "meaning_reversed_short": "Refusing the call. Harsh self-judgment blocking transformation.",
        "meaning_reversed_full": (
            "Reversed, Judgement's call goes unanswered — out of fear, self-doubt, or the weight of shame. "
            "You may be judging yourself too harshly to believe you deserve to rise. "
            "Or you may be ignoring a genuine summons from your deeper self because it requires too much change. "
            "Self-forgiveness is not weakness. It is the prerequisite for transformation."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/dd/RWS_Tarot_20_Judgement.jpg",
        "flavour": "Absolution is not given. It is chosen.",
    },
    {
        "id": 21,
        "name": "The World",
        "arcana": "major",
        "suit": None,
        "number": "XXI",
        "keywords_upright": ["completion", "integration", "accomplishment", "wholeness", "travel"],
        "keywords_reversed": ["incompletion", "shortcuts", "stagnation", "lack of closure"],
        "meaning_short": "A cycle is complete. Wholeness achieved. Celebrate before the next beginning.",
        "meaning_full": (
            "A figure dances within a wreath of laurel, surrounded by the four elemental creatures. "
            "The World is completion — not just of a project or phase, but of a cycle of becoming. "
            "You have integrated what you set out to learn. You have arrived. "
            "Honour this. Do not rush to the next thing before acknowledging how far you have come. "
            "The World is also the threshold: full circle, and the Fool waits at zero once more, "
            "ready to begin again — but changed."
        ),
        "meaning_reversed_short": "Incomplete cycle. Taking shortcuts or refusing to finish what you started.",
        "meaning_reversed_full": (
            "Reversed, the World signals a cycle left open — an achievement almost reached but abandoned, "
            "or a pattern repeating because lessons weren't integrated. "
            "There may be a fear of completion itself, of the grief that comes when something good ends. "
            "Finish the thing. Close the loop. You cannot begin the next chapter while still stuck in this one."
        ),
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/ff/RWS_Tarot_21_World.jpg",
        "flavour": "You have arrived. And the road is waiting.",
    },

    # ── WANDS ────────────────────────────────────────────────────────────────
    {
        "id": 22,
        "name": "Ace of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "Ace",
        "keywords_upright": ["inspiration", "new opportunity", "growth", "potential", "spark"],
        "keywords_reversed": ["delays", "lack of motivation", "missed opportunity", "creative block"],
        "meaning_short": "A spark of creative fire. Grab it — new ventures and inspiration await.",
        "meaning_full": "The Ace of Wands is raw creative fire — an idea whose time has come, a project begging to be started, an impulse worth following. The universe is handing you a lit torch. Your job is not to question whether you deserve it but to take it and run. Act on this energy before it dissipates. The window is open.",
        "meaning_reversed_short": "A creative spark that fizzled. Delays, blocks, or missed inspiration.",
        "meaning_reversed_full": "Reversed, the Ace of Wands' fire struggles to catch. Motivation is elusive; ideas feel half-formed and enthusiasm hollow. Creative blocks loom. A promising start may have stalled. Rekindle: return to why you cared, find the smallest possible action, and let momentum rebuild from there.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/11/Wands01.jpg",
        "flavour": "Every fire began with a single spark.",
    },
    {
        "id": 23,
        "name": "Two of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "2",
        "keywords_upright": ["planning", "future vision", "progress", "decisions", "discovery"],
        "keywords_reversed": ["fear of the unknown", "lack of planning", "bad decisions"],
        "meaning_short": "The world is before you. Plan your next move boldly.",
        "meaning_full": "A figure stands holding a globe, gazing beyond familiar horizons. The Two of Wands is the moment after the spark — when you look at what's possible and begin to choose a direction. You have the ability to go far. Now is the time for strategic vision: not just dreaming but planning, not just wishing but mapping. The world really is at your feet.",
        "meaning_reversed_short": "Fear holding you at the threshold. Poor planning or indecision.",
        "meaning_reversed_full": "Reversed, the Two of Wands shows someone who sees the horizon but won't step toward it. Fear of the unknown, lack of planning, or a bad choice of direction keeps you stuck at the precipice. Dream bigger — but back the dream with a plan.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Wands02.jpg",
        "flavour": "The whole world, and still you hesitate.",
    },
    {
        "id": 24,
        "name": "Three of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "3",
        "keywords_upright": ["expansion", "foresight", "looking ahead", "overseas opportunities"],
        "keywords_reversed": ["obstacles", "delays", "frustration", "lack of foresight"],
        "meaning_short": "Ships are coming in. Your early efforts are starting to pay off.",
        "meaning_full": "Ships on the horizon — the Three of Wands is the first evidence that what you launched is working. You have sent your ideas into the world and they are returning with results. This is a card of expanding horizons, of enterprise extending beyond its original scope. Don't pull back now. Double down on what's working.",
        "meaning_reversed_short": "Returns delayed or blocked. Foresight needed — plan further ahead.",
        "meaning_reversed_full": "Reversed, the ships are late or lost. Efforts feel unrewarded; expansion hits walls. There may be a failure of foresight — not looking far enough ahead, or not accounting for obstacles. Reassess. The plan may need adjustment before you can progress.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Wands03.jpg",
        "flavour": "What you sent out is beginning to return.",
    },
    {
        "id": 25,
        "name": "Four of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "4",
        "keywords_upright": ["celebration", "harmony", "community", "homecoming", "joy"],
        "keywords_reversed": ["lack of support", "instability", "conflict at home"],
        "meaning_short": "Celebrate what has been built. Community, joy, and a moment of arrival.",
        "meaning_full": "Two figures dance beneath garlands strung between four wands. The Four of Wands is pure celebration — the joy of arriving somewhere good, of gathering with people who matter, of recognising what has been built. Allow yourself to enjoy this moment fully. Rest in what is good before pushing forward again.",
        "meaning_reversed_short": "Celebrations disrupted. Tension at home or lack of community.",
        "meaning_reversed_full": "Reversed, the Four of Wands' harmony is disrupted — by conflict in the home, a community that isn't providing support, or a milestone that felt hollow. Something that should be joyful isn't landing right. Look at what is missing from the foundation.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Wands04.jpg",
        "flavour": "The garlands are hung. Let yourself arrive.",
    },
    {
        "id": 26,
        "name": "Five of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "5",
        "keywords_upright": ["conflict", "competition", "tension", "diversity of opinion"],
        "keywords_reversed": ["conflict avoidance", "tension resolved", "suppressed aggression"],
        "meaning_short": "Everyone is fighting for different things. Find the signal in the chaos.",
        "meaning_full": "Five figures swing wands in every direction — not maliciously, but chaotically. The Five of Wands is the noise of competing ideas, agendas, and energies. This doesn't have to mean destructive conflict; it can mean lively debate, creative friction, or the growing pains of collaboration. But something needs to be sorted out before progress resumes.",
        "meaning_reversed_short": "Conflict avoided or finally resolving. Or suppressed aggression simmering.",
        "meaning_reversed_full": "Reversed, the conflict either dissolves or goes underground. If resolving: good. If suppressed: the tension hasn't gone away — it's just waiting. Avoiding necessary confrontation rarely leads anywhere useful.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Wands05.jpg",
        "flavour": "Not all conflict is destruction. Some of it is refinement.",
    },
    {
        "id": 27,
        "name": "Six of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "6",
        "keywords_upright": ["victory", "public recognition", "progress", "self-confidence"],
        "keywords_reversed": ["egotism", "pride before a fall", "lack of recognition"],
        "meaning_short": "Victory lap. Success earned and publicly recognised — accept it.",
        "meaning_full": "A rider returns on horseback, crowned with a laurel wreath while the crowd cheers. The Six of Wands is earned success — the kind that gets noticed. You have achieved something real. This card says: don't deflect the recognition. Allow yourself to be seen in your success. It is not arrogance to accept what you have genuinely earned.",
        "meaning_reversed_short": "Pride before a fall, or success going unacknowledged.",
        "meaning_reversed_full": "Reversed, the Six of Wands' triumph tips into ego, or the victory remains unrecognised. You may be riding too high — overconfident in a win that hasn't fully landed. Or the opposite: you succeeded and no one noticed, leaving you deflated. Either way, check whether validation from outside is running the show.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Wands06.jpg",
        "flavour": "The crowd is cheering. The question is whether you believe you deserve it.",
    },
    {
        "id": 28,
        "name": "Seven of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "7",
        "keywords_upright": ["challenge", "perseverance", "defensiveness", "holding your ground"],
        "keywords_reversed": ["giving up", "overwhelmed", "self-doubt", "caving to pressure"],
        "meaning_short": "Hold your ground. You're being challenged, but you have the high position.",
        "meaning_full": "A figure stands on higher ground, defending against six wands from below. The Seven of Wands is the position of someone who has earned something and is now being tested on whether they'll keep it. Competition, criticism, and challenges come at you — not because you're wrong, but because you're visible. Stand firm. Your position is strong if you believe in it.",
        "meaning_reversed_short": "Caving to pressure or being overwhelmed. Stand firmer or reconsider.",
        "meaning_reversed_full": "Reversed, the Seven of Wands shows someone starting to buckle under pressure. The challenges are wearing you down; doubt is creeping in. You may be right to reconsider your position — or you may be abandoning something worth defending. Distinguish between flexibility and capitulation.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Wands07.jpg",
        "flavour": "The higher ground was won. Now it must be held.",
    },
    {
        "id": 29,
        "name": "Eight of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "8",
        "keywords_upright": ["speed", "action", "movement", "quick decisions", "news"],
        "keywords_reversed": ["delays", "frustration", "scattered energy", "holding back"],
        "meaning_short": "Everything is moving fast. Act quickly — momentum is on your side.",
        "meaning_full": "Eight wands streak through the air in perfect formation. After weeks of waiting, the Eight of Wands signals that everything moves at once. Opportunities arrive, decisions must be made quickly, communication flows. Don't overthink this — the moment is now. Ride the current while it's strong.",
        "meaning_reversed_short": "Momentum stalled or scattered. Delays and frustration with slow progress.",
        "meaning_reversed_full": "Reversed, the Eight of Wands' energy scatters or stalls entirely. Things that should be moving aren't. Messages go unanswered; plans hit unexpected delays. There may be internal resistance slowing what could otherwise flow. Where are you holding yourself back?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Wands08.jpg",
        "flavour": "Finally, everything at once.",
    },
    {
        "id": 30,
        "name": "Nine of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "9",
        "keywords_upright": ["resilience", "persistence", "last stand", "boundaries", "fatigue"],
        "keywords_reversed": ["exhaustion", "giving up", "stubbornness", "paranoia"],
        "meaning_short": "Tired but still standing. One more push — you are closer than you think.",
        "meaning_full": "A weary figure leans on a wand, head bandaged, but still holding the line with eight more behind them. The Nine of Wands is the card of the last stand — exhausted but not defeated. You have been through a great deal. The finish line is closer than it appears. Don't put down the wand now. Rest, then continue.",
        "meaning_reversed_short": "Exhaustion breaking into surrender. Or stubbornness keeping you from help.",
        "meaning_reversed_full": "Reversed, the Nine of Wands' resilience falters — the exhaustion is real and the will to continue is fading. There is no shame in this. But distinguish between genuine burnout that needs rest and stubborn pride refusing help that is being offered. You don't have to carry this alone.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Wands09.jpg",
        "flavour": "Still standing. That is enough.",
    },
    {
        "id": 31,
        "name": "Ten of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "10",
        "keywords_upright": ["burden", "overload", "responsibility", "hard work", "completion near"],
        "keywords_reversed": ["avoiding responsibility", "inability to delegate", "collapse"],
        "meaning_short": "You're carrying too much. The end is in sight, but lay some down.",
        "meaning_full": "A figure struggles toward a village, bent under the weight of ten wands. The Ten of Wands is the card of the overloaded — someone who has taken on so much that the burden is now the whole story. The good news: the village is near. The lesson: you may not need to carry all of this yourself. Completion is close. But first — what can you put down?",
        "meaning_reversed_short": "Crushing burden or refusal to share the load. Something must give.",
        "meaning_reversed_full": "Reversed, the Ten of Wands buckles into collapse or rigid refusal to delegate. Either the load has become unsustainable and something must break, or there is a pathological need to control everything that prevents help from reaching you. Release. Not everything is yours to carry.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Wands10.jpg",
        "flavour": "Set something down. The destination doesn't require all of it.",
    },
    {
        "id": 32,
        "name": "Page of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "Page",
        "keywords_upright": ["enthusiasm", "exploration", "discovery", "free spirit", "new ideas"],
        "keywords_reversed": ["lack of direction", "immaturity", "scattered energy"],
        "meaning_short": "Fearless curiosity. Follow the new thing with open hands.",
        "meaning_full": "The Page of Wands holds their staff and stares at it in wonder — ready to go anywhere, try anything. This card is youthful fire energy: the enthusiasm of someone who hasn't yet been told what's not possible. Follow the new interest. Ask the unusual question. Let curiosity lead before caution arrives.",
        "meaning_reversed_short": "Energy without direction. Scattered ideas, immaturity, or false starts.",
        "meaning_reversed_full": "Reversed, the Page's fire burns without focus — lots of ideas, little follow-through. There is enthusiasm without discipline. Every exciting new thing starts and doesn't finish. Learn to stay with one fire long enough to actually build something.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Wands11.jpg",
        "flavour": "Every expert was once a beginner who refused to care what people thought.",
    },
    {
        "id": 33,
        "name": "Knight of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "Knight",
        "keywords_upright": ["action", "adventure", "impulsiveness", "energy", "passion"],
        "keywords_reversed": ["recklessness", "arrogance", "scattered", "delays"],
        "meaning_short": "Charge forward. Passion and action — but mind the recklessness.",
        "meaning_full": "The Knight of Wands rides at full gallop, fire salamanders on his armour — fearless, magnetic, unstoppable. This is the energy of someone who acts before they think and usually gets away with it through sheer force of charisma and passion. Use this energy. Move fast. But keep one eye on the path ahead.",
        "meaning_reversed_short": "Recklessness and impulsivity causing damage. Slow down.",
        "meaning_reversed_full": "Reversed, the Knight's passion becomes recklessness. Acting before thinking leads to mistakes that could have been avoided. Arrogance may be in play. Channel the fire, but give it direction before you let it run.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/16/Wands12.jpg",
        "flavour": "The fastest way is not always the right way — but sometimes it is.",
    },
    {
        "id": 34,
        "name": "Queen of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "Queen",
        "keywords_upright": ["confidence", "independence", "warmth", "vibrancy", "determination"],
        "keywords_reversed": ["jealousy", "insecurity", "selfishness", "demanding"],
        "meaning_short": "Lead with warmth and confidence. You are magnetic — own it.",
        "meaning_full": "The Queen of Wands sits boldly on her throne, sunflower in hand, black cat at her feet — utterly self-possessed. She is confident without arrogance, warm without neediness, passionate without losing herself. This energy says: you know what you want. You know who you are. Lead from that place.",
        "meaning_reversed_short": "Confidence curdled into jealousy or insecurity. Check the ego.",
        "meaning_reversed_full": "Reversed, the Queen's fire becomes demanding, jealous, or self-absorbed. The confidence is performing rather than genuine. There may be a fear underneath all the heat — of not being enough, of losing what was built. Return to the genuine warmth at your core.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Wands13.jpg",
        "flavour": "The sunflower grows toward light by nature, not effort.",
    },
    {
        "id": 35,
        "name": "King of Wands",
        "arcana": "minor",
        "suit": "wands",
        "number": "King",
        "keywords_upright": ["leadership", "vision", "entrepreneur", "honour", "boldness"],
        "keywords_reversed": ["impulsiveness", "overbearing", "arrogance", "ineffective leadership"],
        "meaning_short": "Lead the vision. Bold, decisive, and inspiring — that's the ask.",
        "meaning_full": "The King of Wands sits with a salamander at his feet and fire in his eyes. He is the visionary leader — someone with a big idea, the charisma to draw others toward it, and the boldness to make it happen. If this card is calling you to lead, accept it without shrinking. Big vision requires big energy.",
        "meaning_reversed_short": "Leadership gone wrong — arrogant, impulsive, or ineffective.",
        "meaning_reversed_full": "Reversed, the King's visionary fire becomes domineering. Leadership is imposed rather than earned; boldness becomes ego. Those who follow do so out of fear or habit, not inspiration. Real leadership comes from clarity of purpose and genuine respect for those you lead.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Wands14.jpg",
        "flavour": "Vision without execution is hallucination. Vision with it is transformation.",
    },

    # ── CUPS ─────────────────────────────────────────────────────────────────
    {
        "id": 36,
        "name": "Ace of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "Ace",
        "keywords_upright": ["new love", "compassion", "creativity", "overwhelming feeling", "new beginnings"],
        "keywords_reversed": ["emotional loss", "blocked creativity", "emptiness", "repression"],
        "meaning_short": "The cup overflows. Open your heart — love and feeling are here.",
        "meaning_full": "A cup overflows with water, a dove descending above it. The Ace of Cups is the pure beginning of emotional experience — new love, creative inspiration, compassion welling up from somewhere deep. The universe is offering emotional abundance. The only requirement is being open to receiving it.",
        "meaning_reversed_short": "Emotional blockage or emptiness. Something is preventing the cup from filling.",
        "meaning_reversed_full": "Reversed, the Ace of Cups' gift is blocked or refused. You may be closed off from love, creativity, or emotional nourishment — by past wounds, fear of vulnerability, or simple exhaustion. What would it take to open even slightly?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Cups01.jpg",
        "flavour": "The cup doesn't ask who deserves filling.",
    },
    {
        "id": 37,
        "name": "Two of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "2",
        "keywords_upright": ["unified love", "partnership", "mutual attraction", "connection"],
        "keywords_reversed": ["disharmony", "imbalance", "broken bonds", "disconnection"],
        "meaning_short": "A deep connection forms. Partnership built on genuine mutual recognition.",
        "meaning_full": "Two figures exchange cups — a bond of equals, a connection that sees and is seen. The Two of Cups is the moment of true meeting: romantic, platonic, or professional. What matters is the mutuality. This card blesses genuine partnerships where both parties bring their whole selves and receive the same in return.",
        "meaning_reversed_short": "Imbalance in a relationship. One person giving more; bonds strained.",
        "meaning_reversed_full": "Reversed, the Two of Cups reveals imbalance — one person more invested, love becoming need, or a bond dissolving. Something that once felt mutual now feels one-sided. Name it honestly before it becomes irreparable.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Cups02.jpg",
        "flavour": "To be truly seen and to truly see — that is the whole thing.",
    },
    {
        "id": 38,
        "name": "Three of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "3",
        "keywords_upright": ["celebration", "friendship", "creativity", "community", "reunion"],
        "keywords_reversed": ["overindulgence", "gossip", "isolation", "cancelled celebrations"],
        "meaning_short": "Gather with your people. Joy is multiplied when shared.",
        "meaning_full": "Three figures dance, cups raised in a garden in bloom. The Three of Cups is friendship, celebration, and the specific joy of being with people who truly know you. This card is a reminder that connection and pleasure are not frivolous — they are essential. Gather. Celebrate. Let yourself be held by your community.",
        "meaning_reversed_short": "Overindulgence or social friction. A celebration that doesn't feel celebratory.",
        "meaning_reversed_full": "Reversed, the Three of Cups' joy turns sour — through excess, gossip, exclusion, or a gathering that feels hollow. There may be drama in your social circles that needs addressing, or a pattern of using celebration to avoid something real.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Cups03.jpg",
        "flavour": "Joy shared is joy doubled.",
    },
    {
        "id": 39,
        "name": "Four of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "4",
        "keywords_upright": ["apathy", "contemplation", "reevaluation", "disconnection", "meditation"],
        "keywords_reversed": ["new perspective", "opportunity arising", "emerging from withdrawal"],
        "meaning_short": "A new offer sits right there — but you're staring inward. Look up.",
        "meaning_full": "A figure sits under a tree, arms crossed, staring at three cups on the ground — missing the fourth cup being extended by a cloud-hand. The Four of Cups is the mood of apathy or discontent: blessings unnoticed, opportunities unseen. Sometimes introspection is needed; sometimes it becomes avoidance. Notice what is being offered before dismissing it.",
        "meaning_reversed_short": "Emerging from apathy. Seeing an opportunity that was there all along.",
        "meaning_reversed_full": "Reversed, the Four of Cups signals a shift — out of the fog of discontentment and into awareness of what's available. A new perspective arrives. You're finally willing to look at what you've been ignoring. Something good has been waiting.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/35/Cups04.jpg",
        "flavour": "The gift was always there. You just weren't looking at it.",
    },
    {
        "id": 40,
        "name": "Five of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "5",
        "keywords_upright": ["grief", "loss", "regret", "sorrow", "disappointment"],
        "keywords_reversed": ["acceptance", "moving on", "recovery", "finding peace"],
        "meaning_short": "Grief is real — but two cups still stand behind you.",
        "meaning_full": "A figure in a dark cloak stares at three spilled cups, back turned to two still standing. The Five of Cups acknowledges real loss and real grief — don't rush past it. But when you're ready: turn around. What remains is not nothing. Mourning is appropriate; staying turned to the spillage forever is not.",
        "meaning_reversed_short": "Beginning to turn toward what remains. Grief lifting, recovery starting.",
        "meaning_reversed_full": "Reversed, the Five of Cups shows a shift in focus — from what was lost toward what remains. Healing is beginning, though it is not yet complete. Acceptance does not mean the loss didn't matter. It means you've chosen to keep living.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Cups05.jpg",
        "flavour": "Turn around. You are not as alone in this as you feel.",
    },
    {
        "id": 41,
        "name": "Six of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "6",
        "keywords_upright": ["nostalgia", "innocence", "joy", "childhood", "reunion"],
        "keywords_reversed": ["living in the past", "naivety", "unrealistic idealism"],
        "meaning_short": "A sweet return. Nostalgia, old connections, or innocent joy.",
        "meaning_full": "A child offers a cup of flowers to another in a peaceful village. The Six of Cups is innocence, memory, and the simple joy of things uncomplicated. This may indicate a reunion with an old friend, a return to something meaningful from your past, or simply an invitation to remember what it felt like before everything got complicated.",
        "meaning_reversed_short": "Stuck in the past or naivety preventing clear-eyed action.",
        "meaning_reversed_full": "Reversed, the Six of Cups' nostalgia becomes a prison. Living in the past, idealising what was, or refusing to grow beyond old patterns. The past was not as simple as memory suggests. There is more here — let yourself find it.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/17/Cups06.jpg",
        "flavour": "Not every gift needs to be complicated.",
    },
    {
        "id": 42,
        "name": "Seven of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "7",
        "keywords_upright": ["choices", "fantasy", "illusion", "wishful thinking", "imagination"],
        "keywords_reversed": ["clarity", "choosing", "sobriety", "overcoming illusion"],
        "meaning_short": "Too many options, too much fantasy. Get real and choose one path.",
        "meaning_full": "Cups overflow with visions — castles, dragons, jewels, shrouded figures. The Seven of Cups is the paralysis of infinite possibility: when everything seems achievable in the imagination and nothing gets done in reality. Beautiful possibilities, yes — but which one are you actually willing to commit to? Dreaming is not deciding.",
        "meaning_reversed_short": "The fog clears. Seeing clearly and finally choosing.",
        "meaning_reversed_full": "Reversed, the Seven of Cups' illusions dissolve — fantasy gives way to clear-eyed reality. You are finally able to choose rather than drift among possibilities. This may feel like a loss of magic, but it is the beginning of real momentum.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Cups07.jpg",
        "flavour": "Every path not chosen is a dream you release. That's not tragedy — it's focus.",
    },
    {
        "id": 43,
        "name": "Eight of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "8",
        "keywords_upright": ["walking away", "disillusionment", "leaving behind", "seeking deeper meaning"],
        "keywords_reversed": ["avoidance", "fear of moving on", "trying again"],
        "meaning_short": "Something no longer serves you. Leave it behind and seek what does.",
        "meaning_full": "A figure walks away from eight neatly stacked cups and into the mountains under a partial moon. The Eight of Cups is one of the most honest cards in the deck: it acknowledges when something — a relationship, a career, a life chapter — has run its course, even if it isn't broken. Walking away from what no longer fulfils you is not failure. It is wisdom.",
        "meaning_reversed_short": "Staying when you know you should leave — or leaving too soon.",
        "meaning_reversed_full": "Reversed, the Eight of Cups signals a failure to walk away from what is already over, or an abandonment driven by avoidance rather than clarity. Are you staying in something because it's genuinely worth staying in — or because leaving feels too hard?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/60/Cups08.jpg",
        "flavour": "Sometimes leaving is the most honest thing you can do.",
    },
    {
        "id": 44,
        "name": "Nine of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "9",
        "keywords_upright": ["contentment", "satisfaction", "gratitude", "wish fulfilled", "luxury"],
        "keywords_reversed": ["inner unhappiness", "materialism", "smugness", "unfulfilled wish"],
        "meaning_short": "The wish card. Something you deeply wanted is manifesting.",
        "meaning_full": "A satisfied figure sits before nine golden cups, arms crossed. The Nine of Cups is known as the wish card — something you have genuinely hoped for is coming or has come. Allow yourself contentment. Don't immediately reach for the next thing. Gratitude is not passivity — it is the fullest way to receive what you've been given.",
        "meaning_reversed_short": "The wish came with strings. Inner satisfaction is harder to find than expected.",
        "meaning_reversed_full": "Reversed, the Nine of Cups reveals that getting what you wanted hasn't brought the peace you expected. Material success or wish fulfillment leaves a gap. What were you actually looking for behind the thing you thought you wanted?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/24/Cups09.jpg",
        "flavour": "Let yourself have it.",
    },
    {
        "id": 45,
        "name": "Ten of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "10",
        "keywords_upright": ["divine love", "harmony", "family", "lasting happiness", "community"],
        "keywords_reversed": ["broken home", "disconnection", "misaligned values"],
        "meaning_short": "The fullest kind of happiness — shared, lasting, and real.",
        "meaning_full": "A family stands beneath a rainbow of cups, arms raised. The Ten of Cups is emotional completion — the happiness that comes not from achievement but from deep belonging. Family, true friendship, a home that is genuinely that. This kind of joy is not dramatic. It is quiet, steady, and profoundly real.",
        "meaning_reversed_short": "Family discord or the gap between an ideal and a reality.",
        "meaning_reversed_full": "Reversed, the Ten of Cups' picture-perfect vision is disrupted by real cracks — discord in the home, misaligned values in a relationship, or the painful gap between what family could be and what it is. Honesty, not idealism, is the path forward.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/84/Cups10.jpg",
        "flavour": "The rainbow doesn't require anything from you. It just is.",
    },
    {
        "id": 46,
        "name": "Page of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "Page",
        "keywords_upright": ["creative beginnings", "intuitive messages", "curiosity", "wonder"],
        "keywords_reversed": ["emotional immaturity", "creative block", "bad news"],
        "meaning_short": "A message from the heart. Creative and intuitive energy arriving.",
        "meaning_full": "The Page of Cups stares in delighted surprise at a fish emerging from their cup. This is the energy of creative innocence and emotional openness — intuitive messages, unexpected inspiration, the willingness to be surprised by your own inner life. Follow the strange and beautiful thing that just surfaced.",
        "meaning_reversed_short": "Emotional immaturity or a creative impulse not yet ready to be born.",
        "meaning_reversed_full": "Reversed, the Page of Cups energy becomes immature or blocked. Emotions may be all over the place — not integrated, just felt and expressed without discernment. Or a creative project is stuck before it began. Give the feeling room to settle before acting on it.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Cups11.jpg",
        "flavour": "The fish didn't ask permission to appear.",
    },
    {
        "id": 47,
        "name": "Knight of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "Knight",
        "keywords_upright": ["romance", "charm", "imagination", "following the heart", "messenger"],
        "keywords_reversed": ["moodiness", "unrealistic idealism", "jealousy", "manipulation"],
        "meaning_short": "A romantic or creative pursuit. Follow the beautiful vision — thoughtfully.",
        "meaning_full": "The Knight of Cups rides calmly, cup held out as an offering — a dreamer in motion. This card signals romantic pursuit, creative quests, or simply the call to follow what moves you emotionally. The Knight charms everyone they meet. Just ensure the dream they're chasing is real.",
        "meaning_reversed_short": "Idealism turning to mood swings or manipulation. Check the fantasy.",
        "meaning_reversed_full": "Reversed, the Knight of Cups' beauty curdles into unrealistic idealism, moody emotional storms, or manipulation dressed as romance. The vision is compelling — but is it real? Is this person (or this version of you) actually following their heart, or creating a story to avoid reality?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Cups12.jpg",
        "flavour": "Offer the cup. But look at what's inside it first.",
    },
    {
        "id": 48,
        "name": "Queen of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "Queen",
        "keywords_upright": ["compassion", "caring", "emotional security", "intuition", "inner feelings"],
        "keywords_reversed": ["emotional insecurity", "co-dependency", "self-pity", "manipulation"],
        "meaning_short": "Lead with compassion and deep intuition. Hold space with wisdom.",
        "meaning_full": "The Queen of Cups sits at the water's edge, gazing at a closed ornate cup. She feels everything deeply — but does not drown in it. This is emotional mastery: profound empathy without loss of self. Be the one who holds space today. Lead with your heart without abandoning your centre.",
        "meaning_reversed_short": "Emotional codependency or insecurity ruling your interactions.",
        "meaning_reversed_full": "Reversed, the Queen's deep feeling becomes entanglement. Emotional boundaries dissolve; empathy becomes people-pleasing or emotional manipulation. Self-pity may be present. Reconnect with your own emotional centre — separate from everyone else's feelings.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Cups13.jpg",
        "flavour": "To hold space is not to carry someone's pain. It is to stand with them in it.",
    },
    {
        "id": 49,
        "name": "King of Cups",
        "arcana": "minor",
        "suit": "cups",
        "number": "King",
        "keywords_upright": ["emotional balance", "compassion", "diplomacy", "wisdom"],
        "keywords_reversed": ["emotional manipulation", "moodiness", "volatility", "coldness"],
        "meaning_short": "Emotional mastery. Lead with heart and wisdom in balance.",
        "meaning_full": "The King of Cups sits on a throne amid turbulent seas — utterly calm. Emotional intelligence here is sovereign: the ability to feel deeply while remaining grounded, to lead with compassion without losing authority. This is the energy of the therapist, the wise mentor, the leader who holds steady in emotional storms.",
        "meaning_reversed_short": "Emotional manipulation or instability. The calm surface hiding volatility.",
        "meaning_reversed_full": "Reversed, the King of Cups' mastery collapses. Emotional volatility, manipulation, or a cruel coldness emerge from beneath the composed exterior. There may be addiction, repression, or an abuse of emotional authority. The surface calm is a performance — what is underneath?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/04/Cups14.jpg",
        "flavour": "The sea rages. The king remains.",
    },

    # ── SWORDS ───────────────────────────────────────────────────────────────
    {
        "id": 50,
        "name": "Ace of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "Ace",
        "keywords_upright": ["breakthrough", "clarity", "sharp mind", "truth", "new idea"],
        "keywords_reversed": ["confusion", "brutality", "chaos", "poor communication"],
        "meaning_short": "Clarity cuts through. A breakthrough in thought or communication arrives.",
        "meaning_full": "A sword thrusts from a cloud, crowned with laurels. The Ace of Swords is the gift of mental clarity — a breakthrough, a sudden seeing-through, the right words finally arriving. This is the moment when confusion falls away and truth stands exposed. Use this clarity while it's sharp.",
        "meaning_reversed_short": "Mental fog or brutal truths delivered without care.",
        "meaning_reversed_full": "Reversed, the Ace of Swords cuts poorly — truth delivered as a weapon, mental confusion clouding what should be clear, or a breakthrough that backfires due to poor timing. Clarity without compassion is just cruelty. Sharpen the thought, but soften the delivery.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Swords01.jpg",
        "flavour": "Truth is the sharpest thing.",
    },
    {
        "id": 51,
        "name": "Two of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "2",
        "keywords_upright": ["difficult choices", "stalemate", "blocked emotions", "avoidance"],
        "keywords_reversed": ["indecision", "confusion", "information overload", "no right answer"],
        "meaning_short": "A decision is being avoided. Lower the swords — you already know.",
        "meaning_full": "A blindfolded figure holds two crossed swords over her heart, back to the sea. The Two of Swords is deliberate not-deciding: a stalemate, an avoidance of a painful choice. The blindfold is chosen — to not see is to not have to decide. But the decision still waits. When you're ready to lower the swords, what do you already know?",
        "meaning_reversed_short": "Information overload making a hard decision harder. Or finally choosing.",
        "meaning_reversed_full": "Reversed, the Two of Swords tips into paralysis from too much information, or finally breaks the stalemate. If clarity is arriving — trust it. If confusion is deepening — step back from the data and ask what you feel.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Swords02.jpg",
        "flavour": "The blindfold is not protection. It is postponement.",
    },
    {
        "id": 52,
        "name": "Three of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "3",
        "keywords_upright": ["heartbreak", "grief", "separation", "sorrow", "painful truth"],
        "keywords_reversed": ["recovery", "forgiveness", "repressing grief", "releasing pain"],
        "meaning_short": "The pain is real. Let yourself grieve without it becoming your identity.",
        "meaning_full": "Three swords pierce a heart in a stormy sky. The Three of Swords does not soften: there is grief here, heartbreak, a painful truth that cuts clean through. This card asks you to feel it rather than intellectualise it. The storm passes. The swords do not stay. But they must be acknowledged before they can be removed.",
        "meaning_reversed_short": "Grief lifting, or grief being suppressed to avoid feeling it.",
        "meaning_reversed_full": "Reversed, the Three of Swords signals either healing from grief or a refusal to let pain surface. Suppressed heartbreak doesn't heal — it waits. If you have been 'fine' through something that wasn't fine, it may be time to finally feel it.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Swords03.jpg",
        "flavour": "You can survive being broken. Most people have.",
    },
    {
        "id": 53,
        "name": "Four of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "4",
        "keywords_upright": ["rest", "restoration", "contemplation", "recovery", "stillness"],
        "keywords_reversed": ["restlessness", "burnout", "refusing to rest", "forced stillness"],
        "meaning_short": "Rest is not defeat. Stop — you need it.",
        "meaning_full": "A knight lies in repose, hands in prayer, beneath a stained-glass window. One sword hangs — three rest on the wall. The Four of Swords commands: rest. Not as a reward, but as medicine. You cannot keep going at this pace. The body and mind require stillness to integrate what they've been through. Step away.",
        "meaning_reversed_short": "Burnout from refusing to rest, or finally returning after needed recovery.",
        "meaning_reversed_full": "Reversed, the Four of Swords shows rest refused or broken by restlessness. You may be pushing through exhaustion because stopping feels like failure. Or you have rested and are ready to re-emerge. Know which one is true.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Swords04.jpg",
        "flavour": "The sword on the wall is there for when you're ready. It will wait.",
    },
    {
        "id": 54,
        "name": "Five of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "5",
        "keywords_upright": ["conflict", "defeat", "winning at all costs", "betrayal"],
        "keywords_reversed": ["reconciliation", "aftermath of conflict", "releasing the grudge"],
        "meaning_short": "Someone won — but at what cost? Victory here may not be worth it.",
        "meaning_full": "A figure gathers fallen swords while two others walk away in defeat. The Five of Swords shows a win — but one that cost relationships, reputation, or self-respect. Was it worth it? This card asks whether the fight was actually necessary, and whether the manner of winning served anyone at all.",
        "meaning_reversed_short": "Aftermath of conflict. Choosing reconciliation over pride.",
        "meaning_reversed_full": "Reversed, the Five of Swords moves past the conflict — either toward genuine reconciliation or a lingering, festering aftermath. If the fight is over: what can be repaired? If it isn't: is continuing this battle serving anything real?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Swords05.jpg",
        "flavour": "Not every battle is worth fighting. Not every win is worth having.",
    },
    {
        "id": 55,
        "name": "Six of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "6",
        "keywords_upright": ["transition", "change", "moving on", "releasing the past", "calmer waters"],
        "keywords_reversed": ["stuck", "can't move on", "turbulence", "unfinished business"],
        "meaning_short": "Moving away from what hurt you. Calmer waters ahead.",
        "meaning_full": "A family crosses to calmer waters by boat. Swords remain — the troubles are not forgotten, but they are no longer the whole horizon. The Six of Swords is gentle transition: not triumphant, not painless, but forward. You are moving toward something better, even if the grief of leaving is still present.",
        "meaning_reversed_short": "Stuck in rough waters. Transition blocked or delayed.",
        "meaning_reversed_full": "Reversed, the Six of Swords shows a transition that hasn't happened yet — or one that keeps being attempted but blocked. Unresolved past keeps pulling the boat back to shore. What is keeping you from moving on?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/29/Swords06.jpg",
        "flavour": "The water ahead is calmer. You are allowed to move toward it.",
    },
    {
        "id": 56,
        "name": "Seven of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "7",
        "keywords_upright": ["deception", "strategy", "cunning", "getting away with something"],
        "keywords_reversed": ["conscience", "caught", "coming clean", "truth surfacing"],
        "meaning_short": "Someone is not being fully honest — possibly you.",
        "meaning_full": "A figure sneaks away from a camp with five swords, leaving two behind. The Seven of Swords is the card of strategic deception — someone taking what they can and hoping no one notices. This may be you operating in survival mode; it may be someone around you. Either way, examine where honesty has been sacrificed for convenience.",
        "meaning_reversed_short": "The deception comes to light. Coming clean or being caught.",
        "meaning_reversed_full": "Reversed, the Seven of Swords' trickery unravels. What was hidden surfaces; what was taken must be accounted for. This can be a release — the weight of deception is exhausting. Coming clean, even when it's hard, is almost always lighter than carrying the secret.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Swords07.jpg",
        "flavour": "The stolen swords are never really yours.",
    },
    {
        "id": 57,
        "name": "Eight of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "8",
        "keywords_upright": ["restriction", "imprisonment", "helplessness", "self-imposed limitations"],
        "keywords_reversed": ["releasing restriction", "new perspective", "self-acceptance"],
        "meaning_short": "You are more free than you believe. The cage is partly in your mind.",
        "meaning_full": "A blindfolded figure stands amid a ring of swords, bound but not secured. The ground is clear; they could walk away. The Eight of Swords is self-imposed limitation — the belief that you are trapped when you are not, the blindfold of fear or past conditioning. Remove the blindfold. Test the binds. You may be freer than you think.",
        "meaning_reversed_short": "Releasing self-imposed restriction. The blindfold coming off.",
        "meaning_reversed_full": "Reversed, the Eight of Swords begins to loosen. The blindfold slips; you see the path out. This is the beginning of genuine liberation — not from circumstance, but from the story you've been telling about it.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Swords08.jpg",
        "flavour": "The swords are real. The imprisonment is a choice.",
    },
    {
        "id": 58,
        "name": "Nine of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "9",
        "keywords_upright": ["anxiety", "worry", "nightmares", "despair", "overwhelm"],
        "keywords_reversed": ["hopelessness", "depression", "healing", "reaching out"],
        "meaning_short": "The 3am mind. The fears are not facts — but they feel like it.",
        "meaning_full": "A figure sits up in bed, head in hands, nine swords hanging above them in the dark. The Nine of Swords is the nightmare: the anxiety spiral, the 3am catastrophising, the weight of worry that won't lift. The swords hang — they don't fall. The fear is real; the disaster it predicts may not be. You are not alone in the dark.",
        "meaning_reversed_short": "The worst fears slowly releasing. Or bottoming out before healing.",
        "meaning_reversed_full": "Reversed, the Nine of Swords either deepens into full depression — the worst fear realising — or finally begins to lift as dawn arrives. Reaching out, speaking the fear aloud to someone safe, is the most powerful thing available to you right now.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Swords09.jpg",
        "flavour": "The night is darkest just before it isn't anymore.",
    },
    {
        "id": 59,
        "name": "Ten of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "10",
        "keywords_upright": ["painful ending", "betrayal", "collapse", "rock bottom", "inevitable conclusion"],
        "keywords_reversed": ["recovery", "regeneration", "resisting the inevitable end"],
        "meaning_short": "Rock bottom — but also the end of that particular fall.",
        "meaning_full": "A figure lies face-down, ten swords in their back, but the dawn breaks golden at the horizon. The Ten of Swords is rock bottom — but it is also, definitively, the bottom. You cannot fall further from here. And notice: it is dawn. The worst has happened. Now the only direction is up. The ending, however painful, is also the end of the worst of it.",
        "meaning_reversed_short": "Slow recovery from collapse. Or clinging to what has already ended.",
        "meaning_reversed_full": "Reversed, the Ten of Swords either shows early recovery — the dawn after the devastation — or a desperate clinging to what has already ended, prolonging the pain unnecessarily. Something is over. Let it be over.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Swords10.jpg",
        "flavour": "You cannot fall further than the bottom. And look — dawn.",
    },
    {
        "id": 60,
        "name": "Page of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "Page",
        "keywords_upright": ["curiosity", "restlessness", "mental agility", "questioning"],
        "keywords_reversed": ["all talk", "haste", "deception", "scatteredness"],
        "meaning_short": "Sharp curiosity and quick thinking. Ask the hard questions.",
        "meaning_full": "The Page of Swords leaps forward, sword raised, eyes alert. This is the energy of restless intellectual curiosity — the one who asks too many questions, who notices what others miss, who is quick to speak and quick to learn. Channel this energy into genuine inquiry rather than argument for its own sake.",
        "meaning_reversed_short": "All talk, no follow-through. Quick thinking becoming hasty mistakes.",
        "meaning_reversed_full": "Reversed, the Page of Swords' quick mind becomes a problem — gossip, hasty words, decisions made without enough thought. The sharpness cuts the wrong things. Slow down the mind long enough to aim.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Swords11.jpg",
        "flavour": "The sharpest minds know when to sheathe the blade.",
    },
    {
        "id": 61,
        "name": "Knight of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "Knight",
        "keywords_upright": ["ambition", "action", "drive", "direct", "authoritative"],
        "keywords_reversed": ["no direction", "disregard for consequences", "burn everything down"],
        "meaning_short": "Charge with purpose and clarity. Speed and directness are assets here.",
        "meaning_full": "The Knight of Swords races at full gallop into a storm, sword forward. This is the energy of pure directed action — fast, sharp, and absolutely committed. When the direction is right, this energy is unstoppable. Be sure you know where you're going before you ride at this speed.",
        "meaning_reversed_short": "Charging without direction. Burning things down with no regard for consequences.",
        "meaning_reversed_full": "Reversed, the Knight of Swords' speed becomes destruction without purpose. Actions are taken that cannot be undone; words are said that cannot be recalled. The speed needs a map. Pause — however briefly — before the next charge.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b0/Swords12.jpg",
        "flavour": "The fastest rider wins nothing if they don't know the destination.",
    },
    {
        "id": 62,
        "name": "Queen of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "Queen",
        "keywords_upright": ["clear boundaries", "direct communication", "independent thought", "objectivity"],
        "keywords_reversed": ["coldness", "bitterness", "cruel words", "isolation"],
        "meaning_short": "Clear-eyed and sharp-tongued. Truth, boundaries, and independence.",
        "meaning_full": "The Queen of Swords sits upright, one hand raised in welcome, sword vertical — both open and precise. She has known loss; it has made her wise rather than bitter. This is the energy of someone who speaks truth clearly, holds boundaries without apology, and thinks for herself. Lead with clarity today.",
        "meaning_reversed_short": "Bitterness or cruelty masked as honesty. Old wounds controlling present choices.",
        "meaning_reversed_full": "Reversed, the Queen of Swords' clarity becomes coldness. Truths are delivered as weapons; independence becomes isolation; old pain shapes every new interaction. The sharp mind is in service of the wounded heart. What would healing look like, rather than protection?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Swords13.jpg",
        "flavour": "Clarity is not cruelty. But cruelty sometimes wears its face.",
    },
    {
        "id": 63,
        "name": "King of Swords",
        "arcana": "minor",
        "suit": "swords",
        "number": "King",
        "keywords_upright": ["intellectual power", "authority", "truth", "clear thinking", "decisiveness"],
        "keywords_reversed": ["manipulative", "tyrannical", "cold-hearted", "dishonest authority"],
        "meaning_short": "Reason and authority. Think clearly, decide decisively, speak truth.",
        "meaning_full": "The King of Swords sits at attention, sword upright, eyes forward. He is the master of the mind — analytical, just, decisive, and authoritative. When this energy is called for, inhabit it fully: think before speaking, speak precisely, and hold the line on truth even when it's uncomfortable.",
        "meaning_reversed_short": "Authority corrupted. Reason weaponised. Manipulation dressed as logic.",
        "meaning_reversed_full": "Reversed, the King of Swords' intellect serves ego rather than truth. Logic is used to justify what is unjust; authority is wielded without wisdom. There may be a figure in your life whose reasonable exterior conceals cruelty or manipulation. Trust your gut alongside their words.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/33/Swords14.jpg",
        "flavour": "The mind is a tool. What it's used for is always a choice.",
    },

    # ── PENTACLES ─────────────────────────────────────────────────────────────
    {
        "id": 64,
        "name": "Ace of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "Ace",
        "keywords_upright": ["new opportunity", "prosperity", "abundance", "manifestation", "security"],
        "keywords_reversed": ["missed opportunity", "poor planning", "greed", "unstable foundation"],
        "meaning_short": "A new material opportunity. Grasp it — abundance wants to begin.",
        "meaning_full": "A hand extends from a cloud holding a single golden pentacle over a lush garden. The Ace of Pentacles is the seed of material abundance — a new job, investment, project, or resource appearing. This is the universe offering tangible support. Reach for it. Plant it. Tend it. It will grow.",
        "meaning_reversed_short": "A material opportunity missed or squandered. Reassess the foundations.",
        "meaning_reversed_full": "Reversed, the Ace of Pentacles' gift is lost through poor planning, greed, or simply not noticing it was there. An opportunity may have slipped by, or the foundations of a new venture are shaky. Return to basics: what is actually needed for this to be stable?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/fd/Pents01.jpg",
        "flavour": "The seed doesn't know it's a forest yet.",
    },
    {
        "id": 65,
        "name": "Two of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "2",
        "keywords_upright": ["balance", "adaptability", "time management", "priorities"],
        "keywords_reversed": ["imbalance", "disorganised", "overwhelmed", "overcommitted"],
        "meaning_short": "Juggling multiple demands. You can do it — but something may need to give.",
        "meaning_full": "A figure dances, juggling two pentacles in a figure-eight loop. Ships rise and fall on waves behind them. The Two of Pentacles is the managed chaos of a full life: balancing work, finances, relationships, and health simultaneously. You are doing more than you should, and somehow doing it. But watch the juggling — if one more ball goes up, something falls.",
        "meaning_reversed_short": "The juggling is failing. Overwhelm, disorganisation, or too many commitments.",
        "meaning_reversed_full": "Reversed, the Two of Pentacles shows the juggling act collapsing. Too many priorities, not enough resources — or an inability to prioritise at all. Something has to be set down. What is the one thing you must keep moving?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Pents02.jpg",
        "flavour": "You can't juggle everything. But you can choose which ball matters most.",
    },
    {
        "id": 66,
        "name": "Three of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "3",
        "keywords_upright": ["teamwork", "collaboration", "learning", "skill", "building"],
        "keywords_reversed": ["disharmony", "poor teamwork", "lack of skill", "apathy"],
        "meaning_short": "Skilled collaboration. The work is better because you're doing it together.",
        "meaning_full": "An apprentice works on a cathedral while two clergy consult the plans. The Three of Pentacles is the card of skilled collaboration: each person's contribution makes the whole greater. This is not the time for solo pride — the work is genuinely improved by bringing others in, by listening to expertise, by doing the thing with care.",
        "meaning_reversed_short": "Poor teamwork or lack of applied skill holding the work back.",
        "meaning_reversed_full": "Reversed, the Three of Pentacles signals collaboration that isn't working — competing visions, poor communication, or a lack of real commitment to the craft. What would it take to get everyone genuinely pulling in the same direction?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Pents03.jpg",
        "flavour": "The cathedral was not built alone.",
    },
    {
        "id": 67,
        "name": "Four of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "4",
        "keywords_upright": ["security", "control", "conserving resources", "stability", "scarcity mindset"],
        "keywords_reversed": ["releasing control", "generosity", "financial instability"],
        "meaning_short": "Holding tight. Security is real — but don't let fear of losing make you rigid.",
        "meaning_full": "A figure clutches four pentacles — two under feet, one in hands, one on crown — unable to move. The Four of Pentacles is stability achieved through fierce holding. The security is real, but the grip may be too tight. Savings, boundaries, and caution have value. But when does protection become stagnation?",
        "meaning_reversed_short": "Releasing the grip. Generosity, or financial instability requiring it.",
        "meaning_reversed_full": "Reversed, the Four of Pentacles either releases into generosity and flow — a healthy letting go — or tips into genuine financial instability that forces it. Examine whether you're holding out of genuine need or out of fear.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/35/Pents04.jpg",
        "flavour": "What are you afraid will happen if you open your hands?",
    },
    {
        "id": 68,
        "name": "Five of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "5",
        "keywords_upright": ["hardship", "poverty", "lack", "isolation", "not seeing help available"],
        "keywords_reversed": ["recovery", "returning stability", "charity accepted"],
        "meaning_short": "Hardship is real — but you may be missing the help that is available.",
        "meaning_full": "Two figures struggle through snow past a lit church window. The Five of Pentacles speaks to genuine material or spiritual poverty — difficult times, feeling left out in the cold. But the window is lit; help is present if you can bring yourself to look up and ask. Pride or shame may be keeping you from the support that exists.",
        "meaning_reversed_short": "Recovery beginning. Help being accepted or stability slowly returning.",
        "meaning_reversed_full": "Reversed, the Five of Pentacles signals improvement — the hardship is lifting, or you are finally accepting the help available. Recovery after difficult times is not linear, but momentum is beginning. Let yourself receive.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/96/Pents05.jpg",
        "flavour": "The window is lit. You just have to look up.",
    },
    {
        "id": 69,
        "name": "Six of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "6",
        "keywords_upright": ["generosity", "charity", "giving", "receiving", "fairness"],
        "keywords_reversed": ["strings attached", "power imbalance", "one-sided generosity"],
        "meaning_short": "The flow of giving and receiving. Are you in balance — or in debt?",
        "meaning_full": "A wealthy figure distributes coins to two kneeling figures while holding a balance scale. The Six of Pentacles asks about the flow of resources: who is giving, who is receiving, and whether the exchange is genuinely fair. Generosity is beautiful — but examine the power dynamics in your giving and receiving.",
        "meaning_reversed_short": "Generosity with strings. Power imbalance in giving or receiving.",
        "meaning_reversed_full": "Reversed, the Six of Pentacles' generosity becomes transactional or coercive. There are strings attached to what is given; the help comes at a hidden cost. Or the giving is one-sided in a way that is draining. Examine what is really being exchanged.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Pents06.jpg",
        "flavour": "Generosity changes its character when it expects something back.",
    },
    {
        "id": 70,
        "name": "Seven of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "7",
        "keywords_upright": ["perseverance", "investment", "long-term view", "patience", "growth"],
        "keywords_reversed": ["impatience", "little reward for effort", "lack of growth"],
        "meaning_short": "A long investment. Patience — what you're growing takes time.",
        "meaning_full": "A farmer leans on a hoe, surveying a crop that is not yet ripe. The Seven of Pentacles is the long game: the slow, patient investment in something whose returns won't come immediately. The work is real; the growth is happening. You just can't see it yet. This is not failure — this is process.",
        "meaning_reversed_short": "Effort without return. Reassess where your energy is going.",
        "meaning_reversed_full": "Reversed, the Seven of Pentacles signals effort that isn't being rewarded as hoped. The crop may not be growing well; the investment may be in the wrong soil. Is the long-term strategy sound? Or is this patience being confused with stubbornness about a failing plan?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Pents07.jpg",
        "flavour": "The harvest isn't ready yet. That doesn't mean it's failing.",
    },
    {
        "id": 71,
        "name": "Eight of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "8",
        "keywords_upright": ["diligence", "skill development", "mastery", "attention to detail"],
        "keywords_reversed": ["perfectionism", "misdirected effort", "lack of ambition"],
        "meaning_short": "Head down, craft forward. Excellence is built one repetition at a time.",
        "meaning_full": "A craftsman sits alone, carving pentacle after pentacle. The Eight of Pentacles is the card of dedicated skill-building: the long hours alone with the work, the willingness to repeat and refine, the joy of craft for its own sake. Mastery is not talent — it is showing up and doing the work, again and again. This card honours that.",
        "meaning_reversed_short": "Perfectionism blocking progress. Or misdirected effort in the wrong area.",
        "meaning_reversed_full": "Reversed, the Eight of Pentacles tips into perfectionism that prevents completion, or diligence applied to the wrong craft entirely. The work ethic is real — but is it pointed at the right thing? Is the pursuit of perfection preventing anything from being finished?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Pents08.jpg",
        "flavour": "Mastery is just repetition that cares.",
    },
    {
        "id": 72,
        "name": "Nine of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "9",
        "keywords_upright": ["luxury", "self-sufficiency", "financial independence", "achievement"],
        "keywords_reversed": ["financial dependence", "materialism without fulfilment", "over-investment in work"],
        "meaning_short": "You built this. Stand in the abundance you created — it's real.",
        "meaning_full": "A woman stands alone in a lush vineyard, a falcon on her wrist. The Nine of Pentacles is the card of earned, enjoyed abundance — someone who built something beautiful through their own effort and now inhabits it with genuine satisfaction. You don't have to diminish what you've created. Let yourself enjoy what you earned.",
        "meaning_reversed_short": "Abundance that doesn't satisfy, or dependence undermining self-sufficiency.",
        "meaning_reversed_full": "Reversed, the Nine of Pentacles' success feels hollow, or is revealed to be built on shaky ground. Material comfort hasn't produced the fulfilment it promised. Or dependence — on a person, a system, or old comforts — is preventing the genuine self-sufficiency you crave.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Pents09.jpg",
        "flavour": "You built this garden. You're allowed to walk in it.",
    },
    {
        "id": 73,
        "name": "Ten of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "10",
        "keywords_upright": ["legacy", "family wealth", "long-term success", "stability", "tradition"],
        "keywords_reversed": ["family conflict", "broken legacy", "instability", "short-term thinking"],
        "meaning_short": "The long view. Legacy, lasting abundance, and what you're building beyond yourself.",
        "meaning_full": "An old figure sits surrounded by family, dogs at his feet, beneath a tree heavy with pentacles. The Ten of Pentacles is the card of legacy — the abundance that extends beyond yourself, through generations, through community, through work that outlasts the moment. What are you building that will matter beyond your own life?",
        "meaning_reversed_short": "Family conflict disrupting what was built. Short-term thinking threatening long-term stability.",
        "meaning_reversed_full": "Reversed, the Ten of Pentacles shows the family foundation fracturing — through conflict, short-sightedness, or a failure to steward what was inherited. The legacy is at risk. What is the pattern or decision that is threatening the long-term? It is not too late to course-correct.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Pents10.jpg",
        "flavour": "Build something that will outlast the moment.",
    },
    {
        "id": 74,
        "name": "Page of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "Page",
        "keywords_upright": ["manifestation", "financial opportunity", "skill development", "new ambition"],
        "keywords_reversed": ["lack of progress", "procrastination", "learn from failure"],
        "meaning_short": "A new ambition takes root. Study, plan, and begin — methodically.",
        "meaning_full": "The Page of Pentacles holds a pentacle before them in wonder — studying it, turning it, learning what it is made of. This card begins a new material pursuit: a new area of study, a financial goal, a skill being built from scratch. The Page is a slow, thorough learner. Be methodical. Be patient. This one will compound.",
        "meaning_reversed_short": "Procrastination or a promising start that hasn't gone anywhere.",
        "meaning_reversed_full": "Reversed, the Page of Pentacles gets stuck in the looking rather than the doing. The ambition is there but the action isn't. Alternatively, a promising venture has stalled. What is the smallest possible next concrete step?",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Pents11.jpg",
        "flavour": "You have to start before you're ready.",
    },
    {
        "id": 75,
        "name": "Knight of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "Knight",
        "keywords_upright": ["efficiency", "routine", "conservatism", "methodical", "determined"],
        "keywords_reversed": ["laziness", "boredom", "obsessive routine", "stagnation"],
        "meaning_short": "Slow and steady builds the thing. Trust the method.",
        "meaning_full": "The Knight of Pentacles sits still on a heavy horse, a pentacle in hand — not charging, but considering. This is the most deliberate of knights: methodical, reliable, hardworking, and not remotely interested in shortcuts. The work will be done correctly. It may take longer. It will be worth it.",
        "meaning_reversed_short": "Routine becoming rut. Laziness or obsessive perfectionism blocking progress.",
        "meaning_reversed_full": "Reversed, the Knight of Pentacles' reliability becomes rigidity. The routine that was productive has become a trap; the methodical approach has collapsed into procrastination or obsessive perfectionism. Movement is required — even imperfect movement.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Pents12.jpg",
        "flavour": "Slow is not the opposite of progress.",
    },
    {
        "id": 76,
        "name": "Queen of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "Queen",
        "keywords_upright": ["practicality", "creature comforts", "financial security", "nurturing", "abundance"],
        "keywords_reversed": ["self-neglect", "financial insecurity", "smothering", "materialism"],
        "meaning_short": "Practical abundance. Nurture yourself and others from a full cup.",
        "meaning_full": "The Queen of Pentacles sits in a lush garden, a pentacle in her lap, a rabbit at her feet. She is earthy, warm, practical, and generous — someone who creates beauty and comfort as naturally as breathing. This is the energy of the nurturer who also takes care of themselves: abundance shared without depletion.",
        "meaning_reversed_short": "Self-neglect or financial anxiety disrupting the ability to nurture.",
        "meaning_reversed_full": "Reversed, the Queen of Pentacles' practical warmth falters. Self-neglect may have run the cup dry; or the nurturing has become smothering. Financial anxiety may be pulling focus from what truly matters. Replenish yourself before trying to nourish anyone else.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/88/Pents13.jpg",
        "flavour": "The most generous gardens are the ones that are also tended.",
    },
    {
        "id": 77,
        "name": "King of Pentacles",
        "arcana": "minor",
        "suit": "pentacles",
        "number": "King",
        "keywords_upright": ["abundance", "prosperity", "security", "ambition", "discipline"],
        "keywords_reversed": ["materialism", "corruption", "stubbornness", "poor financial decisions"],
        "meaning_short": "Mastery of the material. Wealth earned, stability built, prosperity held.",
        "meaning_full": "The King of Pentacles sits on a throne decorated with bulls, his garden abundant around him. He has built what he has through discipline, patience, and strategic thinking — and he holds it wisely. This card says: trust your material instincts. Your abundance is earned. Protect and grow it with the same diligence that created it.",
        "meaning_reversed_short": "Materialism or corruption. Wealth used to control rather than create.",
        "meaning_reversed_full": "Reversed, the King of Pentacles' mastery becomes greed, stubbornness, or financial mismanagement. Wealth may be pursued at the cost of everything else, or used as a tool of control. Examine whether material security has become the whole of the story — and what has been sacrificed for it.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Pents14.jpg",
        "flavour": "The richest thing you own is what you've built by hand.",
    },
]

# Build lookup structures
CARD_BY_ID = {c["id"]: c for c in CARDS}
MAJOR_ARCANA = [c for c in CARDS if c["arcana"] == "major"]
MINOR_ARCANA = [c for c in CARDS if c["arcana"] == "minor"]
WANDS = [c for c in CARDS if c["suit"] == "wands"]
CUPS = [c for c in CARDS if c["suit"] == "cups"]
SWORDS = [c for c in CARDS if c["suit"] == "swords"]
PENTACLES = [c for c in CARDS if c["suit"] == "pentacles"]

SUIT_MAP = {
    "wands": WANDS,
    "cups": CUPS,
    "swords": SWORDS,
    "pentacles": PENTACLES,
    "major": MAJOR_ARCANA,
    "minor": MINOR_ARCANA,
}
