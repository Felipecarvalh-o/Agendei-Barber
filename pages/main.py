import streamlit as st

st.set_page_config(
    page_title="Agendei Barber 💈",
    page_icon="💈",
    layout="wide"
)

# Redireciona automaticamente para o Login ou Home
if "user" not in st.session_state:
    st.switch_page("pages/login.py")
else:
    st.switch_page("pages/home.py")
