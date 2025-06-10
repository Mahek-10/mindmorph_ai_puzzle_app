
import streamlit as st

PUZZLES = {
    1: {"cipher": "Khoor", "hint": "Caesar +3", "answer": "hello"},
    2: {"cipher": "Wklv lv ixq", "hint": "Caesar +3", "answer": "this is fun"},
    3: {"cipher": "Fdhvdu flskhu lv hdvb", "hint": "Caesar +3", "answer": "caesar cipher is easy"},
    4: {"cipher": "Jvvrx ogf", "hint": "Caesar +2", "answer": "happy me"},
    5: {"cipher": "L oryh brx", "hint": "Caesar +3", "answer": "i love you"}
}

def run_puzzle(level=1):
    st.title("Cipher Cracker 🧩")
    st.write(f"Difficulty Level: {level}")

    puzzle = PUZZLES.get(level if level <= 5 else 5)
    st.write("🔐 Encrypted Message:", puzzle["cipher"])
    st.write("💡 Hint:", puzzle["hint"])

    guess = st.text_input("Your Decryption")

    if guess:
        if guess.strip().lower() == puzzle["answer"]:
            st.success("🎉 Correct decryption!")
        else:
            st.error("❌ Incorrect. Try again.")
