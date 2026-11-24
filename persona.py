"""
persona.py  --  YOUR BOT'S PERSONALITY LIVES HERE.

This file is only data: a name, phrases, and word lists. You will edit it in
every stage. The more creative you get here, the more your bot feels like a
real character (a sarcastic coach? a pirate? a robot who loves pizza?).

Other files borrow this data with an import, like:
    from persona import BOT_NAME
"""

# ---------------------------------------------------------------------------
# BASICS
# ---------------------------------------------------------------------------
BOT_NAME = "Dr. Byte"  # TODO: rename your bot!

GREETING = "Hello, I am {name}. Tell me what is on your mind."
FAREWELL = "Goodbye. It was nice talking with you."

# ---------------------------------------------------------------------------
# STAGE 2: topic words and the replies the bot can choose from.
# Format:  "word the user types": ["reply 1", "reply 2", ...]
# TODO: add at least 5 topics of your own!
# ---------------------------------------------------------------------------
RESPONSES = {
    "school": [
        "What part of school is on your mind?",
        "Is school getting easier or harder lately?",
        "Tell me about your favorite class. Or your least favorite.",
    ],
    "family": [
        "Tell me more about your family.",
        "How do you get along with your family?",
        "Who in your family do you talk to the most?",
    ],
    "sports": [
        "What do you love most about playing sports?",
        "Do you play better alone or with a team?",
        "What is the hardest part of training?",
    ],
    "sad": [
        "I am sorry you feel that way. What happened?",
        "When did you start feeling sad?",
        "Is there anything that usually cheers you up?",
    ],
    "happy": [
        "That is great! What made you happy?",
        "Tell me more about what is going well.",
    ],
    "computer": [
        "Do you like working with computers?",
        "What would you build if you could build anything?",
    ],
    "food": [
        "What is your favorite meal?",
        "Do you cook, or do you just eat?",
    ],
    "friends": [
        "What do you like most about your friends?",
        "Do your friends feel the same way?",
    ],
        "music": [
        "What kind of music do you listen to?",
        "Do you have a favorite song?"
    ],

    "games": [
        "What is your favorite video game?",
        "Do you prefer playing alone or with friends?"
    ],

    "movies": [
        "What is your favorite movie?",
        "Do you prefer action or comedy movies?",
    ],

    "sleep": [
        "Do you usually get enough sleep?",
        "What time do you normally go to bed?",
    ],

    "travel": [
        "Where would you like to travel?",
        "What is the best place you have ever visited?"
    ]
}

DEFAULT_RESPONSES = [
    "Please go on.",
    "I see. Tell me more.",
    "Interesting. Why do you say that?",
    "How does that make you feel?",
]

# ---------------------------------------------------------------------------
# STAGE 3: words too boring to "riff" on, and templates to riff with.
# {word} gets replaced by the important word the bot found.
# TODO: add more stop words and at least 5 templates of your own.
# ---------------------------------------------------------------------------
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "so", "if", "of", "to", "in", "on",
    "at", "for", "with", "about", "as", "by", "from", "up", "out",
    "i", "me", "my", "mine", "you", "your", "we", "our", "they", "them",
    "he", "she", "it", "its", "his", "her", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "do", "does", "did",
    "have", "has", "had", "will", "would", "can", "could", "just", "very",
    "really", "not", "no", "yes", "like", "get", "got", "im", "dont", "its",
    "what", "when", "why", "how", "who", "there", "here", "then", "than",
}

RIFF_TEMPLATES = [
    "Tell me more about {word}.",
    "Why does {word} matter to you?",
    "How does {word} make you feel?",
    "What comes to mind when you think about {word}?",
    "Let's talk about {word}. What happened?",
    "Is {word} something you think about often?",
]

# ---------------------------------------------------------------------------
# STAGE 4: pronoun swapping, and groups of related words.
# ---------------------------------------------------------------------------
REFLECTIONS = {
    "i": "you",
    "me": "you",
    "my": "your",
    "mine": "yours",
    "myself": "yourself",
    "am": "are",
    "you": "I",
    "your": "my",
    "are": "am",
}

# Each topic (a key from RESPONSES) lists words that should ALL trigger it.
# This is a hand-made version of "words that mean similar things".
# TODO: add more words to every group, and add groups for your new topics.
TOPIC_GROUPS = {
    "family": ["family", "mom", "mother", "dad", "father", "parents", "sister", "brother"],
    "school": ["school", "homework", "teacher", "class", "test", "exam", "grade", "grades"],
    "sports": ["sports", "wrestling", "soccer", "football", "practice", "game", "team", "coach"],
    "sad": ["sad", "unhappy", "upset", "down", "gloomy", "miserable"],
    "happy": ["happy", "excited", "glad", "cheerful", "thrilled"],
    "computer": ["computer", "code", "coding", "python", "laptop", "program", "robot"],
    "food": ["food", "pizza", "hungry", "dinner", "lunch", "snack", "cooking"],
    "friends": ["friends", "friend", "buddy", "classmates"],
}
