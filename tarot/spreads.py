"""
Spread definitions and atmospheric flavour text for the Tarot cog.
"""

# ------------------------------------------------------------------ #
#  Spread Definitions
# ------------------------------------------------------------------ #

SPREADS = {
    "three_card": {
        "name": "Past · Present · Future",
        "description": "A classic three-card spread illuminating the arc of your situation.",
        "positions": [
            {
                "name": "Past",
                "description": "What has led you here. The energy or events behind this situation.",
            },
            {
                "name": "Present",
                "description": "Where you stand right now. The heart of the matter.",
            },
            {
                "name": "Future",
                "description": "Where this path leads if you continue as you are.",
            },
        ],
    },
    "celtic_cross": {
        "name": "Celtic Cross",
        "description": "The traditional ten-card spread for deep, comprehensive insight.",
        "positions": [
            {
                "name": "The Situation",
                "description": "The heart of the matter — what this reading centres on.",
            },
            {
                "name": "The Challenge",
                "description": "What crosses you. The immediate obstacle or opposing force.",
            },
            {
                "name": "Distant Past",
                "description": "The root cause. What lies beneath this situation.",
            },
            {
                "name": "Recent Past",
                "description": "Events that have recently influenced where you are.",
            },
            {
                "name": "Possible Future",
                "description": "What may come to pass if things continue on their current path.",
            },
            {
                "name": "Immediate Future",
                "description": "What is about to enter your life in the near term.",
            },
            {
                "name": "Your Inner State",
                "description": "How you feel about this situation — fears and internal resources.",
            },
            {
                "name": "External Influences",
                "description": "How others see this situation, or external forces at play.",
            },
            {
                "name": "Hopes & Fears",
                "description": "What you secretly hope for, or what you fear most.",
            },
            {
                "name": "Outcome",
                "description": "The likely resolution if things continue as they are.",
            },
        ],
    },
    "relationship": {
        "name": "Relationship Spread",
        "description": "Explore the dynamics between yourself and another.",
        "positions": [
            {
                "name": "You",
                "description": "How you are showing up in this relationship.",
            },
            {
                "name": "Them",
                "description": "How the other person is showing up.",
            },
            {
                "name": "The Connection",
                "description": "The core energy between you.",
            },
            {
                "name": "The Challenge",
                "description": "What you are navigating together.",
            },
            {
                "name": "The Path Forward",
                "description": "What this relationship is moving toward.",
            },
        ],
    },
    "decision": {
        "name": "Decision Spread",
        "description": "Weigh two paths with clarity.",
        "positions": [
            {
                "name": "The Situation",
                "description": "The core of the decision you face.",
            },
            {
                "name": "Option A",
                "description": "The energy and likely outcome of the first path.",
            },
            {
                "name": "Option B",
                "description": "The energy and likely outcome of the second path.",
            },
            {
                "name": "What You're Missing",
                "description": "A hidden factor your conscious mind hasn't fully considered.",
            },
            {
                "name": "The Wisest Choice",
                "description": "Guidance on which path serves your highest good.",
            },
        ],
    },
    "shadow_work": {
        "name": "Shadow Work Spread",
        "description": "A deep dive into what hides in the unconscious.",
        "positions": [
            {
                "name": "The Shadow",
                "description": "What you have been suppressing or denying.",
            },
            {
                "name": "Its Origin",
                "description": "Where this shadow pattern began.",
            },
            {
                "name": "How It Manifests",
                "description": "How this shadow shows up in your life or behaviour.",
            },
            {
                "name": "The Gift Within",
                "description": "The strength or wisdom hidden inside this wound.",
            },
            {
                "name": "Integration",
                "description": "How to begin working with this part of yourself.",
            },
        ],
    },
    "year_ahead": {
        "name": "Year Ahead",
        "description": "Twelve cards — one for each month — with an overall theme.",
        "positions": [
            {"name": "Overall Theme", "description": "The overarching energy of your year."},
            {"name": "January", "description": ""},
            {"name": "February", "description": ""},
            {"name": "March", "description": ""},
            {"name": "April", "description": ""},
            {"name": "May", "description": ""},
            {"name": "June", "description": ""},
            {"name": "July", "description": ""},
            {"name": "August", "description": ""},
            {"name": "September", "description": ""},
            {"name": "October", "description": ""},
            {"name": "November", "description": ""},
            {"name": "December", "description": ""},
        ],
    },
}


# ------------------------------------------------------------------ #
#  Atmospheric Flavour Text
# ------------------------------------------------------------------ #

FLAVOUR_INTROS = [
    "The cards are shuffled. The veil thins.",
    "Something stirs at the edges of what is known.",
    "The cards do not predict — they reveal.",
    "Between what is and what may be, the cards speak.",
    "Still your mind. What wishes to be seen?",
    "The universe tends toward pattern. Attend to it.",
    "Not fortune-telling. Truth-telling.",
    "The symbols have waited long enough.",
    "Let what is hidden surface.",
    "There are no accidents in a tarot draw.",
    "The archetypes stir. What do they say to you?",
    "Every card drawn is a mirror.",
    "The cards speak in the language of the soul.",
    "Breathe. Then look.",
    "What you seek is also seeking you.",
    "The spread reflects what is already present within.",
    "Lay down what you think you know. The cards speak plainly.",
    "Even the darkness in these cards carries instruction.",
    "The shuffled deck does not lie — only the reader can lie to themselves.",
    "Today the veil between knowing and not-knowing is thin.",
]
