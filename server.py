from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Caminho para salvar as configs recebidas
CONFIG_FILE = "config_recebida.json"

@app.route("/")
def home():
    return "Servidor ativo!"

@app.route("/config", methods=["POST"])
def receber_config():
    try:
        dados = request.json
        if not dados:
            return jsonify({"status": "erro", "mensagem": "Nenhum JSON recebido"}), 400

        # Mostra no Live Tail do Render
        print("📝 Config recebida:", dados)

        # Salva em arquivo
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        return jsonify({"status": "ok"}), 200

    except Exception as e:
        print("❌ Erro ao processar config:", e)
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

if __name__ == "__main__":
    # Usa porta padrão do Render ou 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
