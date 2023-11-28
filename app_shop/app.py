
from flask import Flask, jsonify, render_template, request
import pymongo
from pymongo import MongoClient
import time

app = Flask(__name__)

client = MongoClient('test_mongodb', 27017)
db = client.dev
animals = db.animals


@app.route('/')
def ping_server():
    return "Welcome to the world of animals."


@app.route("/hello", methods=("GET", "POST"))
def hello():
    """
    This function just responds to the browser ULR
    """
    #
    # if request.method == "POST":
    #     content = time.time()

    # return render_template("index.html")

    animal = {"Type": "Lizard", "Name": "Plato"}

    animal_id = animals.insert_one(animal).inserted_id
    return jsonify({"Time": time.time(), "Message": str(db.list_collection_names())})


@app.route("/animals")
def get_animals():

    return str(animals.find_one({"Type": "Lizard"}))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
