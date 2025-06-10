import streamlit as st

PATTERNS = {
    1: ([2, 4, 6, 8], 10),
    2: ([1, 4, 9, 16], 25),
    3: ([3, 6, 12, 24], 48),
    4: ([21, 18, 15, 12], 9),
    5: ([2, 3, 5, 8], 13),
    6: ([100, 90, 81, 73], 66),
    7: ([1, 1, 2, 3, 5], 8),
    8: ([8, 16, 32, 64], 128),
    9: ([10, 20, 15, 30, 25], 50),
    10: ([5, 10, 20, 40], 80),
    11: ([7, 14, 28, 56], 112),
    12: ([81, 27, 9, 3], 1),
    13: ([2, 6, 12, 20], 30),
    14: ([0, 1, 1, 2, 3, 5], 8),
    15: ([4, 8, 16, 32, 64], 128)
}

def run_puzzle(level=1):
    st.title("Pattern Sequence 🧩")
    st.write(f"Difficulty Level: {level}")

    seq, answer = PATTERNS.get(level, PATTERNS[1])

    st.write("🔢 Identify the next number in the sequence:")
    st.write(" → ".join(map(str, seq)) + " → ?")

    user_input = st.number_input("Your Answer", step=1, format="%d")

    if st.button("Check Answer"):
        if int(user_input) == answer:
          if user_answer.strip().lower() == answer:
    st.success("🎉 Correct!")
    return "correct"  # 👈 Add this line

        else:
            st.error(f"❌ Incorrect. Try again.")
