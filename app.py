import streamlit as st
import streamlit.components.v1 as components

# Configuração para remover menus e ganhar cada pixel da tela
st.set_page_config(page_title="Origem", layout="wide", initial_sidebar_state="collapsed")

# Estilo para forçar o componente a ocupar a tela toda e tirar margens
st.markdown("""
    <style>
        .block-container { padding: 0rem; }
        iframe { width: 100% !important; border: none; }
        .stCaption { text-align: center; padding: 5px; color: #888; }
    </style>
""", unsafe_allow_html=True)

st.caption("Do Big Bang ao Presente: Arraste para coletar os átomos.")

try:
    with open("index.html", "r", encoding="utf-8") as f:
        jogo_html = f.read()
    # Altura dinâmica para garantir que tudo apareça no mobile
    components.html(jogo_html, height=1000, scrolling=False)
except FileNotFoundError:
    st.error("Arquivo index.html não encontrado.")