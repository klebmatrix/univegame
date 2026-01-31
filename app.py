import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cosmos", layout="wide", initial_sidebar_state="collapsed")

# CSS para esconder o cabeçalho do Streamlit e zerar margens
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding: 0px; margin: 0px;}
        iframe {width: 100vw; height: 100vh; border: none;}
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        jogo_html = f.read()
    components.html(jogo_html, height=1200, scrolling=False)
except FileNotFoundError:
    st.error("Arquivo index.html não encontrado.")