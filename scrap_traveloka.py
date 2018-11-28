import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://admin:adm00n@test-cluster-shard-00-00-zk4lm.mongodb.net:27017,test-cluster-shard-00-01-zk4lm.mongodb.net:27017,test-cluster-shard-00-02-zk4lm.mongodb.net:27017/test?ssl=true&replicaSet=test-cluster-shard-0&authSource=admin&retryWrites=true')

departure_airport = 'CGK' # CGK
arrival_airport = 'DPS' # DPS
departure_date = datetime.datetime.now().strftime('%d-%m-%Y') # dd-mm-yyyy
arrival_date = 'NA'
passenger = '1.0.0' # adult child infant 1.1.1
seat_class = 'ECONOMY' # ECONOMY BUSINESS FIRST PREMIUM_ECONOMY

db = client['flight']
coll = db['traveloka.{}'.format(datetime.datetime.now())]

driver = webdriver.Chrome()
driver.get("https://www.traveloka.com/en-id/flight/fullsearch?ap={}.{}&dt={}.{}&ps={}&sc={}".format(departure_airport, arrival_airport, departure_date, arrival_date, passenger, seat_class))

soup_base = BeautifulSoup(driver.page_source, 'html.parser')

# model
prices = []
time_departure = []
time_arrival = []
time_duration = []
plane_vendors = []

# price
for item in soup_base.find_all('div', class_='_27kIL'):
    price = str(item.get_text())
    price_int = int(''.join(price[3:-4].split('.')))
    prices.append(price_int)

# time
for index, item in enumerate(soup_base.find_all('div', class_='_32ZNg')):
    if ((index + 1) % 3 == 0):
        time_duration.append(str(item.get_text()))
    elif ((index + 2) % 3 == 0):
        time_arrival.append(str(item.get_text()))
    elif ((index + 3) % 3 == 0):
        time_departure.append(str(item.get_text()))

# plane vendor
for item in soup_base.find_all('div', class_='_2HE-b'):
    plane_vendors.append(str(item.get_text()))

zip_list = zip(plane_vendors, prices, time_departure, time_arrival, time_duration)

for item in zip_list:
    obj = {
        "plane_vendor": item[0],
        "price": item[1],
        "departure_time": item[2],
        "arrival_time": item[3],
        "duration": item[4],
        "source": {
            "source_id": 1,
            "source_name": "Traveloka"
        }
    }
    coll.insert_one(obj)
