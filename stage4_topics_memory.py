"""
STAGE 4: Related words, pronoun swapping, and memory
====================================================
Three upgrades that make the bot feel a lot smarter:

  A. TOPIC GROUPS   "mom", "dad", "sister" all mean the topic "family".
  B. REFLECTION     "I hate my homework" -> "Why do you say you hate your homework?"
  C. MEMORY         Remember earlier important words and circle back to them.

Run it:   python stage4_topics_memory.py
"""

import random

from chat_loop import run_chat
from persona import RESPONSES, DEFAULT_RESPONSES, RIFF_TEMPLATES, REFLECTIONS, TOPIC_GROUPS
from stage2_word_lists import clean_words
from stage3_important_word import find_important_word

remembered = []     # important words from earlier in the conversation


# ---------------------------------------------------------------------------
# A. Topic groups (this is a hand-made version of "words that mean similar things")
# ---------------------------------------------------------------------------
def find_topic(words):
    """Return the topic name (a key of RESPONSES) if any word belongs to a
    group in TOPIC_GROUPS, otherwise None."""
    for topic, group in TOPIC_GROUPS.items():
        for word in words:
            if word in group:
                return topic
    return None


# ---------------------------------------------------------------------------
# B. Reflection
# ---------------------------------------------------------------------------
def reflect(words):
    """Swap perspective: ['i', 'am', 'sad'] -> 'you are sad'."""
    # TODO 1: Right now this just glues the words back together unchanged.
    #   Build a new list called `swapped`. For each word: if it is a key in
    #   REFLECTIONS, add REFLECTIONS[word]; otherwise add the word itself.
    #   Then return " ".join(swapped).
    return " ".join(words)


# ---------------------------------------------------------------------------
# The brain
# ---------------------------------------------------------------------------
def get_reply(user_input):
    words = clean_words(user_input)
    important = find_important_word(words)

    # C. Memory: save this turn's important word for later
    if important is not None:
        remembered.append(important)

    # TODO 2 (memory callback): every so often, bring up something from earlier.
    #   Fill in the blank so the bot picks a RANDOM old word (not just the first).
    if len(remembered) >= 3 and random.random() < 0.25:
        old_word = remembered[0]      # <- TODO: use random.choice on remembered[:-1]
        return f"Earlier you mentioned {old_word}. Does that connect to this?"

    # Topic groups first
    topic = find_topic(words)
    if topic is not None:
        return random.choice(RESPONSES[topic])

    # Reflection: when the user is talking about themselves
    if ("i" in words or "my" in words) and len(words) >= 3:
        return f"Why do you say {reflect(words)}?"

    # Riff on the important word
    if important is not None:
        return random.choice(RIFF_TEMPLATES).format(word=important)

    return random.choice(DEFAULT_RESPONSES)


if __name__ == "__main__":
    run_chat(get_reply)


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# TODO 3: Expand TOPIC_GROUPS in persona.py. Add 5+ words to every group and
#         create groups for your own topics (don't forget matching RESPONSES!).
#
# CHECKPOINT: type "I am nervous about the dance". Is the reply grammatical?
#   Now type "I hate my homework". Why did you get a DIFFERENT kind of reply?
#   (Hint: look at the ORDER of the rules in get_reply. Order matters!)
#
# THINK (this is the big idea behind word2vec): you just typed lists of words
#   that "mean the same thing" BY HAND. What if a program could LEARN those
#   groups by reading millions of sentences? Your teacher will discuss this.
#
# CHALLENGE 1: Don't let the memory callback repeat the same old word twice.
# CHALLENGE 2: Add a mood tracker: count how many "sad" topics vs "happy"
#   topics came up, and have the bot comment when the conversation turns.
