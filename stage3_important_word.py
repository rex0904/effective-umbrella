"""
STAGE 3: Find the important word and riff on it
===============================================
Dr. Sbaitso and ELIZA could keep talking about almost anything with a simple
trick: pick one important word out of your sentence and ask about it.

Plan:
  1. If the user mentions a topic we know -> use the Stage 2 reply.
  2. Otherwise find the "important" word and plug it into a template:
         "Tell me more about {word}."

Run it:   python stage3_important_word.py
"""

import random

from chat_loop import run_chat
from persona import RESPONSES, DEFAULT_RESPONSES, STOP_WORDS, RIFF_TEMPLATES
from stage2_word_lists import clean_words   # reuse your Stage 2 function!


def find_important_word(words):
    """Return the most important word in the list, or None if there is none.

    VERSION 1 (works now): the first word that is not a boring stop word.
    """
    for word in words:
        if word not in STOP_WORDS:
            return word
    return None

    # TODO 1 (VERSION 2): "first word" is not always the best word.
    #   Change the function so it returns the LONGEST word that is not a stop
    #   word. Longer words are often more specific ("homework" vs "bad").
    #   Hint: keep a variable called `best` and update it inside the loop.
    #
    # TODO 2 (VERSION 3): invent your own scoring. For example: +2 points if
    #   the word is a key in RESPONSES, +1 point per letter over 5, -1 point
    #   if it appears in the first position. Highest score wins.


def get_reply(user_input):
    words = clean_words(user_input)

    # Step 1: known topic?
    for word in words:
        if word in RESPONSES:
            return random.choice(RESPONSES[word])

    # Step 2: riff on the important word
    important = find_important_word(words)
    if important is not None:
        template = random.choice(RIFF_TEMPLATES)
        return template.format(word=important)

    # Step 3: nothing useful
    return random.choice(DEFAULT_RESPONSES)


if __name__ == "__main__":
    run_chat(get_reply)


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# TODO 3: Add 5+ templates of your own to RIFF_TEMPLATES in persona.py.
#         Make them sound like YOUR bot's personality.
#
# TODO 4: Add 10+ stop words to STOP_WORDS. Try typing sentences and watch for
#         boring words the bot riffs on ("Tell me more about really...").
#
# CHECKPOINT: type "my teacher assigned a gigantic project".
#   Which word did your bot pick? Is that the word YOU would have picked?
#
# CHALLENGE: The bot sometimes uses the same template twice in a row. Keep a
#   variable called `last_template` and make sure the bot picks a different one.
