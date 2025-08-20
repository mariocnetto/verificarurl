from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para receber a configuração
@app.route("/config", methods=["POST"])
def receber_config():
    dados = request.json  # pega o JSON enviado
    if dados is None:
        print("⚠️ Nenhum dado recebido!")
        return jsonify({"status": "fail", "message": "Nenhum dado enviado"}), 400

    # Mostra os dados completos no log
    print("📝 Config recebida:", dados)

    # Aqui você pode salvar em arquivo se quiser
    # with open("ultima_config.json", "w") as f:
    #     import json
    #     json.dump(dados, f, indent=4)

    return jsonify({"status": "ok"}), 200

# Endpoint de teste
@app.route("/", methods=["GET"])
def home():
    return "Servidor ativo!", 200

if __name__ == "__main__":
    # Porta padrão para Render
    app.run(host="0.0.0.0", port=10000)
