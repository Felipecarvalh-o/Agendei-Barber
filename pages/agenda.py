import streamlit as st
from supabase_client import (
    listar_servicos,
    listar_agendamentos,
    criar_agendamento,
    listar_clientes
)

# ============================
# VERIFICA LOGIN
# ============================
if "user" not in st.session_state:
    st.switch_page("pages/login.py")

user = st.session_state["user"]
st.title("Agenda 📅")


# ============================
# FORMULÁRIO DE AGENDAMENTO
# ============================
data = st.date_input("Data")
hora = st.time_input("Hora")

# ---- Lista serviços ----
servicos = listar_servicos(user.id)

if not servicos:
    st.warning("Cadastre um serviço primeiro.")
    st.stop()

servico = st.selectbox(
    "Serviço",
    servicos,
    format_func=lambda s: s["name"]
)

# ---- Lista clientes ----
clientes = listar_clientes()

if not clientes:
    st.warning("Cadastre um cliente primeiro.")
    st.stop()

cliente = st.selectbox(
    "Cliente",
    clientes,
    format_func=lambda c: c["name"]
)

# ============================
# BOTÃO CADASTRAR AGENDAMENTO
# ============================
if st.button("Agendar"):
    data_hora = f"{data} {hora}"

    criar_agendamento(
        barbeiro_id=user.id,
        client_id=cliente["id"],
        service_id=servico["id"],
        data_hora=data_hora
    )

    st.success("Agendamento criado com sucesso!")
    st.rerun()


# ============================
# LISTA DE AGENDAMENTOS
# ============================
st.divider()
st.subheader("Agendamentos do dia")

agendamentos = listar_agendamentos(user.id)

if not agendamentos:
    st.info("Nenhum agendamento encontrado.")
else:
    for a in agendamentos:
        cliente_nome = a.get("client", {}).get("name", "Cliente")
        servico_nome = a.get("service", {}).get("name", "Serviço")

        st.write(
            f"📌 **{a['appointment_time']}** — "
            f"{cliente_nome} — {servico_nome}"
        )
