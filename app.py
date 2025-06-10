import streamlit as st
from login import require_login
from main import launch_game  # This should contain your puzzle selection and game logic

# App entry point
def main():
    st.set_page_config(page_title="MindMorph Puzzle Hub", layout="centered")

    # Require login first
    require_login()

    # Show welcome and launch puzzles
    st.sidebar.markdown(f"👤 Logged in as: `{st.session_state['username']}`")
    launch_game()

if __name__ == "__main__":
    main()
