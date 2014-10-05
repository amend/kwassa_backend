from flask import Flask
from flask import jsonify
from flask import json
from bson import json_util
from pymongo import MongoClient
import pymongo

kwassa_backend = Flask(__name__)
kwassa_backend.debug = True
db = MongoClient().kwassa

@kwassa_backend.route("/")
def hello():
    return "Hello World!"

@kwassa_backend.route("/bestalbums/byyear/<int:year>/")
def bestalbums_byyear(year):
    albums_cursor = db.best_new_albums.find({"date": {"$regex": str(year) + "$"}}).sort("score", pymongo.DESCENDING)
    # http://stackoverflow.com/questions/11280382/python-mongodb-pymongo-json-encoding-and-decoding
    albums = [json.dumps(doc, default=json_util.default) for doc in albums_cursor]
    return jsonify(success=1,
                  albums=albums)

if __name__ == "__main__":
    kwassa_backend.run()
