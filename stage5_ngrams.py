"""
STAGE 5: Predicting the next word with n-grams
==============================================
Until now every reply came from a template YOU wrote. Now the bot will
GENERATE new sentences by learning which words tend to follow which words in
a text file (corpus.txt).

  Bigram  (n=2): looks at 1 word  to predict the next one.
  Trigram (n=3): looks at 2 words to predict the next one.

This is the simplest ancestor of the language models behind modern chatbots:
"given the words so far, what word probably comes next?"

Run it:   python stage5_ngrams.py
Special command inside the chat:   /peek school    (shows what the model learned)
"""

import random
from collections import Counter

from chat_loop import run_chat
from stage2_word_lists import clean_words
from stage3_important_word import find_important_word
from stage4_topics_memory import find_topic, get_reply as rules_reply

N = 2   # TODO 3: change to 3 (trigrams). What happens to the sentences?


def load_corpus(path="corpus.txt"):
    """Read the text file and return a list of lines."""
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def build_model(lines, n=2):
    """Learn from the lines. Returns a dictionary:
         context (tuple of words)  ->  list of words that followed it

    For n=2 and the line "i like pizza", we learn:
         ("<start>",) -> ["i"]
         ("i",)       -> ["like"]
         ("like",)    -> ["pizza"]
         ("pizza",)   -> ["<end>"]
    """
    model = {}
    for line in lines:
        words = clean_words(line)
        tokens = ["<start>"] * (n - 1) + words + ["<end>"]
        for i in range(len(tokens) - (n - 1)):
            context = tuple(tokens[i : i + n - 1])
            next_word = tokens[i + n - 1]
            if context not in model:
                model[context] = []
            model[context].append(next_word)
    return model


def generate(model, n=2, seed=None, max_words=14):
    """Write a sentence one word at a time. If `seed` is given, start from a
    place where the seed word appears (so the bot 'riffs' on it)."""
    # choose a starting context
    starts = [c for c in model if seed is not None and seed in c]
    if starts:
        context = random.choice(starts)
    else:
        context = ("<start>",) * (n - 1)

    sentence = [w for w in context if w != "<start>"]

    while len(sentence) < max_words:
        options = model.get(context)
        if not options:
            break
        next_word = random.choice(options)     # TODO 1: see the challenge below
        if next_word == "<end>":
            break
        sentence.append(next_word)
        context = tuple(list(context)[1:] + [next_word])

    return " ".join(sentence).capitalize() + "."


def peek(model, word):
    """Show the most likely next words after `word` (bigram models only)."""
    options = model.get((word,))
    if not options:
        return f"I never saw '{word}' in my corpus."
    top = Counter(options).most_common(5)
    pieces = [f"{w} ({count})" for w, count in top]
    return f"After '{word}' I usually see: " + ", ".join(pieces)


MODEL = build_model(load_corpus(), N)


def get_reply(user_input):
    # special command for exploring the model
    if user_input.startswith("/peek"):
        parts = user_input.split()
        if len(parts) < 2:
            return "Try:  /peek school"
        return peek(build_model(load_corpus(), 2), parts[1].lower())

    words = clean_words(user_input)
    important = find_important_word(words)

    # Known topics still get the Stage 4 treatment.
    # Otherwise, 60% of the time, try to generate a brand-new sentence.
    no_topic = find_topic(words) is None
    seen_it = important is not None and any(important in c for c in MODEL)
    if no_topic and seen_it and random.random() < 0.6:
        return generate(MODEL, N, seed=important)

    return rules_reply(user_input)     # fall back to everything from Stage 4


if __name__ == "__main__":
    run_chat(get_reply)


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# TODO 1 (CHALLENGE): `random.choice(options)` treats every option equally, but
#   `options` contains repeats, so common words ARE more likely. Try picking
#   the MOST COMMON next word every time instead (hint: Counter(options)
#   .most_common(1)). What happens to the bot? Why is it boring now?
#
# TODO 2: Open corpus.txt and ADD 20+ lines in your bot's voice (jokes, advice,
#   catchphrases). Run it again. Your bot just learned a new personality
#   without you writing a single new if-statement.
#
# TODO 3: Set N = 3. Sentences should sound more natural but repeat the
#   corpus more. Why? (Hint: with 2 words of context, there are far fewer
#   possible next words.)
#
# THINK: What would happen if corpus.txt had 10 MILLION lines instead of 38?
#   What if it had your whole class's chat history? What new problems appear?
#
# SHOWCASE: Pick your best 3 minutes of conversation to show the class.
