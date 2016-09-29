from pymongo import MongoClient
from pyicloud import PyiCloudService
import time

# Store your password in keychain for security!

# Connect to icloud and mongo
api = PyiCloudService('joshnroy@gmail.com')

client = MongoClient()
db = client['openJosh']

coll = db['location-iphone']

while True:
    coll.insert_one(api.devices[2].location())
    time.sleep(300)
