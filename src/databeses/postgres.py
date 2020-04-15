import psycopg2
from resources.login_details import *


def pg_dbs():
    dbName = "postgres"
    try:
        # TODO: Change host name
        # TODO: Get DB name, user and password as parameter
        db_conn = psycopg2.connect(host=TEMP_SERVER_NAME, port=PG_PORT, dbname=dbName, user=PG_ROOT_USER,
                                   password=PG_ROOT_PASSWORD)
        db_cursor = db_conn.cursor()
        db_cursor.execute("""SELECT datname FROM pg_database;""")
        dbList = []
        for database in db_cursor.fetchall():
            dbList.append(database[0])
    except psycopg2.Error as e:
        print(e)
    return dbList
