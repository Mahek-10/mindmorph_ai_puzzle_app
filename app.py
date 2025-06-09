import streamlit as st
import os
import importlib
import base64

# Set page config
st.set_page_config(page_title="MindMorph AI Puzzle App", layout="wide")

# Load sound
def load_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true" controls><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        st.markdown(md, unsafe_allow_html=True)

load_audio("assets/sounds/welcome.mp3")

# Sidebar for puzzle selection
puzzle = st.sidebar.selectbox("Choose a Puzzle", [
    "sudoku", "word_morph", "logic_grid", "pattern_sequence", "ai_crossword",
    "spot_difference", "maze_escape", "memory_matrix", "tangram_ai", "cipher_cracker",
    "sliding_puzzle", "riddle_bot", "match_three", "spatial_3d", "ai_jigsaw"
])

# Scoreboard
if "score" not in st.session_state:
    st.session_state["score"] = 0

st.sidebar.markdown(f"### 🏆 Score: {st.session_state['score']}")

# Import and run puzzle
puzzle_module = importlib.import_module(f"puzzles.{puzzle}")
puzzle_module.run()