import streamlit as st
from supabase_client import listar_clientes, criar_cliente

# ============================
# VERIFICA LOGIN
# ============================
if "user" not in st.session_state:
    st.switch_page("pages/login.py")

st.title("Clientes 👥")

# ============================
# FORMULÁRIO DE NOVO CLIENTE
# ============================
st.subheader("Cadastrar cliente")

nome = st.text_input("Nome")
telefone = st.text_input("Telefone (opcional)")

if st.button("Adicionar cliente"):
    if nome.strip() == "":
        st.error("O nome é obrigatório.")
    else:
        criar_cliente(nome, telefone)
        st.success("Cliente cadastrado com sucesso!")
        st.rerun()

st.divider()

# ============================
# LISTAGEM DE CLIENTES
# ============================
st.subheader("Lista de clientes")

clientes = listar_clientes()

if not clientes:
    st.info("Nenhum cliente cadastrado ainda.")
else:
    for c in clientes:
        telefone = c.get("phone", "")
        telefone_txt = f"📞 {telefone}" if telefone else ""
        st.write(f"👤 **{c['name']}** {telefone_txt}")
