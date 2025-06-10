import streamlit as st
import json
import os

USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_user(username, password):
    users = load_users()
    users[username] = password
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def login_ui():
    st.title("🔐 MindMorph Login")
    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])
    users = load_users()

    with login_tab:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            if username in users and users[username] == password:
                st.session_state["username"] = username
                st.success(f"✅ Welcome, {username}!")
            else:
                st.error("❌ Invalid credentials")

    with signup_tab:
        new_user = st.text_input("New Username", key="new_user")
        new_pass = st.text_input("New Password", type="password", key="new_pass")
        if st.button("Sign Up"):
            if new_user in users:
                st.error("Username already exists.")
            elif new_user.strip() == "" or new_pass.strip() == "":
                st.error("Username and password cannot be empty.")
            else:
                save_user(new_user, new_pass)
                st.success("🎉 User registered! Please login.")

def require_login():
    if "username" not in st.session_state:
        login_ui()
        st.stop()
