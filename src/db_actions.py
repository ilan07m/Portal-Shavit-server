import psycopg2
from resources.login_details import *

print("!!! I will try to connect to postgres  on your vm right now: !!!")
DB_NAME = "postgres"
QUERY = ""
try:
    # TODO: Change host name
    db_conn = psycopg2.connect(host=TEMP_SERVER_NAME, port=PG_PORT, dbname=DB_NAME, user=PG_ROOT_USER, password=PG_ROOT_PASSWORD)
    db_cursor = db_conn.cursor()
    print("Database opened successfully")
    db_cursor.execute("""SELECT datname FROM pg_database;""")
    # print cursor.fetchall()
    for database in db_cursor.fetchall():
        print(database)
except psycopg2.Error as e:
    print(e)
