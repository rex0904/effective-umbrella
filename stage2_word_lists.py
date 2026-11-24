"""
STAGE 2: Break the sentence into a list of words
================================================
Stage 1's bug: "hi" matched inside "this". The fix: split what the user types
into a LIST of whole words, then look each word up in a DICTIONARY of topics
(see RESPONSES in persona.py).

Run it:   python stage2_word_lists.py
"""

import random
import string

from chat_loop import run_chat
from persona import RESPONSES, DEFAULT_RESPONSES


def clean_words(text):
    """Turn 'I LOVE School!!' into the list ['i', 'love', 'school']."""
    text = text.lower()
    for ch in string.punctuation:       # remove . , ! ? and friends
        text = text.replace(ch, "")
    return text.split()                 # split on spaces -> list of words


def get_reply(user_input):
    """The bot's brain: take the user's text, return a reply (a string)."""
    words = clean_words(user_input)
    topics = []

    for word in words:
        if word in RESPONSES:
            topics.append(word)

    if topics:
        chosen_topic = random.choice(topics)
        return random.choice(RESPONSES[chosen_topic])

    return random.choice(DEFAULT_RESPONSES)
            # TODO 2: What if the user mentions TWO topics ("school and sports")?
            # Right now the bot only answers the FIRST one. Could you collect
            # all the topics in a list instead, and then pick one at random?

    return random.choice(DEFAULT_RESPONSES)


if __name__ == "__main__":
    # (This line means: only start chatting when you run THIS file directly.
    #  Later stages import functions from this file, and we don't want the
    #  chat to start by accident when they do.)
    run_chat(get_reply)


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# TODO 1: Open persona.py and add at least 5 new topics to RESPONSES, each with
#         3+ replies. Run the bot and test every one.
#
# CHECKPOINT: type "this is hard". Does the bot still say "Hello"? (It should
#             not. Why is that fixed now?)
#
# Because clean_words() splits the sentence into individual words.
#
# THINK: type "I love my mom". The bot ignores "mom". Why? How could we teach
#        it that "mom" belongs with "family"? (Stage 4 answers this.)
#
# The bot ignores "mom" because it is not currently a key in the RESPONSES dictionary. To teach it that "mom" belongs with "family", we would need to create a connection between related words