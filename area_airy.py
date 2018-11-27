# _3P_ds _1m7is _2BCH7 td td div
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient

client = MongoClient('mongodb://admin:adm00n@test-cluster-shard-00-00-zk4lm.mongodb.net:27017,test-cluster-shard-00-01-zk4lm.mongodb.net:27017,test-cluster-shard-00-02-zk4lm.mongodb.net:27017/test?ssl=true&replicaSet=test-cluster-shard-0&authSource=admin&retryWrites=true')

db = client['flight']
coll = db['country_list']

driver = webdriver.Chrome()
driver.get("https://www.traveloka.com/en-id/flight")

