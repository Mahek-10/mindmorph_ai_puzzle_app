import streamlit as st

TANGRAMS = {
    1: {
        "shapes": ["triangle", "square", "parallelogram"],
        "target": "house"
    },
    2: {
        "shapes": ["triangle", "triangle", "square", "parallelogram"],
        "target": "cat"
    },
    3: {
        "shapes": ["triangle", "square", "triangle", "parallelogram", "triangle"],
        "target": "rocket"
    }
}

def run_puzzle(level=1):
    st.title("Tangram AI 🧩")
    st.write(f"Difficulty Level: {level}")

    puzzle = TANGRAMS.get(level if level <= 3 else 3)
    shapes = puzzle["shapes"]
    target = puzzle["target"]

    st.subheader(f"Available Shapes: {', '.join(shapes)}")
    st.write(f"🧩 Can you guess the shape formed?")

    guess = st.text_input("Your Answer (e.g., house, cat, rocket)")

    if guess:
        if guess.strip().lower() == target:
            st.success("🎉 Correct!")
        else:
            st.error("❌ Incorrect. Try again.")
