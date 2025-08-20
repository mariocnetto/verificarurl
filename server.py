from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para receber a configuração
@app.route("/registrar", methods=["POST"])
def registrar():
    config = request.json
    print("Configuração recebida:", config)
    # Aqui você pode salvar em arquivo ou banco de dados
    with open("config_recebida.json", "w") as f:
        import json
        json.dump(config, f, indent=4)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
