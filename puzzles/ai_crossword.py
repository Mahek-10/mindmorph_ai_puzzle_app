import streamlit as st

CROSSWORDS = {
    1: {"clue": "Opposite of day", "answer": "night"},
    2: {"clue": "A fruit that's also a color", "answer": "orange"},
    3: {"clue": "The 5th planet from the Sun", "answer": "jupiter"},
    4: {"clue": "Fastest land animal", "answer": "cheetah"},
    5: {"clue": "Capital of France", "answer": "paris"},
    6: {"clue": "Ocean between Africa and Australia", "answer": "indian"},
    7: {"clue": "Word for water in solid form", "answer": "ice"},
    8: {"clue": "Heaviest naturally occurring element", "answer": "uranium"},
    9: {"clue": "Another word for zero", "answer": "nought"},
    10: {"clue": "Comes after Wednesday", "answer": "thursday"},
    11: {"clue": "Currency of Japan", "answer": "yen"},
    12: {"clue": "An animal with tusks and a trunk", "answer": "elephant"},
    13: {"clue": "The red planet", "answer": "mars"},
    14: {"clue": "The opposite of cold", "answer": "hot"},
    15: {"clue": "A device to compute", "answer": "computer"}
}

def run_puzzle(level=1):
    st.title("AI Crossword 🧩")
    st.write(f"Difficulty Level: {level}")

    puzzle = CROSSWORDS.get(level, CROSSWORDS[1])
    st.write("🧩 Clue:", puzzle["clue"])

    guess = st.text_input("Your Answer")

    if guess:
        if user_answer.strip().lower() == answer:
    st.success("🎉 Correct!")
    return "correct"  # 👈 Add this line

        else:
            st.error("❌ Incorrect. Try again.")
