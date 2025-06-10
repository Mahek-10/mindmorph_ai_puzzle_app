import streamlit as st

DIFFERENCES = {
    1: {"image1": "🙂🙂🙂😃🙂", "image2": "🙂🙂🙂🙂🙂", "diff": 4},
    2: {"image1": "🐶🐶🐱🐶🐶", "image2": "🐶🐶🐶🐶🐶", "diff": 3},
    3: {"image1": "🍎🍏🍎🍎🍎", "image2": "🍎🍎🍎🍎🍎", "diff": 2},
    4: {"image1": "🌟🌟🌟✨🌟", "image2": "🌟🌟🌟🌟🌟", "diff": 4},
    5: {"image1": "🎈🎈🎉🎈🎈", "image2": "🎈🎈🎈🎈🎈", "diff": 3},
    6: {"image1": "👀👀👁️👀👀", "image2": "👀👀👀👀👀", "diff": 3},
    7: {"image1": "🍔🍔🍟🍔🍔", "image2": "🍔🍔🍔🍔🍔", "diff": 3},
    8: {"image1": "🚗🚗🚙🚗🚗", "image2": "🚗🚗🚗🚗🚗", "diff": 3},
    9: {"image1": "🌈🌈☁️🌈🌈", "image2": "🌈🌈🌈🌈🌈", "diff": 3},
    10: {"image1": "📚📚📖📚📚", "image2": "📚📚📚📚📚", "diff": 3},
    11: {"image1": "🧊🧊🧊❄️🧊", "image2": "🧊🧊🧊🧊🧊", "diff": 4},
    12: {"image1": "🎃🎃👻🎃🎃", "image2": "🎃🎃🎃🎃🎃", "diff": 3},
    13: {"image1": "📦📦📬📦📦", "image2": "📦📦📦📦📦", "diff": 3},
    14: {"image1": "🐸🐸🦎🐸🐸", "image2": "🐸🐸🐸🐸🐸", "diff": 3},
    15: {"image1": "🦄🦄🐴🦄🦄", "image2": "🦄🦄🦄🦄🦄", "diff": 3},
}

def run_puzzle(level=1):
    st.title("Spot the Difference 🧩")
    st.write(f"Difficulty Level: {level}")

    puzzle = DIFFERENCES.get(level, DIFFERENCES[15])

    st.subheader("🔍 Image A:")
    st.write(puzzle["image1"])

    st.subheader("🖼️ Image B:")
    st.write(puzzle["image2"])

    guess = st.number_input("What is the position of the difference (1-based)?", min_value=1, max_value=5, step=1)

    if st.button("Check"):
        if guess == puzzle["diff"]:
            st.success("🎉 Correct! You spotted the difference.")
            return "correct"
        else:
            st.error("❌ Nope, try again.")
