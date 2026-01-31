import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cosmos", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container {padding: 0px; margin: 0px;}
        iframe {width: 100vw; height: 100vh; border: none;}
        header, footer, #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        # Altura alta para garantir que o conteúdo não seja cortado
        components.html(f.read(), height=1000, scrolling=False)
except:
    st.error("index.html não encontrado")