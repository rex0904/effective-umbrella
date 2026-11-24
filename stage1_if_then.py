"""
STAGE 1: if / elif / else
=========================
Goal: a bot that reacts to a few things you type.

Run it:   python stage1_if_then.py
Quit it:  type  bye
"""

from safety import check_safety   # a safety net added by your teacher. Leave it.

BOT_NAME = "Dr. Byte"   # TODO 1: give your bot a name

print(f"{BOT_NAME}: Hello. Tell me what is on your mind. (type 'bye' to leave)")

while True:
    # .lower() turns "HELLO" into "hello" so we only have to check one spelling
    user_input = input("You: ").lower()

    safety_message = check_safety(user_input)
    if safety_message:
        print(f"{BOT_NAME}: {safety_message}")
        continue

    if user_input == "bye":
        print(f"{BOT_NAME}: Goodbye. Take care.")
        break
    elif "hello" in user_input or "hi" in user_input:
        print(f"{BOT_NAME}: Hello! How are you feeling today?")
    elif "sad" in user_input:
        print(f"{BOT_NAME}: I am sorry to hear that. Why do you feel sad?")
    elif "school" in user_input:
        print(f"{BOT_NAME}: Tell me more about school.")
    elif "sports" in user_input:
        print(f"{BOT_NAME}: What sports do you enjoy playing?")
    elif "happy" in user_input:
        print(f"{BOT_NAME}: That's great! What made you happy?")
    elif "tired" in user_input:
        print(f"{BOT_NAME}: Have you been getting enough sleep?")
    # TODO 2: add at least 3 more `elif` rules about topics YOU choose.
    # TODO 3: make one of your rules react to TWO different words (use `or`).
    else:
        print(f"{BOT_NAME}: Please go on.")


# ---------------------------------------------------------------------------
# BUG HUNT (do this after your TODOs)
# ---------------------------------------------------------------------------
# Run the bot and type:   this is hard
# Why does the bot say "Hello!"?  (Hint: what does `"hi" in "this"` give you?)
# Write your guess here:
#
# The bot says "Hello!" because "hi" is contained inside the word "this".
#
# We will fix this properly in Stage 2 by breaking the sentence into WORDS.
