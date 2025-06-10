import streamlit as st

TANGRAMS = {
    1: {"shapes": ["triangle", "square"], "target": "arrow"},
    2: {"shapes": ["triangle", "square", "parallelogram"], "target": "house"},
    3: {"shapes": ["triangle", "triangle", "square"], "target": "boat"},
    4: {"shapes": ["triangle", "triangle", "square", "parallelogram"], "target": "cat"},
    5: {"shapes": ["triangle", "square", "triangle", "parallelogram"], "target": "rocket"},
    6: {"shapes": ["triangle", "triangle", "triangle", "square", "parallelogram"], "target": "bird"},
    7: {"shapes": ["triangle", "square", "square", "parallelogram"], "target": "fish"},
    8: {"shapes": ["triangle", "parallelogram", "square", "triangle", "triangle"], "target": "rabbit"},
    9: {"shapes": ["triangle", "parallelogram", "square", "triangle", "square"], "target": "tree"},
    10: {"shapes": ["triangle", "triangle", "parallelogram", "square", "triangle"], "target": "plane"},
    11: {"shapes": ["triangle", "square", "triangle", "triangle", "parallelogram", "square"], "target": "duck"},
    12: {"shapes": ["triangle", "triangle", "square", "square", "parallelogram"], "target": "swan"},
    13: {"shapes": ["triangle", "parallelogram", "triangle", "triangle", "square", "square"], "target": "horse"},
    14: {"shapes": ["triangle", "triangle", "triangle", "square", "parallelogram", "triangle"], "target": "fox"},
    15: {"shapes": ["triangle", "square", "triangle", "triangle", "parallelogram", "square", "triangle"], "target": "person"},
}

def run_puzzle(level=1):
    st.title("Tangram AI 🧩")
    st.write(f"Difficulty Level: {level}")

    puzzle = TANGRAMS.get(level, TANGRAMS[15])
    shapes = puzzle["shapes"]
    target = puzzle["target"]

    st.subheader(f"Available Shapes: {', '.join(shapes)}")
    st.write("🧩 Guess the shape formed from these parts.")

    guess = st.text_input("Your Answer (e.g., cat, rocket, swan)").strip().lower()

    if guess:
        if guess == target:
            st.success("🎉 Correct!")
            return "correct"
        else:
            st.error("❌ Incorrect. Try again.")
