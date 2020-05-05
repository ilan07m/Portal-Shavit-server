from .databeses.postgres import *
from .databeses.mongo import *
from .databeses.oracle import *


def get_all_dbs(dbType):
    switch = {'postgres': pg_dbs(), 'mongo': mongo_dbs(), 'oracle': oracle_dbs()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


def backup_all_dbs(dbType):
    switch = {'postgres': pg_backup_all(), 'mongo': mongo_backup_all(), 'oracle': oracle_backup_all()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


def restore_all_dbs(dbType):
    switch = {'postgres': pg_restore_all(), 'mongo': mongo_restore_all(), 'oracle': oracle_restore_all()}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func


def crete_db(dbType, dbName):
    switch = {'postgres': create_pg_db(dbName), 'mongo': create_mongo_db(dbName), 'oracle': create_oracle_db(dbName)}
    func = switch.get(dbType, lambda: 'Not a valid dbType...')
    return func
