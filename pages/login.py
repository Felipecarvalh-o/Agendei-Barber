import streamlit as st
from supabase_client import login_email, get_or_create_profile

st.set_page_config(page_title="Login 💈")

st.title("Entrar")

# Se o usuário abriu o login direto sem selecionar papel
if "role_choice" not in st.session_state:
    st.warning("Escolha primeiro se você é Cliente ou Barbeiro.")
    st.switch_page("start.py")
    st.stop()

selected_role = st.session_state["role_choice"]

email = st.text_input("Email")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    user = login_email(email, password)

    if not user:
        st.error("Credenciais inválidas")
        st.stop()

    profile = get_or_create_profile(
        user.id,
        email,
        default_role=selected_role
    )

    st.session_state["user"] = user
    st.session_state["role"] = profile["role"]

    if selected_role == "barber":
        st.switch_page("dashboard_barber.py")
    else:
        st.switch_page("dashboard_client.py")
