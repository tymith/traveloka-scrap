from flask import Flask
from flask_restful import Resource, Api
# from flask_pymongo import PyMongo
from pymongo import MongoClient

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            pass
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://admin:adm00n@test-cluster-shard-00-00-zk4lm.mongodb.net:27017,test-cluster-shard-00-01-zk4lm.mongodb.net:27017,test-cluster-shard-00-02-zk4lm.mongodb.net:27017/test?ssl=true&replicaSet=test-cluster-shard-0&authSource=admin&retryWrites=true')

db = client['flight']
coll = db['traveloka']

class getResult(Resource):
    def get(self):
        res = []
        for x in coll.find():
            res.append(x)
        
        return json.loads(JSONEncoder().encode(res))

api.add_resource(getResult, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
    