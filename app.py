import streamlit as st
import streamlit.components.v1 as components
import os

# Configuração da página para ocupar bem o espaço
st.set_page_config(page_title="Jornada Cósmica", layout="wide")

# Título e Introdução Pedagógica
st.title("🌌 Jornada Cósmica: Da Origem ao Humano")
st.write("Explore a linha do tempo do universo, colete átomos e aprenda sobre a nossa origem estelar.")

# Carregamento do Jogo (index.html)
try:
    with open("index.html", "r", encoding="utf-8") as f:
        jogo_html = f.read()
    
    # Injeta o jogo na página. Ajustei a altura para 700px para caber bem no navegador.
    components.html(jogo_html, height=700, scrolling=False)

except FileNotFoundError:
    st.error("Erro: O arquivo 'index.html' não foi encontrado. Certifique-se de que ele está na mesma pasta do app.py no GitHub.")

# Rodapé com o conceito das imagens
st.markdown("---")
st.info("**Cunho Pedagógico:** Este jogo representa a evolução desde o Universo Primordial até o Universo Moderno, destacando o 'Cosmic Noon' como o período crucial de formação dos elementos químicos que compõem a vida.")