import pymongo
from ..ssh_commands import *
from resources.login_details import *
MONGO_BACKUP_ALL_COMMAND = "mongodump -u " + MONGO_ROOT_USER + " -p " + MONGO_ROOT_PASSWORD\
                           + " --authenticationDatabase admin --out "  # Need to insert the backup file name
MONGO_RESTORE_ALL_COMMAND = "mongorestore -u " + MONGO_ROOT_USER + " -p " + MONGO_ROOT_PASSWORD\
                            + " --authenticationDatabase admin --drop "  # Need to insert the dmp file name
# TODO: Change dir where backup files are!
MONGO_DMP_DIR = "~/mongobackups/{}"  # format with whole/db/collection


def mongo_dbs():
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    dbsList = client.list_database_names()
    return dbsList


# TODO: Change the server name, the username and the password!!! + get backup file as parameter!!!
def mongo_backup_all():
    output = run_command(MONGO_BACKUP_ALL_COMMAND + "/path/to/backup/file_name",
                         connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'MONGO backup of all dbs is done!!'


# TODO: Change the server name, the username and the password!!! + get backup file as parameter!!!
def mongo_restore_all():
    output = run_command(MONGO_RESTORE_ALL_COMMAND + "/path/to/backup/file_name",
                         connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'MONGO restore of all dbs is done!!'


def mongo_backup_files_of_all():
    path = MONGO_DMP_DIR.format("whole")
    print(path)
    dmpList = []
    command = "cd {}; ls -A1".format(path)
    output = run_command(command, connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    splitedfiles = output.splitlines()
    for project in splitedfiles:
        dmpList.append(project.decode('UTF-8'))
    return dmpList


def mongo_backup_files_of_db():
    path = MONGO_DMP_DIR.format("db")
    print(path)
    dmpList = []
    command = "cd {}; ls -A1".format(path)
    output = run_command(command, connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    splitedfiles = output.splitlines()
    for project in splitedfiles:
        dmpList.append(project.decode('UTF-8'))
    return dmpList


def mongo_backup_files_of_collection():
    path = MONGO_DMP_DIR.format("collection")
    print(path)
    dmpList = []
    command = "cd {}; ls -A1".format(path)
    output = run_command(command, connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    splitedfiles = output.splitlines()
    for project in splitedfiles:
        dmpList.append(project.decode('UTF-8'))
    return dmpList


# TODO: Get DB name, user and password as parameter at every function that needs specific user


def create_mongo_db(dbName):
    pass
