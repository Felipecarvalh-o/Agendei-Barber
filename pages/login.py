import streamlit as st
from supabase_client import login_email, get_or_create_profile

st.title("Agendei Barber 💈")

email = st.text_input("Email")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    try:
        user = login_email(email, password)

        if user:
            profile = get_or_create_profile(user.id, user.email)

            # Nunca quebra – agora sempre existe profile válido
            st.session_state["user"] = user
            st.session_state["role"] = profile.get("role", "barber")

            st.success("Login realizado com sucesso!")
            st.switch_page("pages/home.py")

        else:
            st.error("Credenciais inválidas")

    except Exception as e:
        st.error("Erro ao fazer login")
        st.write(e)
