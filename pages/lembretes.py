import streamlit as st
from database import listar_agendamentos, criar_lembrete

st.title("Lembretes WhatsApp 💬")

# Segurança — só barbeiro acessa
if st.session_state.get("role") != "barber":
    st.error("Acesso negado. Área exclusiva para barbeiros.")
    st.stop()

user = st.session_state.get("user")

if not user:
    st.error("Erro: usuário não autenticado.")
    st.stop()

# Listar agendamentos
agendamentos = listar_agendamentos(user.id)

if not agendamentos:
    st.info("Nenhum agendamento encontrado.")
    st.stop()

for ag in agendamentos:
    cliente = ag.get("client", {})
    servico = ag.get("service", {})
    dt = ag.get("appointment_time")

    st.write(f"📌 **{cliente.get('name')}** — {servico.get('name')} — {dt}")

    if st.button(f"Enviar lembrete para {cliente.get('name')}", key=ag["id"]):
        criar_lembrete(ag["id"])
        st.success("Lembrete registrado!")
