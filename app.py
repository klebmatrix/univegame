import streamlit as st
import streamlit.components.v1 as components

# Configuração para esconder menus e ganhar espaço
st.set_page_config(page_title="Cosmos", layout="wide", initial_sidebar_state="collapsed")

# Estilo para remover margens brancas do Streamlit
st.markdown("""
    <style>
        .reportview-container .main .block-container { padding-top: 0rem; }
        iframe { border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.caption("Do Big Bang ao Presente: Arraste para coletar os átomos.")

try:
    with open("index.html", "r", encoding="utf-8") as f:
        jogo_html = f.read()
    # Altura maior para garantir que o fundo apareça no mobile
    components.html(jogo_html, height=800)
except FileNotFoundError:
    st.error("Arquivo index.html não encontrado.")