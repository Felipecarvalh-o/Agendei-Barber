import streamlit as st

def require_login():
    if "user" not in st.session_state:
        st.switch_page("start")
        st.stop()

def require_role(allowed):
    require_login()
    role = st.session_state.get("role")
    if role not in allowed:
        st.error("Você não tem permissão para acessar esta página.")
        st.stop()

def load_profile():
    return {
        "id": st.session_state["user"].id,
        "email": st.session_state["user"].email,
        "name": st.session_state.get("profile_name", ""),
        "role": st.session_state.get("role", "client")
    }
