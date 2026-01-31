import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.markdown("""
    <style>
        .block-container {padding: 0px;}
        iframe {border: none; width: 100vw; height: 100vh;}
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=800)
except:
    st.error("Erro: Arquivo index.html não encontrado.")