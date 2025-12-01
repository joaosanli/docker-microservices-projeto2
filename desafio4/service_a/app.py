from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Rennan", "active_since": "2022-01-15"},
    {"id": 2, "name": "Ana", "active_since": "2023-06-01"},
]

@app.route("/users")
def get_users():
    return jsonify(USERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
