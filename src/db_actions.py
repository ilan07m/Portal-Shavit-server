from .databeses.postgres import *
from .databeses.mongo import *
from .databeses.oracle import *


def all_postgres_dbs(): return pg_dbs()


def all_mongo_dbs(): return mongo_dbs()


def all_oracle_dbs(): return 'ORACLE is about to be ready...'


def get_all_dbs(dbType):
    switch = {'postgres': all_postgres_dbs, 'mongo': all_mongo_dbs, 'oracle': all_oracle_dbs}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    output = func()
    return output


'''
def get_all_dbs(dbType):
    if dbType == 'postgres':
        print('postgres db is chosen!')
        output = pg_dbs()
    elif dbType == 'mongo':
        print('mongo db is chosen!')
        output = mongo_dbs()
    elif dbType == 'oracle':
        # TODO: Make oracle.py module
        print('oracle db is chosen!')
        output = "ORACLE is about to be ready..."
    else:
        output = "Not a valid dbType..."
    return output
'''

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
