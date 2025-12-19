import streamlit as st
import pandas as pd
from supabase_client import listar_agendamentos, listar_servicos

# ============================
# VERIFICA LOGIN
# ============================
if "user" not in st.session_state:
    st.switch_page("pages/Login.py")

user = st.session_state["user"]
barbeiro_id = user.id  # ID do barbeiro logado

# ============================
# CARREGAR CSS
# ============================
def load_css():
    try:
        with open("styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

load_css()

st.markdown("<div class='title'>Financeiro 💰</div>", unsafe_allow_html=True)

# ============================
# BUSCAR DADOS
# ============================
ag = listar_agendamentos(barbeiro_id)
servicos = {s["id"]: s for s in listar_servicos(barbeiro_id)}

dados = []

for a in ag:
    service_id = a.get("service_id")

    if not service_id:  # evita erro
        continue

    servico = servicos.get(service_id)
    if not servico:
        continue

    dados.append({
        "Data": a["appointment_time"].split("T")[0],  # extrai só a data
        "Valor": servico.get("price", 0)
    })

df = pd.DataFrame(dados)

# ============================
# EXIBIÇÃO
# ============================
if df.empty:
    st.info("Sem dados financeiros até o momento.")
else:
    total = df["Valor"].sum()
    st.markdown(
        f"""
        <div class='card'>
            <h2>Total: R$ {total:.2f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Faturamento diário")
    st.bar_chart(df.groupby("Data")["Valor"].sum())
