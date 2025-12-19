import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# ==============================
#  CONFIGURAÇÃO INICIAL
# ==============================
st.set_page_config(
    page_title="Agendei Barber 💈",
    layout="wide"
)

# ==============================
#  CSS E ESTILOS
# ==============================
background_url = "https://images.unsplash.com/photo-1598387993561-5bfd4f9dd1ce"

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url('{background_url}') !important;
    background-size: cover !important;
    background-position: center !important;
}}

.overlay {{
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.55);
    z-index: -1;
}}

.card {{
    background: rgba(255,255,255,0.18);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    text-align: center;
}}

button[kind="secondary"] {{
    background: rgba(255,255,255,0.2) !important;
    border: 1px solid rgba(255,255,255,0.6) !important;
    color: white !important;
    font-weight: bold;
    border-radius: 50px !important;
}}

button[kind="primary"] {{
    background: #F5C542 !important;
    color: black !important;
    font-weight: bold;
    border-radius: 50px !important;
}}
</style>

<div class="overlay"></div>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ==============================
#  INTERFACE
# ==============================
_, col, _ = st.columns([1, 2, 1])

with col:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## 💈 Encontre seu Barber")
    st.markdown("### Agendamentos rápidos e profissionais")

    # Evita KeyError caso login tente ler role_choice
    if "role_choice" not in st.session_state:
        st.session_state["role_choice"] = None

    # Botão Barbeiro
    if st.button("Sou Barbeiro 🧔‍♂️", key="barber_btn"):
        st.session_state["role_choice"] = "barber"
        switch_page("login")

    # Botão Cliente
    if st.button("Sou Cliente 🙋‍♂️", key="client_btn"):
        st.session_state["role_choice"] = "client"
        switch_page("login")

    st.markdown("</div>", unsafe_allow_html=True)
