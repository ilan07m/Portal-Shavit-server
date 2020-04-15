import pymongo
from resources.login_details import *


def mongo_dbs():
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    dbsList = client.list_database_names()
    return dbsList
