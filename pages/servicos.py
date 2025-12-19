import streamlit as st
from supabase_client import listar_servicos, criar_servico

# ============================
# VERIFICA LOGIN
# ============================
if "user" not in st.session_state:
    st.switch_page("pages/login.py")

user = st.session_state["user"]
barbeiro_id = user.id

st.title("Serviços 💈")

# ============================
# FORMULÁRIO DE NOVO SERVIÇO
# ============================
st.subheader("Cadastrar serviço")

nome = st.text_input("Nome do serviço")
preco = st.number_input("Preço (R$)", min_value=0.0, step=1.0)
duracao = st.number_input("Tempo do serviço (minutos)", min_value=10, step=5)

if st.button("Adicionar serviço"):
    if nome.strip() == "":
        st.error("O nome é obrigatório.")
    else:
        criar_servico(barbeiro_id, nome, preco, duracao)
        st.success("Serviço cadastrado!")
        st.rerun()

st.divider()

# ============================
# LISTA DE SERVIÇOS
# ============================
st.subheader("Serviços cadastrados")

servicos = listar_servicos(barbeiro_id)

if not servicos:
    st.info("Nenhum serviço cadastrado ainda.")
else:
    for s in servicos:
        st.write(
            f"✂️ **{s['name']}** — "
            f"R$ {s['price']} — "
            f"⏱ {s['duration_minutes']} min"
        )
