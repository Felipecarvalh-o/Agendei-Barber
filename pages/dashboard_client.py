import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from utils import require_login, load_profile
from supabase_api import (
    listar_servicos,
    listar_agendamentos,
    criar_agendamento
)

import datetime

st.set_page_config(
    page_title="Área do Cliente 🙋‍♂️",
    layout="wide"
)

# ============================
# Proteção da página
# ============================
require_login()
profile = load_profile()

if profile["role"] != "client":
    st.error("Acesso permitido somente para clientes.")
    st.stop()

# ============================
# Estilo Premium
# ============================
st.markdown("""
<style>
.header-box {
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(135deg, #000000aa, #333333aa);
    backdrop-filter: blur(6px);
    color: white;
    margin-bottom: 25px;
}
.section-card {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 25px;
}
.section-card h3 {
    color: white;
}
button[kind="primary"] {
    background: #F5C542 !important;
    color: black !important;
    font-weight: bold;
    border-radius: 50px !important;
}
</style>
""", unsafe_allow_html=True)

# ============================
# Header
# ============================
st.markdown(f"""
<div class="header-box">
    <h2>🙋‍♂️ Olá, {profile['name'] or 'Cliente'}!</h2>
    <p>Bem-vindo ao seu painel de agendamentos.</p>
</div>
""", unsafe_allow_html=True)

# ============================
# Carrega serviços do barbeiro padrão
# ============================

# Para agora, você pode optar por 1 barbeiro fixo ou permitir escolher
# Mais tarde evoluímos isso! 
BARBEIRO_PADRAO = "default-barber"

servicos = listar_servicos(BARBEIRO_PADRAO)

# ============================
# Agendar novo horário
# ============================

with st.container():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("### 📅 Novo Agendamento")

    if len(servicos) == 0:
        st.warning("Nenhum serviço disponível para agendar.")
    else:
        nomes = {f"{s['name']} — R$ {s['price']}": s for s in servicos}
        escolha = st.selectbox("Escolha o serviço ✂️", list(nomes.keys()))

        data = st.date_input("Escolha o dia", datetime.date.today())
        hora = st.time_input("Escolha o horário", datetime.time(14, 0))

        if st.button("Agendar Agora"):
            data_hora = datetime.datetime.combine(data, hora).isoformat()

            criar_agendamento(
                BARBEIRO_PADRAO,
                profile["id"],
                nomes[escolha]["id"],
                data_hora
            )

            st.success("Agendamento realizado com sucesso!")
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

# ============================
# Histórico do cliente
# ============================

historico = listar_agendamentos(BARBEIRO_PADRAO)
historico_cliente = [h for h in historico if h["client_id"] == profile["id"]]

with st.container():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("### 📘 Meu Histórico")

    if len(historico_cliente) == 0:
        st.info("Nenhum agendamento encontrado.")
    else:
        for h in historico_cliente:
            serv = h.get("service", {}).get("name", "Serviço")
            data = h["appointment_time"].replace("T", "  ").split(".")[0]
            st.write(f"📌 **{data}** — {serv}")

    st.markdown("</div>", unsafe_allow_html=True)
