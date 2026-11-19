"""
safety.py  --  TEACHER-MAINTAINED. Please do not edit or delete.

Our bots are programs, not counselors. If someone types something that sounds
like they might be in danger, the bot stops "riffing" and points to real help.
Every stage file uses this.
"""

DANGER_PHRASES = [
    "kill myself",
    "hurt myself",
    "want to die",
    "suicide",
    "self harm",
    "self-harm",
    "end it all",
    "don't want to be here",
]

SAFETY_MESSAGE = (
    "That sounds really serious, and I am only a computer program. "
    "Please talk to a trusted adult right now, like a parent, a teacher, or a "
    "school counselor. In the U.S. you can also call or text 988 at any time."
)


def check_safety(text):
    """Return the safety message if the text sounds worrying, otherwise None."""
    text = text.lower()
    for phrase in DANGER_PHRASES:
        if phrase in text:
            return SAFETY_MESSAGE
    return None
