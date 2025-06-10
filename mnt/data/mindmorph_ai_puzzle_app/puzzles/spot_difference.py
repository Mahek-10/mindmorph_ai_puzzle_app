
import streamlit as st

DIFFERENCES = {
    1: {
        "image1": "🙂🙂🙂😃🙂",
        "image2": "🙂🙂🙂🙂🙂",
        "diff": 4
    },
    2: {
        "image1": "🐶🐶🐱🐶🐶",
        "image2": "🐶🐶🐶🐶🐶",
        "diff": 3
    },
    3: {
        "image1": "🍎🍏🍎🍎🍎",
        "image2": "🍎🍎🍎🍎🍎",
        "diff": 2
    },
    4: {
        "image1": "🌟🌟🌟✨🌟",
        "image2": "🌟🌟🌟🌟🌟",
        "diff": 4
    },
    5: {
        "image1": "🎈🎈🎉🎈🎈",
        "image2": "🎈🎈🎈🎈🎈",
        "diff": 3
    }
}

def run_puzzle(level=1):
    st.title("Spot the Difference 🧩")
    st.write(f"Difficulty Level: {level}")

    puzzle = DIFFERENCES.get(level if level <= 5 else 5)
    st.subheader("Image A:")
    st.write(puzzle["image1"])
    st.subheader("Image B:")
    st.write(puzzle["image2"])

    guess = st.number_input("What is the position of the difference (1-based)?", min_value=1, max_value=5, step=1)

    if st.button("Check"):
        if guess == puzzle["diff"]:
            st.success("🎉 Correct! You spotted the difference.")
        else:
            st.error("❌ Nope, try again.")
