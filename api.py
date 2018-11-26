from flask import Flask
from flask_restful import Resource, Api
# from flask_pymongo import PyMongo
from pymongo import MongoClient
import json

app = Flask(__name__)
api = Api(app)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)

client = MongoClient('mongodb://admin:adm00n@test-cluster-shard-00-00-zk4lm.mongodb.net:27017,test-cluster-shard-00-01-zk4lm.mongodb.net:27017,test-cluster-shard-00-02-zk4lm.mongodb.net:27017/test?ssl=true&replicaSet=test-cluster-shard-0&authSource=admin&retryWrites=true')

db = client['flight']
coll = db['traveloka']

res = []


class HelloWorld(Resource):
    def get(self):
        for x in coll.find():
            res.append(x)
        return res

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
    