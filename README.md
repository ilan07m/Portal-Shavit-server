# Portal-Shavit-Server
Server side of portal shavit
* [Installation](#installation)
* [Built With](#built-With)
* [List Of Requests](#list-of-requests)

## Installation

Use the package manager pip to install: [flask](https://pypi.org/project/Flask/), [flask_swagger_ui](https://pypi.org/project/flask-swagger-ui/), [paramiko](https://pypi.org/project/paramiko/), [psycopg2](https://pypi.org/project/psycopg2/), [pymongo](https://pypi.org/project/pymongo/).

```bash
pip install flask paramiko flask_swagger_ui psycopg2 pymongo
```

From the main folder run:

```bash
python app.py
```

## Built With

* [pyhton](https://www.python.org/downloads/release/python-382/) - Python v3.8.2

## List Of Requests

### API Resources

  - [GET /api/v1/shavit/resources/users](#get-apiv1shavitresourcesusers)
  - [GET /api/v1/shavit/resources/servers](#get-apiv1shavitresourcesservers)
  - [GET /api/v1/shavit/resources/servers?serverGroupName=<SERVER_GROUP_NAME>](#get-apiv1shavitresourcesserversservergroupnameserver_group_name)
  - [GET /api/v1/shavit/resources/servers/services?serverGroupName=<SERVER_GROUP_NAME>](#get-apiv1shavitresourcesserversservicesservergroupnameserver_group_name)
  - [GET /api/v1/shavit/actions/servers/service?serverName=<SERVER_NAME>&serviceName=<SERVICE_NAME>&actionType=<ACTION_TYPE>](#get-apiv1shavitactionsserversserviceservernameserver_nameservicenameservice_nameactiontypeaction_type)
  - [GET /api/v1/shavit/dbs](#get-apiv1shavitdbs)
  - [GET /api/v1/shavit/dbs?dbType=<DB_NAME>](#get-apiv1shavitdbsdbtypedb_name)
  - [GET /api/v1/shavit/dbs/backup_files?dbType=<DB_NAME>&resourceType=<RESOURCE_TYPE>](#get-apiv1shavitdbsbackup_filesdbtypedb_nameresourcetyperesource_type)
  - [GET /api/v1/shavit/dbs/backup?dbType=<DB_NAME>](#get-apiv1shavitdbsbackupdbtypedb_name)
  - [GET /api/v1/shavit/dbs/restore?dbType=<DB_NAME>](#get-apiv1shavitdbsrestoredbtypedb_name)
  - [GET /api/v1/shavit/dbs/create?dbType=<DB_TYPE>&dbName=<DB_NAME>](#get-apiv1shavitdbscreatedbtypedb_typedbnamedb_name)
  - [GET /api/v1/shavit/ocp/login/infra](#get-apiv1shavitocplogininfra)
  - [GET /api/v1/shavit/ocp/projects](#get-apiv1shavitocpprojects)
  - [GET /api/v1/shavit/ocp/services?project=<PROJECT_NAME>](#get-apiv1shavitocpservicesprojectproject_name)
  
 
 
### GET /api/v1/shavit/resources/users

Example: http://localhost:5000/api/v1/shavit/resources/users

Response body:

    [
        "user1", 
        "user2", 
        "user3"
    ]

### GET /api/v1/shavit/resources/servers

Example: http://localhost:5000/api/v1/shavit/resources/servers

Response body:

    [
        {
            "OPENSHIFT": [
                {
                    "name": "openshift-server1"
                }, 
                {
                    "name": "openshift-server2"
                }, 
                {
                    "name": "openshift-server3"
                }]
        }, 
        {
            "POSTGRES": [
                {
                    "name": "pg1"
                }, 
                {
                    "name": "pg2"
                }]
        }, 
        {
            "MONGO": [
                {
                    "name": "mongo1"
                }, 
                {
                    "name": "mongo2"
                }]
        }
        ........
    ]

### GET /api/v1/shavit/resources/servers?serverGroupName=<SERVER_GROUP_NAME>

Example: http://localhost:5000/api/v1/shavit/resources/servers?serverGroupName=postgres

Response body:

    [
        "pg1", 
        "pg2"
    ]
    
### GET /api/v1/shavit/resources/servers/services?serverGroupName=<SERVER_GROUP_NAME>

Example: http://localhost:5000/api/v1/shavit/resources/servers/services?serverGroupName=openshift

Response body:

    [
        "atomic-openshift-node", 
        "docker",
        "firewalld",
        "iptables"
    ]

### GET /api/v1/shavit/actions/servers/service?serverName=<SERVER_NAME>&serviceName=<SERVICE_NAME>&actionType=<ACTION_TYPE>

Example: http://localhost:5000/api/v1/shavit/actions/servers/service?serverName=myserver.com&serviceName=docker&actionType=start

Response body:

```bash
active \ started \ stoped \ restarted
```

### GET /api/v1/shavit/dbs

Example: http://localhost:5000/api/v1/shavit/dbs

Response body:

    [
      "postgres", 
      "mongo", 
      "oracle"
    ]
    
### GET /api/v1/shavit/dbs?dbType=<DB_NAME>

Example: http://localhost:5000/api/v1/shavit/dbs?dbType=postgres

Response body:

    [
      "postgres", 
      "template1", 
      "template0"
    ]
    
### GET /api/v1/shavit/dbs/backup_files?dbType=<DB_NAME>&resourceType=<RESOURCE_TYPE>

Example: http://localhost:5000/api/v1/shavit/dbs/backup_files?dbType=postgres&resourceType=schema
Resource types: all, db, schema, collection

Response body:

    [
        "pgschema1.dmp", 
        "pgschema2.dmp", 
        "pgschema3.dmp"
    ]
    
### GET /api/v1/shavit/dbs/backup?dbType=<DB_NAME>

Example: http://localhost:5000/api/v1/shavit/dbs/backup?dbType=postgres

Response body:

    '<DB_NAME> backup of all dbs is done!' /OR/ 'ERROR'
    
### GET /api/v1/shavit/dbs/restore?dbType=<DB_NAME>

Example: http://localhost:5000/api/v1/shavit/dbs/restore?dbType=postgres

Response body:

    '<DB_NAME> restore of all dbs is done!' /OR/ 'ERROR'
    
### GET /api/v1/shavit/dbs/create?dbType=<DB_TYPE>&dbName=<DB_NAME>

Example: http://localhost:5000/api/v1/shavit/dbs/create?dbType=postgres&dbName=testdb

Response body:

    'done!'

### GET /api/v1/shavit/ocp/login/infra

Example: http://localhost:5000/api/v1/shavit/ocp/login/infra

Response body:

    'Login succeeded! Logged in as infra .......'
    
### GET /api/v1/shavit/ocp/projects

Example: http://localhost:5000/api/v1/shavit/ocp/projects

Response body:

    [
      "myproject", 
      "myproject2", 
      "myproject3"
    ]
    
### GET /api/v1/shavit/ocp/services?project=<PROJECT_NAME>

Example: http://localhost:5000/api/v1/shavit/ocp/services?project=myproject

Response body:

    [
        "mysql", 
        "ruby-hello-world"
    ]