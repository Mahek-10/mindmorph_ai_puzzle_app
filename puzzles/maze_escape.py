import streamlit as st

MAZES = {
    1: {
        "intro": "You are at the maze entrance. You can go [north] or [east].",
        "paths": {
            "north": {
                "text": "You hit a wall. Go back.",
                "end": False
            },
            "east": {
                "text": "You move east and see a door. Go [north] or [east].",
                "options": {
                    "north": {
                        "text": "You found the exit! 🎉",
                        "end": True
                    },
                    "east": {
                        "text": "Dead end.",
                        "end": False
                    }
                },
                "end": False
            }
        }
    }
}

def run_puzzle(level=1):
    st.title("Maze Escape 🧩")
    st.write(f"Difficulty Level: {level}")

    maze = MAZES.get(level, MAZES[1])
    st.write(maze["intro"])

    choice1 = st.selectbox("First move?", ["north", "east"], key="move1")
    result1 = maze["paths"][choice1]
    st.write(result1["text"])

    if not result1.get("end") and "options" in result1:
        choice2 = st.selectbox("Next move?", list(result1["options"].keys()), key="move2")
        result2 = result1["options"][choice2]
        st.write(result2["text"])
        if result2.get("end"):
            st.success("🎉 You escaped the maze!")
