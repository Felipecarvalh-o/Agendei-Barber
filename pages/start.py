import streamlit as st

st.set_page_config(page_title="Agendei Barber 💈", layout="wide")

background_url = "https://images.unsplash.com/photo-1598387993561-5bfd4f9dd1ce"

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url('{background_url}');
    background-size: cover;
    background-position: center;
}}

.overlay {{
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.55);
    z-index: -1;
}}

.card {{
    background: rgba(255,255,255,0.15);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
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

_, col, _ = st.columns([1,2,1])

with col:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## 💈 Encontre seu Barber")
    st.markdown("Agendamentos rápidos e profissionais")

    if st.button("Sou Barbeiro 🧔‍♂️"):
        st.session_state["role_choice"] = "barber"
        st.switch_page("login.py")

    if st.button("Sou Cliente 🙋‍♂️"):
        st.session_state["role_choice"] = "client"
        st.switch_page("login.py")

    st.markdown("</div>", unsafe_allow_html=True)
