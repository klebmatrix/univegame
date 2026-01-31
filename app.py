import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cosmos", layout="wide")

# Texto super reduzido para ganhar espaço
st.caption("Do Big Bang ao Presente: Colete os átomos da nossa origem.")

try:
    with open("index.html", "r", encoding="utf-8") as f:
        jogo_html = f.read()
    # Aumentei a altura para 800 para o jogo brilhar na tela
    components.html(jogo_html, height=800, scrolling=False)
except FileNotFoundError:
    st.error("Arquivo index.html não encontrado.")