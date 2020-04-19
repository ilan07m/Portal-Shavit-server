import pymongo
from resources.login_details import *


def mongo_dbs():
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    dbsList = client.list_database_names()
    return dbsList


def mongo_backup_all():
    return 'MONGO backup of all dbs is done!!'


def mongo_restore_all():
    return 'MONGO restore of all dbs is done!!'


# TODO: Get DB name, user and password as parameter at every function that needs specific user