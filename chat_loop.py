"""
chat_loop.py  --  the "plumbing" for Stages 2-5.

In Stage 1 you wrote the chat loop yourself. From Stage 2 on, this file runs
the loop for you (typing, quitting, safety check) so you can focus on the
bot's BRAIN: a function called get_reply().

You do not need to edit this file.
"""

from persona import BOT_NAME, GREETING, FAREWELL
from safety import check_safety


def run_chat(get_reply):
    """Keep chatting until the user says bye. `get_reply` is a function that
    takes the user's text and returns the bot's reply (a string)."""
    print(f"{BOT_NAME}: {GREETING.format(name=BOT_NAME)} (type 'bye' to leave)")
    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            break

        safety_message = check_safety(user_input)
        if safety_message:
            print(f"{BOT_NAME}: {safety_message}")
            continue

        if user_input.strip().lower() in ("bye", "quit", "exit"):
            print(f"{BOT_NAME}: {FAREWELL}")
            break

        print(f"{BOT_NAME}: {get_reply(user_input)}")
