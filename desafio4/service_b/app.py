import requests
from flask import Flask, jsonify

app = Flask(__name__)

SERVICE_A_URL = "http://service_a:5001/users"

@app.route("/report")
def report():
    try:
        resp = requests.get(SERVICE_A_URL, timeout=2)
        resp.raise_for_status()
        users = resp.json()
    except Exception as e:
        return jsonify(error="Erro ao falar com o service_a", details=str(e)), 500

    info = [
        f"Usuário {u['name']} ativo desde {u['active_since']}"
        for u in users
    ]

    return jsonify(
        message="Relatório de usuários montado pelo service_b",
        details=info,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
