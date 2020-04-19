from .databeses.postgres import *
from .databeses.mongo import *
from .databeses.oracle import *


def all_postgres_dbs(): return pg_dbs()
def bk_all_pg(): return pg_backup_all()
def restore_all_pg(): return pg_restore_all()


def all_mongo_dbs(): return mongo_dbs()
def bk_all_mongo(): return mongo_backup_all()
def restore_all_mongo(): return mongo_restore_all()



def all_oracle_dbs(): return oracle_dbs()
def bk_all_oracle(): return oracle_backup_all()
def restore_all_oracle(): return oracle_restore_all()


def get_all_dbs(dbType):
    switch = {'postgres': all_postgres_dbs, 'mongo': all_mongo_dbs, 'oracle': all_oracle_dbs}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    output = func()
    return output


def backup_all_dbs(dbType):
    switch = {'postgres': bk_all_pg, 'mongo': bk_all_mongo, 'oracle': bk_all_oracle}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    output = func()
    return output


def restore_all_dbs(dbType):
    switch = {'postgres': restore_all_pg, 'mongo': restore_all_mongo, 'oracle': restore_all_oracle}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    output = func()
    return output


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
