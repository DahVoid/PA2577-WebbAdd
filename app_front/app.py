
from flask import Flask, jsonify, render_template, request, url_for, redirect
import pymongo
from pymongo import MongoClient
import json
import requests

app = Flask(__name__)

client = MongoClient('mongodb', 27017)
db = client.dev
history = db.history


@app.route("/")
def ping_server():
    return "Hello to use the application please proceed to <a href=" + url_for("add") + " > add</a>"


@app.route("/empty_db")
def empty_db():
    history.drop()
    return "db dropped"


@app.route('/add', methods=["GET", "POST"])
def add():
    r = False
    if request.form:
        if request.method == "POST":
            a = request.form["a"]
            b = request.form["b"]
            response = requests.get(
                "http://flask-app-back:5000/add/" + a + "/" + b)
            r = response.text

    # Get history from db
    hist = []
    for row in history.find():
        str_row = row["A"] + " + " + row["B"] + " = " + row["R"]
        hist.append(str_row)
    return render_template("index.html", history=hist, result=r)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
