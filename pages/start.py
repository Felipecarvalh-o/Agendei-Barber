import streamlit as st
from streamlit_extras.switch_page_button import switch_page

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
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0,0,0,0.55);
    z-index: -1;
}}
.card {{
    background: rgba(255,255,255,0.15);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    text-align: center;
}}
.btn {{
    width: 100%;
    padding: 14px;
    border-radius: 50px;
    border: none;
    font-weight: 700;
    cursor: pointer;
}}
.btn-yellow {{
    background: #F5C542;
}}
.btn-outline {{
    background: transparent;
    border: 2px solid white;
    color: white;
}}
</style>

<div class="overlay"></div>
"""

st.markdown(page_bg, unsafe_allow_html=True)

_, col, _ = st.columns([1,2,1])

with col:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## 💈 Encontre seu Barber")
    st.markdown("### Agende rapidamente e com praticidade")

    if st.button("Sou Barbeiro 🧔‍♂️", key="barber", use_container_width=True):
        st.session_state["role_choice"] = "barber"
        switch_page("login")

    if st.button("Sou Cliente 🙋‍♂️", key="client", use_container_width=True):
        st.session_state["role_choice"] = "client"
        switch_page("login")

    st.markdown("</div>", unsafe_allow_html=True)
