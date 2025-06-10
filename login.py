import streamlit as st

# Dummy user credentials (this can be replaced with a more secure method or database)
USER_CREDENTIALS = {
    "admin": "password123",
    "user1": "pass1"
}

def login():
    st.title("🧠 MindMorph AI - Login")
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if USER_CREDENTIALS.get(username) == password:
                st.session_state.authenticated = True
                st.success("Login successful!")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password.")
        return False
    return True
