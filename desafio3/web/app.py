import os
import psycopg2
import redis
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.getenv("DATABASE_HOST", "db")
CACHE_HOST = os.getenv("CACHE_HOST", "cache")

def check_postgres():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname="desafio3",
            user="desafio3",
            password="desafio3",
            connect_timeout=2,
        )
        conn.close()
        return True
    except Exception:
        return False

def check_redis():
    try:
        r = redis.Redis(host=CACHE_HOST, port=6379, socket_connect_timeout=2)
        r.ping()
        return True
    except Exception:
        return False

@app.route("/")
def status():
    return jsonify(
        web="ok",
        postgres="ok" if check_postgres() else "erro",
        redis="ok" if check_redis() else "erro",
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
