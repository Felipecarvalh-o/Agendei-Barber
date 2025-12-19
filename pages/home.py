import streamlit as st

# ============================
# VERIFICA LOGIN
# ============================
if "user" not in st.session_state or "role" not in st.session_state:
    st.switch_page("pages/login.py")

user = st.session_state["user"]
role = st.session_state["role"]

# ============================
# PÁGINA PRINCIPAL
# ============================
st.title("Painel Principal 💈")

st.subheader("Perfil atual:")
st.write(f"🔹 **{role.upper()}**")

st.divider()

# ============================
# MENU DINÂMICO POR FUNÇÃO
# ============================
if role == "barber":
    st.page_link("pages/servicos.py", label="💈 Serviços")
    st.page_link("pages/agenda.py", label="📅 Agenda")
    st.page_link("pages/financeiro.py", label="💰 Financeiro")
    st.page_link("pages/clientes.py", label="👥 Clientes")

elif role == "client":
    st.page_link("pages/agenda.py", label="📅 Agendar horário")
    st.page_link("pages/clientes.py", label="👤 Meu Perfil")
