from .databeses.postgres import *
from .databeses.mongo import *
from .databeses.oracle import *
POSTGRES = 'postgres'
MONGO = 'mongo'
ORACLE = 'oracle'
ALL = 'all'
DB = 'db'
SCHEMA = 'schema'
COLLECTION = 'collection'


# Get all dbs of db type
def get_all_dbs(dbType):
    switch = {'postgres': pg_dbs(), 'mongo': mongo_dbs(), 'oracle': oracle_dbs()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


# Get dmp files section
def backup_files_of_all_dbs(dbType):
    if dbType == POSTGRES:
        return pg_backup_files_of_all()
    elif dbType == MONGO:
        return mongo_backup_files_of_all()
    elif dbType == ORACLE:
        return oracle_backup_files_of_all()
    else:
        return "Error! not a valid db type..."


def backup_files_of_specific_db(dbType):
    if dbType == POSTGRES:
        return pg_backup_files_of_db()()
    elif dbType == MONGO:
        return mongo_backup_files_of_db()
    elif dbType == ORACLE:
        return oracle_backup_files_of_db()
    else:
        return "Error! not a valid db type..."


def backup_files_of_specific_schema(dbType):
    if dbType == POSTGRES:
        return pg_backup_files_of_schema()()
    elif dbType == ORACLE:
        return oracle_backup_files_of_schema()
    else:
        return "Error! not a valid db type..."


def backup_files_of_specific_collection(dbType):
    if dbType == MONGO:
        return mongo_backup_files_of_collection()
    else:
        return "Error! not a valid db type..."


def backup_files_by_type(dbType, resourceType):
    if resourceType == ALL:
        return backup_files_of_all_dbs(dbType)
    elif resourceType == DB:
        return backup_files_of_specific_db(dbType)
    elif resourceType == SCHEMA:
        return backup_files_of_specific_schema(dbType)
    elif resourceType == COLLECTION:
        return backup_files_of_specific_collection(dbType)
    else:
        return "Error! not a valid resource type..."


# Backup section
def backup_all_dbs(dbType):
    switch = {'postgres': pg_backup_all(), 'mongo': mongo_backup_all(), 'oracle': oracle_backup_all()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


# Restore section
def restore_all_dbs(dbType):
    switch = {'postgres': pg_restore_all(), 'mongo': mongo_restore_all(), 'oracle': oracle_restore_all()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


def restore_specific_db(dbType, args):
        return ""


def restore_specific_schema(dbType, args):
    return ""


def restore_specific_collection(dbType, args):
    return ""


def restore_by_type(dbType, resourceType, args):
    return ""

def restore_by_type2(dbType, resourceType, args):
    if resourceType == DB:
        pass
    elif resourceType == SCHEMA:
        pass
    elif resourceType == COLLECTION:
        pass
    elif resourceType == ALL:
        pass
    return "Error!"


# Create section
def crete_db(dbType, dbName):
    if dbType == POSTGRES:
        return create_pg_db(dbName)
    elif dbType == MONGO:
        return create_mongo_db(dbName)
    elif dbType == ORACLE:
        return create_oracle_db(dbName)
    else:
        return "Error! not a valid db type..."
    ''' switch = {'postgres': create_pg_db(dbName), 'mongo': create_mongo_db(dbName), 'oracle': create_oracle_db(dbName)}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func'''
