import pymongo
from ..ssh_commands import *
from resources.login_details import *
MONGO_BACKUP_ALL_COMMAND = "mongodump -u " + MONGO_ROOT_USER + " -p " + MONGO_ROOT_PASSWORD\
                           + " --authenticationDatabase admin --out "  # Need to insert the backup file name
MONGO_RESTORE_ALL_COMMAND = "mongorestore -u " + MONGO_ROOT_USER + " -p " + MONGO_ROOT_PASSWORD\
                            + " --authenticationDatabase admin --drop "  # Need to insert the dmp file name


def mongo_dbs():
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    dbsList = client.list_database_names()
    return dbsList


# TODO: Change the server name, the username and the password!!! + get backup file as parameter!!!
def mongo_backup_all():
    output = run_command(MONGO_BACKUP_ALL_COMMAND + "/path/to/backup/file_name",
                         connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'MONGO backup of all dbs is done!!' + output


# TODO: Change the server name, the username and the password!!! + get backup file as parameter!!!
def mongo_restore_all():
    output = run_command(MONGO_RESTORE_ALL_COMMAND + "/path/to/backup/file_name",
                         connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'MONGO restore of all dbs is done!!' + output


# TODO: Get DB name, user and password as parameter at every function that needs specific user
