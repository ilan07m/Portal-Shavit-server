# Portal-Shavit-server
Server side of portal shavit
* [Installation](#installation)
* [Built With](#Built With)
* [List Of Requests](#List Of Requests)

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

  - [GET /api/v1/shavit/resources/users](#get-/api/v1/shavit/resources/users)
  - [GET /api/v1/shavit/resources/servers](#get-/api/v1/shavit/resources/servers)
  - [GET /api/v1/shavit/resources/servers?serverGroupName=<SERVER_GROUP_NAME>](#post-/api/v1/shavit/resources/servers?serverGroupName=<SERVER_GROUP_NAME>)
  - [GET /api/v1/shavit/actions/servers/service?serverName=<SERVER_NAME>&serviceName=<SERVICE_NAME>&actionType=<ACTION_TYPE>](#get-magazines)
  


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

Request body:

    [
        {
            "name": "pg1"
        }, 
        {
            "name": "pg2"
        }
    ]
