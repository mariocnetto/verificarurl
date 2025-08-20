from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota raiz apenas para testar
@app.route("/")
def index():
    return "Servidor rodando!", 200

# Rota para receber configuração do bot
@app.route("/config", methods=["POST"])
def receber_config():
    data = request.json  # pega o JSON enviado
    print("Config recebida:", data)  # debug no log
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render define PORT
    app.run(host="0.0.0.0", port=port)
