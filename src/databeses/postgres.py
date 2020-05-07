from psycopg2 import connect, extensions, sql, Error
from ..ssh_commands import *
from resources.login_details import *
PG_GET_ALL_DBS_COMMAND = "SELECT datname FROM pg_database;"
PG_BACKUP_ALL_COMMAND = "pg_dumpall --clean -f "  # Need to insert the dmp file name
PG_RESTORE_ALL_COMMAND = "psql -f "  # Need to insert the dmp file name
# TODO: Change dir where backup files are!
PG_DMP_DIR = "~/pgbackups/{}/"  # format with whole/db/schema"
LIST_COMMAND = 'cd {}; ls -A1'
RESOURCE_ERROR = 'Not a valid resourceType...'


def pg_dbs():
    dbList = []
    try:
        # TODO: Change host name
        db_conn = connect(host=TEMP_SERVER_NAME, port=PG_PORT, dbname=PG_MAIN_DB, user=PG_ROOT_USER,
                                   password=PG_ROOT_PASSWORD)
        db_cursor = db_conn.cursor()
        db_cursor.execute(PG_GET_ALL_DBS_COMMAND)
        for database in db_cursor.fetchall():
            if not database[0].startswith('template'):
                dbList.append(database[0])
    except Error as e:
        print(e)
    return dbList


# TODO: Change the server name, the username and the password!!! + get dmp file as parameter!!!
def pg_backup_all():
    output = run_command(PG_BACKUP_ALL_COMMAND + "pg_bk_dump.dmp", connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'PG backup of all dbs is done!'


# TODO: Change the server name, the username and the password!!! + get dmp file as parameter!!!
# TODO: Make it work!
def pg_restore_all():
    output = run_command(PG_RESTORE_ALL_COMMAND + "pg_bk_dump.dmp", connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'PG restore of all dbs is done!'


def get_pg_backup_files_by_type(resourceType):
    dirName = {'all': 'whole', 'db': 'db', 'schema': 'schema'}
    resource = dirName.get(resourceType, RESOURCE_ERROR)
    if resource == RESOURCE_ERROR:
        return RESOURCE_ERROR
    path = PG_DMP_DIR.format(resource)
    dmpList = []
    output = run_command(LIST_COMMAND.format(path), connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    splitedfiles = output.splitlines()
    for project in splitedfiles:
        dmpList.append(project.decode('UTF-8'))
    return dmpList


# TODO: Get DB name, user and password as parameter at every function that needs specific user


def create_pg_db(dbName):
    try:
        db_conn = connect(host=TEMP_SERVER_NAME, port=PG_PORT, dbname=PG_MAIN_DB, user=PG_ROOT_USER,
                                   password=PG_ROOT_PASSWORD)
        autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        db_conn.set_isolation_level(autocommit)
        db_cursor = db_conn.cursor()
        # use the sql module instead to avoid SQL injection attacks
        db_cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbName)))
        db_cursor.close()
        db_conn.close()
        return "done!"
    except Error as e:
        return e
