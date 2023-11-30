
from flask import Flask, jsonify, render_template
import pymongo
from pymongo import MongoClient
import time

app = Flask(__name__)

client = MongoClient('mongodb', 27017)
db = client.dev
animals = db.animals


@app.route('/')
def ping_server():
    return "Welcome to the backend."


@app.route('/get_str', methods=["GET"])
def get_str():

    return "Hello from backend"


# @app.route("/hello", methods=("GET", "POST"))
# def hello():
#     """
#     This function just responds to the browser ULR
#     """
#     #
#     # if request.method == "POST":
#     #     content = time.time()

#     # return render_template("index.html")

#     animal = {"Type": "Lizard", "Name": "Plato", "Time": str(time.time())}

#     animal_id = animals.insert_one(animal).inserted_id
#     return jsonify({"Message": str(db.list_collection_names())})


@app.route("/animals")
def get_animals():
    out_str = "count: " + str(animals.count_documents({})) + "<br>"
    for animal in animals.find():
        out_str += str(animal)
        out_str += "<br>"

    return out_str


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
