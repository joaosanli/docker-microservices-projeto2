from flask import Flask, jsonify

app = Flask(__name__)

ORDERS = [
    {"id": 101, "user_id": 1, "value": 150.0},
    {"id": 102, "user_id": 2, "value": 200.5},
    {"id": 103, "user_id": 3, "value": 99.9},
]

@app.route("/orders")
def orders():
    return jsonify(ORDERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
