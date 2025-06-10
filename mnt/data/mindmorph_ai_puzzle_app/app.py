
import streamlit as st
from login import login
from launcher import launcher

if login():
    launcher()
