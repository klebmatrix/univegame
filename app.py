import os
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Puxa a chave das variáveis de ambiente do Render
# Lembre-se de configurar "chave_mestra" no painel do Render
CHAVE_MESTRA = os.getenv("chave_mestra")

@app.route('/')
def index():
    # Aqui você cola o código HTML do jogo que criamos
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route('/verificar_acesso')
def verificar():
    # Exemplo de uso pedagógico da chave se necessário
    return jsonify({"status": "protegido", "valido": CHAVE_MESTRA is not None})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))