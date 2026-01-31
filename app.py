import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cosmos", layout="wide")

# Remove absolutamente tudo que sobra de espaço
st.markdown("""
    <style>
        .block-container {padding: 0px;}
        iframe {width: 100vw; height: 100vh; border: none;}
        header, footer, #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=2000) # Altura de sobra para não cortar
except:
    st.error("index.html não encontrado")