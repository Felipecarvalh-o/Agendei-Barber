import streamlit as st

if "user" not in st.session_state:
    st.switch_page("pages/Login.py")

user = st.session_state["user"]

import streamlit as st

if "user" not in st.session_state:
    st.switch_page("pages/Login.py")

from supabase_client import listar_agendamentos, listar_clientes
from datetime import date
import urllib.parse

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("<div class='title'>Lembretes WhatsApp 💬</div>", unsafe_allow_html=True)

hoje = str(date.today())
agendamentos = listar_agendamentos()
clientes = {c["id"]: c for c in listar_clientes()}

for a in agendamentos:
    if a["appointment_date"] == hoje:
        cliente = clientes.get(a["client_id"])
        if not cliente:
            continue

        msg = f"Olá {cliente['name']} 👋\nSeu horário hoje às {a['appointment_time']} está confirmado 💈"
        link = f"https://wa.me/55{cliente['phone']}?text={urllib.parse.quote(msg)}"

        st.markdown(f"""
        <div class='card'>
            <p><strong>{cliente['name']}</strong></p>
            <a href="{link}" target="_blank">📲 Enviar lembrete</a>
        </div>
        """, unsafe_allow_html=True)
