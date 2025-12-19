import streamlit as st

if "user" not in st.session_state:
    st.switch_page("pages/Login.py")

user = st.session_state["user"]

import streamlit as st

if "user" not in st.session_state:
    st.switch_page("pages/Login.py")


def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

