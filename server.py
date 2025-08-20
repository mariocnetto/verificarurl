from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite que seu bot envie requests de qualquer origem

# === Armazena a configuração recebida ===
BOT_CONFIG = {}

@app.route("/")
def home():
    return "Servidor do Bot ativo!"

@app.route("/config", methods=["POST"])
def receber_config():
    global BOT_CONFIG
    data = request.json
    if not data:
        return jsonify({"status": "erro", "mensagem": "Nenhum JSON recebido"}), 400

    BOT_CONFIG = data
    print("💾 Configuração recebida:", BOT_CONFIG)  # Log no servidor
    return jsonify({"status": "ok", "mensagem": "Configuração salva com sucesso!"})

@app.route("/config", methods=["GET"])
def enviar_config():
    return jsonify(BOT_CONFIG)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render define PORT
    app.run(host="0.0.0.0", port=port)
