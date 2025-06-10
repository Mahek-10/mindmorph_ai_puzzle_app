
import streamlit as st

PUZZLES = {
    1: {
        "clues": [
            "Alice likes apples.",
            "Bob doesn't like bananas.",
            "Cathy likes cherries."
        ],
        "question": "Who likes bananas?",
        "answer": "None"
    },
    2: {
        "clues": [
            "Tom sits left of Jerry.",
            "Spike is not next to Tom.",
            "Tyke sits right of Jerry."
        ],
        "question": "Who is between Tom and Tyke?",
        "answer": "Jerry"
    },
    3: {
        "clues": [
            "Red lives in the first house.",
            "Blue lives next to Green.",
            "Green is not in the third house."
        ],
        "question": "What color is in the second house?",
        "answer": "Green"
    },
    # Add more puzzles as needed
}

def run_puzzle(level=1):
    st.title("Logic Grid 🧩")
    st.write(f"Difficulty Level: {level}")

    puzzle = PUZZLES.get(level, PUZZLES[1])

    st.subheader("Clues")
    for clue in puzzle["clues"]:
        st.write(f"- {clue}")

    user_answer = st.text_input("🧠 " + puzzle["question"])

    if user_answer:
        if user_answer.strip().lower() == puzzle["answer"].lower():
            st.success("🎉 Correct!")
        else:
            st.error("❌ Try again.")
