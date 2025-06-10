import streamlit as st

PUZZLES = {
    1: {"cipher": "Khoor", "hint": "Caesar +3", "answer": "hello"},
    2: {"cipher": "Wklv lv ixq", "hint": "Caesar +3", "answer": "this is fun"},
    3: {"cipher": "Fdhvdu flskhu lv hdvb", "hint": "Caesar +3", "answer": "caesar cipher is easy"},
    4: {"cipher": "Jvvrx ogf", "hint": "Caesar +2", "answer": "happy me"},
    5: {"cipher": "L oryh brx", "hint": "Caesar +3", "answer": "i love you"},
    6: {"cipher": "Wklv lv d whvw", "hint": "Caesar +3", "answer": "this is a test"},
    7: {"cipher": "Fdhvdu lv ixq", "hint": "Caesar +3", "answer": "caesar is fun"},
    8: {"cipher": "Dwwdfn dw gdzq", "hint": "Caesar +3", "answer": "attack at dawn"},
    9: {"cipher": "Frgh lv srvvleoh", "hint": "Caesar +3", "answer": "code is possible"},
    10: {"cipher": "Sbwkrq lv dzhvrph", "hint": "Caesar +3", "answer": "python is awesome"},
    11: {"cipher": "Fubswr judskv", "hint": "Caesar +3", "answer": "crypto graphs"},
    12: {"cipher": "Wkh hqg lv qhdu", "hint": "Caesar +3", "answer": "the end is near"},
    13: {"cipher": "Krw grjv", "hint": "Caesar +3", "answer": "hot dogs"},
    14: {"cipher": "Fkhfnhq qxjjhwv", "hint": "Caesar +3", "answer": "chicken nuggets"},
    15: {"cipher": "Jdph rq", "hint": "Caesar +3", "answer": "game on"},
}

def run_puzzle(level=1):
    st.title("Cipher Cracker 🧩")
    st.write(f"Difficulty Level: {level}")

    puzzle = PUZZLES.get(level, PUZZLES[15])
    cipher = puzzle["cipher"]
    answer = puzzle["answer"]
    hint = puzzle["hint"]

    st.write("🔐 Encrypted Message:", cipher)
    st.write("💡 Hint:", hint)

    user_input = st.text_input("Your Decryption")

    if user_input:
        if user_input.strip().lower() == answer:
            st.success("🎉 Correct!")
            return "correct"
        else:
            st.error("❌ Incorrect. Try again.")
