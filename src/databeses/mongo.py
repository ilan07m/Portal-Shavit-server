import pymongo
from ..ssh_commands import *
from resources.login_details import *
MONGO_BACKUP_ALL_COMMAND = "mongodump -u {} -p {} --authenticationDatabase admin --out {}"  # Insert username, password, and the backup file path
MONGO_RESTORE_ALL_COMMAND = "mongorestore -u {} -p {} --authenticationDatabase admin --drop {}"  # Insert username, password, and the dmp file path
# TODO: Change dir where backup files are!
MONGO_DMP_DIR = "~/mongobackups/{}"  # format with whole/db/collection
LIST_COMMAND = 'cd {}; ls -A1'
RESOURCE_ERROR = 'Not a valid resourceType...'


def mongo_dbs():
    try:
        client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        dbsList = client.list_database_names()
        return dbsList
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to server: %s" % e)



# TODO: Change the server name, the username and the password!!! + get backup file as parameter!!!
def mongo_backup_all():
    output = run_command(MONGO_BACKUP_ALL_COMMAND.format(MONGO_ROOT_USER, MONGO_ROOT_PASSWORD, "/path/backup/file"),
                         connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'MONGO backup of all dbs is done!!'

# TODO: Change to valid command with format!
# TODO: Change the server name, the username and the password!!! + get backup file as parameter!!!
def mongo_restore_all():
    output = run_command(MONGO_RESTORE_ALL_COMMAND.format(MONGO_ROOT_USER, MONGO_ROOT_PASSWORD, "/path/backup/file"),
                         connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    return 'MONGO restore of all dbs is done!!'


def get_mongo_backup_files_by_type(resourceType):
    dirName = {'all': 'whole', 'db': 'db', 'collection': 'collection'}
    resource = dirName.get(resourceType, RESOURCE_ERROR)
    if resource == RESOURCE_ERROR:
        return RESOURCE_ERROR
    path = MONGO_DMP_DIR.format(resource)
    dmpList = []
    output = run_command(LIST_COMMAND.format(path), connect_to_server(TEMP_SERVER_NAME, MY_USERNAME, MY_PASS))
    splitedfiles = output.splitlines()
    for project in splitedfiles:
        dmpList.append(project.decode('UTF-8'))
    return dmpList


# TODO: Get DB name, user and password as parameter at every function that needs specific user


def create_mongo_db(dbName):
    try:
        client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        newDB = client[dbName]
        sampleCollection = newDB["Delete_Me_Collection"]
        result = sampleCollection.insert_one({"note": "Delete me"})
        dbsList = client.list_database_names()
        return "%s db Created, Delete the sample collection and edit as you want" % dbName
    except pymongo.errors.ConnectionFailure as e:
        error = "Could not connect to server: %s" % e
        return error


# TODO: Check if working!!!!!!!!
def create_mongo_user(dbName, username, password):
    try:
        client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        db = client[dbName]
        db.command("createUser", username, pwd=password, roles=["dbOwner"])
        return "%s db Created, Delete the sample collection and edit as you want" % username
    except pymongo.errors.ConnectionFailure as e:
        error = "Could not connect to server: %s" % e
        return error
    '''
    To create a user:
    db.command("createUser", "admin", pwd="password", roles=["root"])
    
    To create a read-only user:
    db.command("createUser", "user", pwd="password", roles=["read"])
    
    To change a password:
    db.command("updateUser", "user", pwd="newpassword")
    
    Or change roles:
    db.command("updateUser", "user", roles=["readWrite"])
    db.command("updateUser", "user", roles=["readWrite"])
    '''
