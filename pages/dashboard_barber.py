import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from utils import require_login, load_profile
from supabase_api import (
    listar_servicos,
    listar_clientes,
    listar_agendamentos,
)

st.set_page_config(
    page_title="Painel do Barbeiro 💈",
    layout="wide"
)

# ============================
# Proteção da página
# ============================
require_login()
profile = load_profile()

if profile["role"] != "barber":
    st.error("Acesso negado — somente barbeiros podem acessar este painel.")
    st.stop()

# ============================
# Estilo premium
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
.metric {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
}
.metric h2 {
    color: #F5C542;
    margin: 5px;
}
</style>
""", unsafe_allow_html=True)

# ============================
# Header
# ============================
st.markdown(f"""
<div class="header-box">
    <h2>💈 Bem-vindo, {profile['name'] or 'Barbeiro'}!</h2>
    <p>Barbearia: <b>{profile['barbershop_name'] or 'Configure no perfil'}</b></p>
</div>
""", unsafe_allow_html=True)

# ============================
# Dados do barbeiro
# ============================
servicos = listar_servicos(profile["id"])
clientes = listar_clientes()
agenda = listar_agendamentos(profile["id"])

# ============================
# Métricas
# ============================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric'><h2>👥</h2><p>Clientes</p><h2>" +
                str(len(clientes)) + "</h2></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric'><h2>✂️</h2><p>Serviços</p><h2>" +
                str(len(servicos)) + "</h2></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric'><h2>📅</h2><p>Agendamentos</p><h2>" +
                str(len(agenda)) + "</h2></div>", unsafe_allow_html=True)

# ============================
# Seções
# ============================

# Serviços
with st.container():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("### ✂️ Serviços cadastrados")

    if len(servicos) == 0:
        st.info("Nenhum serviço cadastrado ainda.")
    else:
        for s in servicos:
            st.write(f"**{s['name']}** — R$ {s['price']} — {s['duration_minutes']} min")

    if st.button("Gerenciar Serviços"):
        switch_page("servicos")

    st.markdown("</div>", unsafe_allow_html=True)

# Agenda
with st.container():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("### 📅 Agenda do dia")

    if len(agenda) == 0:
        st.info("Nenhum horário marcado.")
    else:
        for a in agenda:
            cliente = a["client"]["name"] if a.get("client") else "Cliente não encontrado"
            servico = a["service"]["name"] if a.get("service") else "Serviço"
            st.write(f"🕒 **{a['appointment_time']}** — {cliente} — {servico}")

    if st.button("Ver Agenda Completa"):
        switch_page("agendamentos")

    st.markdown("</div>", unsafe_allow_html=True)

# Clientes
with st.container():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("### 👤 Clientes")

    if len(clientes) == 0:
        st.info("Nenhum cliente ainda.")
    else:
        for c in clientes:
            st.write(f"• **{c['name']}** — {c['phone']}")

    if st.button("Gerenciar Clientes"):
        switch_page("clientes")

    st.markdown("</div>", unsafe_allow_html=True)

# Lembretes
with st.container():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("### 💬 Lembretes Automáticos")

    if st.button("Enviar / Gerenciar Lembretes"):
        switch_page("lembretes")

    st.markdown("</div>", unsafe_allow_html=True)
