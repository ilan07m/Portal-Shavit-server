from .databeses.postgres import *
from .databeses.mongo import *
from .databeses.oracle import *
'''POSTGRES = 'postgres'
MONGO = 'mongo'
ORACLE = 'oracle' '''
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
    switch = {'postgres': pg_backup_files_of_all(),
              'mongo': mongo_backup_files_of_all(),
              'oracle': oracle_backup_files_of_all()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


def backup_files_of_specific_db(dbType):
    switch = {'postgres': pg_backup_files_of_db(),
              'mongo': mongo_backup_files_of_db(),
              'oracle': oracle_backup_files_of_db()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


def backup_files_of_specific_schema(dbType):
    switch = {'postgres': pg_backup_files_of_schema(),
              'oracle': oracle_backup_files_of_schema()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


def backup_files_of_specific_collection(dbType):
    switch = {'mongo': mongo_backup_files_of_collection()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


def backup_files_by_type(dbType, resourceType):
    switch = {'all': backup_files_of_all_dbs(dbType),
              'db': backup_files_of_specific_db(dbType),
              'schema': backup_files_of_specific_schema(dbType),
              'collection': backup_files_of_specific_collection(dbType)}
    func = switch.get(resourceType, lambda: 'Not a valid dbType...')
    return func


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
    switch = {'postgres': create_pg_db(dbName), 'mongo': create_mongo_db(dbName), 'oracle': create_oracle_db(dbName)}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func
