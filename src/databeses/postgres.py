import psycopg2
from resources.login_details import *


def pg_dbs():
    dbList = []
    try:
        # TODO: Change host name
        db_conn = psycopg2.connect(host=TEMP_SERVER_NAME, port=PG_PORT, dbname=PG_MAIN_DB, user=PG_ROOT_USER,
                                   password=PG_ROOT_PASSWORD)
        db_cursor = db_conn.cursor()
        db_cursor.execute("""SELECT datname FROM pg_database;""")
        for database in db_cursor.fetchall():
            dbList.append(database[0])
    except psycopg2.Error as e:
        print(e)
    return dbList


def pg_backup_all():
    return 'PG backup of all dbs is done!'


def pg_restore_all():
    return 'PG restore of all dbs is done!'

# TODO: Get DB name, user and password as parameter at every function that needs specific user