import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cosmos", layout="wide")

st.markdown("""
    <style>
        .block-container {padding: 0px;}
        iframe {border: none;}
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        # Altura fixa de 600px para garantir que carregue no celular
        components.html(f.read(), height=600, scrolling=False)
except:
    st.error("Erro ao carregar index.html")