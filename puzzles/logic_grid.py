import streamlit as st

PUZZLES = {
    1: {
        "clues": [
            "Alice likes apples.",
            "Bob doesn't like bananas.",
            "Cathy likes cherries."
        ],
        "question": "Who likes bananas?",
        "answer": "None"
    },
    2: {
        "clues": [
            "Tom sits left of Jerry.",
            "Spike is not next to Tom.",
            "Tyke sits right of Jerry."
        ],
        "question": "Who is between Tom and Tyke?",
        "answer": "Jerry"
    },
    3: {
        "clues": [
            "Red lives in the first house.",
            "Blue lives next to Green.",
            "Green is not in the third house."
        ],
        "question": "What color is in the second house?",
        "answer": "Green"
    },
    4: {
        "clues": [
            "Emma is taller than Ava.",
            "Ava is taller than Mia.",
            "Olivia is the tallest."
        ],
        "question": "Who is the shortest?",
        "answer": "Mia"
    },
    5: {
        "clues": [
            "The dog is not in the red house.",
            "The cat is in the blue house.",
            "The fish is not in the green house."
        ],
        "question": "Which pet is in the red house?",
        "answer": "Fish"
    },
    6: {
        "clues": [
            "John, Max, and Leo are in a race.",
            "Max finished before Leo.",
            "John finished last."
        ],
        "question": "Who came in second?",
        "answer": "Leo"
    },
    7: {
        "clues": [
            "There are three doors: red, green, and blue.",
            "The treasure is not behind the red or green door."
        ],
        "question": "Where is the treasure?",
        "answer": "Blue"
    },
    8: {
        "clues": [
            "The baker wears a white hat.",
            "The chef doesn't wear black.",
            "The butcher wears blue."
        ],
        "question": "What color hat does the chef wear?",
        "answer": "White"
    },
    9: {
        "clues": [
            "Sara drives a red car.",
            "Mike drives a blue car.",
            "Emma drives a green car."
        ],
        "question": "Who drives the blue car?",
        "answer": "Mike"
    },
    10: {
        "clues": [
            "Each student gets one subject: Math, History, or Art.",
            "Liam doesn’t take Math or Art.",
            "Emma takes Art."
        ],
        "question": "What subject does Liam take?",
        "answer": "History"
    },
    11: {
        "clues": [
            "The apple is not on the top shelf.",
            "The banana is below the apple.",
            "The cherry is at the bottom."
        ],
        "question": "What is on the middle shelf?",
        "answer": "Banana"
    },
    12: {
        "clues": [
            "Monday is not the first day of work.",
            "Tuesday is before Thursday.",
            "Wednesday comes after Tuesday."
        ],
        "question": "Which day comes after Tuesday?",
        "answer": "Wednesday"
    },
    13: {
        "clues": [
            "Table A has 2 chairs.",
            "Table B has 3 chairs.",
            "Table C has one less than Table B."
        ],
        "question": "How many chairs does Table C have?",
        "answer": "2"
    },
    14: {
        "clues": [
            "Jack is older than Jill.",
            "Jill is older than Joe.",
            "Jack is younger than Mary."
        ],
        "question": "Who is the second oldest?",
        "answer": "Jack"
    },
    15: {
        "clues": [
            "There are 3 books: red, blue, and green.",
            "The red book is not first.",
            "The green book is last."
        ],
        "question": "Which book is in the middle?",
        "answer": "Red"
    }
}

def run_puzzle(level=1):
    st.title("Logic Grid 🧩")
    st.write(f"Difficulty Level: {level}")

    puzzle = PUZZLES.get(level, PUZZLES[1])

    st.subheader("Clues")
    for clue in puzzle["clues"]:
        st.write(f"- {clue}")

    user_answer = st.text_input("🧠 " + puzzle["question"])

    if user_answer:
        if user_answer.strip().lower() == puzzle["answer"].lower():
            st.success("🎉 Correct!")
            return "correct"
        else:
            st.error("❌ Try again.")
