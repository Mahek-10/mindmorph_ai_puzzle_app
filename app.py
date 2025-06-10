import streamlit as st
import os
from login import require_login

st.set_page_config(page_title="MindMorph Puzzle Hub", layout="centered")
require_login()

st.sidebar.markdown(f"👤 Logged in as: `{st.session_state['username']}`")

try:
    from main import launch_game
    launch_game()
except ModuleNotFoundError as e:
    st.error("❌ Could not find the puzzle launcher.")
    st.code(str(e))
    st.caption("Make sure the file `main.py` exists and contains a function named `launch_game()`.")
