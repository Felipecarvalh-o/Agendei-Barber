import streamlit as st
from supabase_client import login_email, get_or_create_profile

st.set_page_config(page_title="Login", layout="centered")

# ---------------------------------------------------------
# 1. Verifica escolha de cliente/barbeiro
# ---------------------------------------------------------
role_choice = st.session_state.get("role_choice")

if not role_choice:
    st.error("Escolha primeiro se você é Cliente ou Barbeiro na tela inicial.")
    st.stop()

st.title("Entrar")

email = st.text_input("Email")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    user = login_email(email, password)

    if user is None:
        st.error("Email ou senha incorretos.")
        st.stop()

    # Cria perfil se ainda não existir
    profile = get_or_create_profile(user.id, email, role_choice)
    st.session_state["user"] = user
    st.session_state["profile"] = profile

    # Redirecionamento inteligente
    if profile["role"] == "barber":
        st.switch_page("home_barber")
    else:
        st.switch_page("home_client")
