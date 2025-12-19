import streamlit as st
from supabase_client import login_email, get_or_create_profile

st.set_page_config(page_title="Login • Agendei Barber", layout="centered")

st.title("🔐 Login")

role_from_choice = st.session_state.get("role_choice", "client")

email = st.text_input("Email")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    try:
        user = login_email(email, password)

        if user:
            # cria ou busca perfil já usando a role escolhida
            profile = get_or_create_profile(
                user.id,
                user.email,
                default_role=role_from_choice
            )

            # salva sessão
            st.session_state["user"] = user
            st.session_state["role"] = profile.get("role", "client")

            st.success("Login realizado com sucesso!")

            # redireciona para página correta
            if st.session_state["role"] == "barber":
                st.switch_page("pages/home_barber.py")
            else:
                st.switch_page("pages/home_client.py")

        else:
            st.error("Credenciais inválidas")

    except Exception as e:
        st.error("Erro ao fazer login")
        st.write(e)
