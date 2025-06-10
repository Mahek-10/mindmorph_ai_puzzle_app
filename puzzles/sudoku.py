import streamlit as st
import random

def generate_sudoku(level):
    # Very basic sudoku generator for demo purposes
    # A proper generator would ensure solvability
    base = 3
    side = base * base

    def pattern(r, c): return (base*(r % base)+r//base+c) % side
    def shuffle(s): return random.sample(s, len(s))
    rBase = range(base)
    rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, side+1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    # Hide cells based on level
    empties = level * 5  # More empty cells with higher difficulty
    for _ in range(empties):
        board[random.randint(0, 8)][random.randint(0, 8)] = 0
    return board

def display_sudoku(board):
    for row in board:
        st.write(" ".join(str(num) if num != 0 else "." for num in row))

def run_puzzle(level=1):
    st.title("Sudoku 🧩")
    st.write(f"Difficulty Level: {level}")

    board = generate_sudoku(level)
    display_sudoku(board)
    st.info("This is a simplified Sudoku generator. No validation or user input yet.")
