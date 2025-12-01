from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    hostname = socket.gethostname()
    return jsonify(
        message="Olá! Este é o servidor do Desafio 1 respondendo na rede Docker.",
        timestamp=now,
        container=hostname,
    )

if __name__ == "__main__":
    # host=0.0.0.0 para ficar acessível de fora do container
    app.run(host="0.0.0.0", port=8080)
