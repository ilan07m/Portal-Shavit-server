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


# Get dmp files
def get_backup_files_by_type(dbType, resourceType):
    if dbType == POSTGRES:
        return get_pg_backup_files_by_type(resourceType)
    elif dbType == MONGO:
        return get_mongo_backup_files_by_type(resourceType)
    elif dbType == ORACLE:
        return get_oracle_backup_files_by_type(resourceType)
    else:
        return "Error! not a valid dbType type..."


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


def get_master_of_db_cluster(dbType):
    if dbType == POSTGRES:
        return get_pg_master()
    elif dbType == MONGO:
        return get_mongo_master()
    elif dbType == ORACLE:
        return get_oracle_master()
    else:
        return "Error! not a valid db type..."
