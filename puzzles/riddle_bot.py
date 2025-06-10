import streamlit as st

RIDDLES = [
    ("What has keys but can't open locks?", "keyboard"),
    ("What runs but never walks?", "water"),
    ("What has a face and hands but no arms or legs?", "clock"),
    ("What can travel around the world while staying in a corner?", "stamp"),
    ("What has to be broken before you can use it?", "egg"),
    ("What gets wetter the more it dries?", "towel"),
    ("What has a neck but no head?", "bottle"),
    ("What comes once in a minute, twice in a moment, but never in a thousand years?", "m"),
    ("What has an eye but cannot see?", "needle"),
    ("What has many teeth but can’t bite?", "comb"),
    ("What gets bigger the more you take away?", "hole"),
    ("The more of me you take, the more you leave behind. What am I?", "footsteps"),
    ("I’m tall when I’m young, and I’m short when I’m old. What am I?", "candle"),
    ("What belongs to you, but other people use it more than you do?", "name"),
    ("What is full of holes but still holds water?", "sponge")
]

def run_puzzle(level=1):
    st.title("Riddle Bot 🤖")
    st.write(f"Difficulty Level: {level}")

    if level > len(RIDDLES):
        st.warning("No more riddles at this level.")
        return

    riddle, answer = RIDDLES[level - 1]
    st.write("🧠", riddle)

    user_answer = st.text_input("Your Answer").strip().lower()
    if user_answer:
        if user_answer == answer:
           if user_answer.strip().lower() == answer:
    st.success("🎉 Correct!")
    return "correct"  # 👈 Add this line

        else:
            st.error("❌ Try again!")
