import json
import pymongo 

data = {}
with open("data.json") as file:
    data = json.load(file)

city_country_mapping = {
    "new_york": "usa",
    "dallas": "usa",
    "beijing": "china",
    "colombo": "sri_lanka",
    "hong_kong": "china",
    "kandy": "sri_lanka",
    "wuhan": "china",
    "chicago": "usa"
}

# print(data['visa_rates'][city_country_mapping["beijing"]])

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["Passenger_Management_System"]
collection = db["tickets"]

# print(data)

for i in db['tickets'].find({}):
    total = data['visa_rates'][city_country_mapping[i['visa_stamped_location'][-1]]] + int(i['ticket_price'])
    print(f"id:{i['ticket_id']}, Name: {i['passenger_name']}, Total Price: {total}")