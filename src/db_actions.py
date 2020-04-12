import psycopg2
import pymongo
from resources.login_details import *

# POSTGRES
'''
print("!!! I will try to connect to postgres  on your vm right now: !!!")
DB_NAME = "postgres"
QUERY = ""
try:
    # TODO: Change host name
    # TODO: Get DB name, user and password as parameter
    db_conn = psycopg2.connect(host=TEMP_SERVER_NAME, port=PG_PORT, dbname=DB_NAME, user=PG_ROOT_USER, password=PG_ROOT_PASSWORD)
    db_cursor = db_conn.cursor()
    print("Database opened successfully")
    db_cursor.execute("""SELECT datname FROM pg_database;""")
    # print cursor.fetchall()
    dbList = []
    for database in db_cursor.fetchall():
        dbList.append(database)
        print(database)
except psycopg2.Error as e:
    print(e)
'''


def pg_dbs():
    DB_NAME = "postgres"
    try:
        # TODO: Change host name
        # TODO: Get DB name, user and password as parameter
        db_conn = psycopg2.connect(host=TEMP_SERVER_NAME, port=PG_PORT, dbname=DB_NAME, user=PG_ROOT_USER,
                                   password=PG_ROOT_PASSWORD)
        db_cursor = db_conn.cursor()
        db_cursor.execute("""SELECT datname FROM pg_database;""")
        dbList = []
        for database in db_cursor.fetchall():
            print(database[0])
            dbList.append(database[0])
    except psycopg2.Error as e:
        print(e)
    return dbList


# MONGO
'''
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client.movies
dbsList = client.list_database_names()
collectionsList = db.list_collection_names()
print("DB's list is:")
print(dbsList)
print("Current DB is: " + db.name)
print("Collections list in current db is:")
print(collectionsList)
'''


def mongo_dbs():
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    dbsList = client.list_database_names()
    return dbsList
