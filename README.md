# Build Your Own Chatbot 🤖

In this lab you'll build a chatbot in the style of **Dr. Sbaitso** (1991) and **ELIZA** (1966): a bot that keeps a conversation going by picking out the important word in what you say and riffing on it. You'll start with plain `if` statements and finish with a bot that **writes its own sentences** using n-grams, the simplest ancestor of today's AI chatbots.

You are not just filling in blanks. Your bot's name, personality, vocabulary, and sense of humor are **yours** to design.

---

## 1. Open your coding environment (Codespaces)

1. Make sure you are signed in to GitHub.
2. On this repository's page, click the green **Code** button → **Codespaces** tab → **Create codespace on main**.
3. Wait about a minute. A coding window (VS Code in your browser) opens with this README and `stage1_if_then.py`.
4. To run a file, open the **Terminal** panel at the bottom and type, for example:
   ```
   python stage1_if_then.py
   ```
5. When you're done for the day: click the blue **Codespaces** button at the bottom-left → **Stop Current Codespace**. (This saves your computing time. Your work is kept.)

> ⚠️ **Never delete earlier stage files.** Later stages borrow functions from them.

---

## 2. The five stages

| Stage | File | New idea | Your bot can... |
|---|---|---|---|
| 1 | `stage1_if_then.py` | `if / elif / else`, `input()`, loops | react to a few exact phrases |
| 2 | `stage2_word_lists.py` | lists, dictionaries, `random.choice` | recognize topic **words** and vary its answers |
| 3 | `stage3_important_word.py` | functions, stop words, string templates | pick the important word and riff on it |
| 4 | `stage4_topics_memory.py` | word groups, pronoun swapping, memory | understand "mom" means *family*, flip "I/my" to "you/your", and remember |
| 5 | `stage5_ngrams.py` | n-grams, probability, files | **generate new sentences** it learned from a text file |

Work in order. Each file has `TODO` markers and a **CHECKPOINT** at the bottom. Show your teacher each checkpoint before moving on.

### Where your creativity goes
- **`persona.py`**: your bot's name, topics, replies, templates, and word groups. *Most of your creative work happens here.*
- **`corpus.txt`**: (Stage 5) the text your bot learns to talk like.

### Files you don't need to edit
`chat_loop.py` (runs the chat for you) and `safety.py` (a safety net, see below).

---

## 3. How to know it's working

Every stage has a CHECKPOINT. Here's the idea of what to look for:

- **Stage 1:** the bot answers your rules, and you can explain the "this is hard → Hello!" bug.
- **Stage 2:** the bug is gone, and you have 5+ new topics.
- **Stage 3:** type any weird sentence. The bot grabs a sensible word and asks about it.
- **Stage 4:** `I am nervous about the dance` → *"Why do you say you are nervous about the dance?"*
- **Stage 5:** type `/peek school` to see what the bot learned, then watch it write sentences you never typed.

## 4. Stuck?

1. Read the **red error message** from the bottom up. The last line says what went wrong.
2. Check your **indentation** (spaces at the start of lines) and your **colons** `:`.
3. Add a `print()` to see what a variable holds, e.g. `print(words)`.
4. Ask a classmate to explain *what they think the line does*. Then ask your teacher.

## 5. About the safety net

Your bot is a *program*, not a counselor. `safety.py` makes every stage respond to worrying messages by pointing to real people who can help. Please leave it alone and don't try to get your bot to give advice about serious problems.

## 6. Final showcase

Prepare a 3-minute demo: your bot's name and personality, one thing you're proud of in `persona.py`, one funny or surprising reply, and one thing the bot gets **wrong** and why. 🎤
