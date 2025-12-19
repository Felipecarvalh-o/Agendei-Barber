import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from supabase_api import login_email, login_social
from utils import save_user_session, load_profile

st.set_page_config(page_title="Login | Agendei Barber", layout="centered")

st.title("🔐 Login")

role = st.session_state.get("role_choice", None)
if not role:
    st.warning("Escolha primeiro se você é Cliente ou Barbeiro.")
    switch_page("Home")
    st.stop()

email = st.text_input("Email")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    user = login_email(email, password)
    
    if user:
        save_user_session(user)
        
        # Carrega ou cria profile
        profile = load_profile()

        # Se for cliente -> dashboard cliente
        if profile["role"] == "client":
            switch_page("dashboard_client")

        # Se for barbeiro -> dashboard barbeiro
        else:
            switch_page("dashboard_barber")
    else:
        st.error("Email ou senha incorretos.")

st.divider()
st.write("Ou entre com:")
if st.button("Entrar com Google"):
    login_social("google")
