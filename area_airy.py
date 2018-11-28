
import requests
# from pymongo import MongoClient

# client = MongoClient('mongodb://admin:adm00n@test-cluster-shard-00-00-zk4lm.mongodb.net:27017,test-cluster-shard-00-01-zk4lm.mongodb.net:27017,test-cluster-shard-00-02-zk4lm.mongodb.net:27017/test?ssl=true&replicaSet=test-cluster-shard-0&authSource=admin&retryWrites=true')

# db = client['flight']
# coll = db['airy_city_list']

r = requests.get('https://sky-api.airyrooms.com/v1/static/airport')
airports = r.json()['data']['airports']

for airport in airports:
    airport['city']
    airport['areaCode']
    airport['airportCode']
    airport['internationalAirportName']

