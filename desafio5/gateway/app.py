import requests
from flask import Flask, jsonify

app = Flask(__name__)

USERS_URL = "http://users:5001/users"
ORDERS_URL = "http://orders:5003/orders"

@app.route("/users")
def proxy_users():
    try:
        resp = requests.get(USERS_URL, timeout=2)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as e:
        return jsonify(error="Erro ao consultar serviço de usuários", details=str(e)), 502

@app.route("/orders")
def proxy_orders():
    try:
        resp = requests.get(ORDERS_URL, timeout=2)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as e:
        return jsonify(error="Erro ao consultar serviço de pedidos", details=str(e)), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
