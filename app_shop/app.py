from flask import Flask, jsonify
from pymongo import MongoClient
import time
app = Flask(__name__)


@app.route("/")
def hello():
    """
    This function just responds to the browser ULR
    """
    return jsonify({"Time": time.time(), "Message": "Hello12!"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
