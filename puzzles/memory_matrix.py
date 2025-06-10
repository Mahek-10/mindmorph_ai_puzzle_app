import streamlit as st
import random
import time

def generate_grid(size=3):
    numbers = random.sample(range(10, 100), size*size)
    grid = [numbers[i:i+size] for i in range(0, size*size, size)]
    return grid

def run_puzzle(level=1):
    st.title("Memory Matrix 🧩")
    st.write(f"Difficulty Level: {level}")

    size = 3 + (level // 5)  # grid size increases with level
    grid = generate_grid(size)

    st.write("🧠 Memorize this grid:")
    for row in grid:
        st.write(" ".join(str(num) for num in row))

    st.info("Wait 5 seconds and the grid will disappear...")

    time.sleep(5)
    st.empty()  # clears previous output

    col = st.number_input("Which column was the number 42 in? (1-based)", min_value=1, max_value=size)

    # We'll fake a match for demonstration
    if st.button("Submit"):
        if col == 2:
            st.success("🎉 You remembered correctly!")
        else:
            st.error("❌ Incorrect. Keep practicing!")
