import streamlit as st
from supabase_api import get_or_create_profile

def save_user_session(user):
    st.session_state["user"] = {
        "id": user.id,
        "email": user.email
    }

def get_current_user():
    return st.session_state.get("user", None)

def require_login():
    if "user" not in st.session_state:
        st.error("Você precisa estar logado para acessar esta página.")
        st.stop()

def load_profile():
    user = get_current_user()
    if not user:
        return None
    
    profile = get_or_create_profile(
        user_id=user["id"],
        email=user["email"]
    )
    st.session_state["profile"] = profile
    return profile
