import streamlit as st
import streamlit.components.v1 as components
import os

# Configuração da página
st.set_page_config(page_title="Jornada Cósmica", layout="centered")

# Puxa a chave das variáveis de ambiente (Configurada no Streamlit Secrets ou Render)
# Use letras minúsculas como você solicitou: chave_mestra
CHAVE_MESTRA = os.getenv("chave_mestra", "123456") # Valor padrão caso não encontre

st.title("🌌 Origem do Universo")

# Verificação de PIN (Mínimo 6, Máximo 8 caracteres conforme sua regra)
pin_input = st.text_input("Digite seu PIN de acesso para iniciar a evolução:", type="password")

if pin_input == CHAVE_MESTRA:
    st.success("Acesso concedido! Iniciando linha do tempo...")
    
    # Lendo o arquivo do jogo
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            jogo_html = f.read()
        
        # Renderiza o jogo dentro do Streamlit
        components.html(jogo_html, height=600, scrolling=False)
        
    except FileNotFoundError:
        st.error("Arquivo index.html não encontrado no repositório!")
else:
    if pin_input:
        st.error("PIN incorreto. A matéria escura bloqueou seu acesso.")

# Rodapé pedagógico
st.markdown("---")
st.caption("Atividade Pedagógica: Evolução Estelar e Origem da Vida.")