import psycopg2
from ..ssh_commands import *
from resources.login_details import *
PG_GET_ALL_DBS_COMMAND = "SELECT datname FROM pg_database;"
PG_BACKUP_ALL_COMMAND = "pg_dumpall --clean -f "  # Need to insert the dmp file name
PG_RESTORE_ALL_COMMAND = "psql -f "  # Need to insert the dmp file name


def pg_dbs():
    dbList = []
    try:
        # TODO: Change host name
        db_conn = psycopg2.connect(host=TEMP_SERVER_NAME, port=PG_PORT, dbname=PG_MAIN_DB, user=PG_ROOT_USER,
                                   password=PG_ROOT_PASSWORD)
        db_cursor = db_conn.cursor()
        db_cursor.execute(PG_GET_ALL_DBS_COMMAND)
        for database in db_cursor.fetchall():
            dbList.append(database[0])
    except psycopg2.Error as e:
        print(e)
    return dbList


# TODO: Change the server name, the username and the password!!! + get dmp file as parameter!!!
def pg_backup_all():
    output = run_command(PG_BACKUP_ALL_COMMAND + "pg_bk_dump.dmp", connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'PG backup of all dbs is done!' + output


# TODO: Change the server name, the username and the password!!! + get dmp file as parameter!!!
def pg_restore_all():
    output = run_command(PG_RESTORE_ALL_COMMAND + "pg_bk_dump.dmp", connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'PG restore of all dbs is done!' + output

# TODO: Get DB name, user and password as parameter at every function that needs specific user
