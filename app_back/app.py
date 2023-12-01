
from flask import Flask, jsonify, render_template
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb', 27017)
db = client.dev
history = db.history


@app.route('/')
def ping_server():
    return "Welcome to the backend."


@app.route('/add/<a>/<b>', methods=["GET", "POST"])
def add(a, b):
    result = str(int(a) + int(b))
    row = {"A": a, "B": b, "R": result}
    row_id = history.insert_one(row).inserted_id
    return result


@app.route('/get_str', methods=["GET"])
def get_str():

    return "Hello from backend"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
