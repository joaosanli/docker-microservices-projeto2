from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Rennan"},
    {"id": 2, "name": "Ana"},
    {"id": 3, "name": "João"},
]

@app.route("/users")
def users():
    return jsonify(USERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
