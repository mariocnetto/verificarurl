from flask import Flask, request
import json
import os

app = Flask(__name__)

# Cria pasta para salvar configs se não existir
if not os.path.exists("configs"):
    os.makedirs("configs")

@app.route('/')
def home():
    return "Servidor rodando"

@app.route('/config', methods=['POST'])
def receber_config():
    data = request.json  # pega o JSON enviado pelo bot
    print("=== Config Recebida ===")
    print(json.dumps(data, indent=4))  # imprime bonito nos logs do Render

    # Salva em arquivo dentro da pasta configs
    arquivo = os.path.join("configs", "config_recebida.json")
    with open(arquivo, 'w') as f:
        json.dump(data, f, indent=4)

    return {"status": "ok"}

if __name__ == '__main__':
    # Render define a porta pelo ambiente
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
