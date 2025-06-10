import streamlit as st
import importlib

PUZZLES = {
    "Sudoku": "puzzles.sudoku",
    "Word Morph": "puzzles.word_morph",
    "Logic Grid": "puzzles.logic_grid",
    "Pattern Sequence": "puzzles.pattern_sequence",
    "AI Crossword": "puzzles.ai_crossword",
    "Spot the Difference": "puzzles.spot_difference",
    "Maze Escape": "puzzles.maze_escape",
    "Memory Matrix": "puzzles.memory_matrix",
    "Tangram AI": "puzzles.tangram_ai",
    "Cipher Cracker": "puzzles.cipher_cracker",
    "Sliding Puzzle": "puzzles.sliding_puzzle",
    "Riddle Bot": "puzzles.riddle_bot",
    "Match Three": "puzzles.match_three",
    "Spatial 3D": "puzzles.spatial_3d",
    "AI Jigsaw": "puzzles.ai_jigsaw",
}

def launcher():
    st.sidebar.title("🧩 Puzzle Launcher")
    puzzle_choice = st.sidebar.selectbox("Choose a Puzzle", list(PUZZLES.keys()))
    level = st.sidebar.slider("Select Level", 1, 15, 1)

    module_name = PUZZLES[puzzle_choice]
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "run_puzzle"):
            module.run_puzzle(level=level)
        else:
            st.error(f"The selected puzzle '{puzzle_choice}' is missing a 'run_puzzle' function.")
    except ModuleNotFoundError as e:
        st.error(f"Error loading puzzle module: {e}")
