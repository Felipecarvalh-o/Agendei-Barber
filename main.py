import streamlit as st

st.set_page_config(
    page_title="Agendei Barber 💈",
    page_icon="💈",
    layout="wide"
)

st.title("Agendei Barber 💈")

if "user" not in st.session_state:
    st.warning("Faça login pelo menu lateral")
else:
    st.success(f"Bem-vindo!")
