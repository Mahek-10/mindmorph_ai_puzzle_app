import streamlit as st

PUZZLES = [
    ("cold", "warm"),
    ("lead", "gold"),
    ("head", "tail"),
    ("make", "take"),
    ("good", "evil"),
    ("love", "hate"),
    ("slow", "fast"),
    ("high", "low"),
    ("life", "dead"),
    ("rich", "poor"),
    ("more", "less"),
    ("true", "fake"),
    ("give", "take"),
    ("open", "shut"),
    ("play", "work")
]

def run_puzzle(level=1):
    st.title("Word Morph 🧩")
    st.write(f"Difficulty Level: {level}")

    if level > len(PUZZLES):
        st.warning("Level not found.")
        return

    start, end = PUZZLES[level - 1]
    st.write(f"Start word: `{start.upper()}` → End word: `{end.upper()}`")

    user_words = st.text_area("Enter word sequence (one per line)").splitlines()

    if st.button("Check Solution"):
        if not user_words:
            st.error("Enter at least one word.")
            return

        valid = user_words[0].strip().lower() == start and user_words[-1].strip().lower() == end
        all_four = all(len(word) == 4 for word in user_words)

        # Check one-letter difference between each word
        def one_letter_diff(w1, w2):
            return sum(a != b for a, b in zip(w1, w2)) == 1

        steps_valid = all(one_letter_diff(user_words[i], user_words[i+1])
                          for i in range(len(user_words)-1))

        if valid and all_four and steps_valid:
            st.success("🎉 Correct transformation!")
        else:
            st.error("❌ Invalid transformation. Check each step carefully.")
