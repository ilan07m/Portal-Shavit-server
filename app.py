import flask
from flask import request, jsonify, send_from_directory
from resources.servers import *
from resources.services import *
from src.service_actions import *
from src.db_actions import *
from src.openshift_actions import *
#from src.error_handlers import *
from resources.login_details import *
from src.swagger import swaggerui_blueprint, SWAGGER_URL, REQUEST_API
DEBUG_MODE = True  # Change to False if you want to run without debug mode!

# Sets the app, DEBUG mode and registers to swagger service
app = flask.Flask(__name__)
app.config["DEBUG"] = DEBUG_MODE
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(REQUEST_API)


# Route to static resources on demand
@app.route('/static/<path:path>', methods=['GET'])
def send_static(path):
    return send_from_directory('static', path)


# http://localhost:5000/
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Portal Shavit Project</h1>
              <p>This site is a prototype API for Portal-Shavit.</p>'''


# http://localhost:5000/api/v1/shavit/resources/users
# Returns all users
@app.route('/api/v1/shavit/resources/users', methods=['GET'])
def api_all_users():
    return jsonify(USERS)


# http://localhost:5000/api/v1/shavit/resources/servers
# Returns all servers
# http://localhost:5000/api/v1/shavit/resources/servers?serverGroupName=openshift
# Returns all servers of server group, in this example all openshift servers
@app.route('/api/v1/shavit/resources/servers', methods=['GET'])
def api_servers_by_group_name():
    if 'serverGroupName' in request.args:
        serverGroupName = str(request.args['serverGroupName']).upper()
    elif 'serverGroupName' not in request.args:
        return jsonify(SERVERS)
    else:
        return "Error: No id field provided. Please specify an server group name!"
    results = return_all_servers_of_group(serverGroupName)
    return jsonify(results)


# http://localhost:5000/api/v1/shavit/actions/servers/service?serverName=<OUR_IP>&serviceName=docker&actionType=status
# Performs the wanted service action on the wanted service on the wanted server
# Checks if the service is valid from services.py file!
@app.route('/api/v1/shavit/actions/servers/service', methods=['GET'])
def api_service_action():
    if 'actionType' in request.args:
        actionType = str(request.args['actionType'])
    else:
        return "Error: Bad arguments. Please specify valid server and service name, and action type!"
    output = action_on_service(request.args, actionType, MY_USERNAME, MY_PASS)
    return output


# http://localhost:5000/api/v1/shavit/resources/servers/services?serverGroupName=openshift
# Returs all the services wanted for the servers in server group chosen
# Checks if the service is valid from services.py file!
@app.route('/api/v1/shavit/resources/servers/services', methods=['GET'])
def api_all_services_of_server_type():
    if 'serverGroupName' in request.args:
        serverGroupName = str(request.args['serverGroupName']).upper()
    else:
        return "Error: Bad arguments. Please specify valid server group name!"
    output = get_all_services_of_server_group(serverGroupName)
    return jsonify(output)


# http://localhost:5000/api/v1/shavit/dbs
# Returns all available types of dbs we have
# http://localhost:5000/api/v1/shavit/dbs?dbType=postgres
# Returns all dbs of postgres / mongo / oracle
@app.route('/api/v1/shavit/dbs', methods=['GET'])
def api_get_dbs():
    if 'dbType' in request.args:
        dbType = str(request.args['dbType'])
    elif 'dbType' not in request.args:
        return jsonify(DATABASES)
    output = get_all_dbs(dbType)
    return jsonify(output)


# http://localhost:5000/api/v1/shavit/dbs/backup_files?dbType=postgres&resourceType=all
# Get dmps of ALL dbs of postgres / mongo / oracle
# http://localhost:5000/api/v1/shavit/dbs/backup_files?dbType=postgres&resourceType=db
# Get dmps of SPECIFIC db of postgres / mongo / oracle
# http://localhost:5000/api/v1/shavit/dbs/backup_files?dbType=postgres&resourceType=schema
# Get dmps of SPECIFIC schema of postgres / oracle
# http://localhost:5000/api/v1/shavit/dbs/backup_files?dbType=mongo&resourceType=collection
# Get dmps of SPECIFIC collection of mongo
@app.route('/api/v1/shavit/dbs/backup_files', methods=['GET'])
def api_get_dump_files_to_restore_from_dbs():
    if ('dbType' in request.args) and ('resourceType' in request.args):
        dbType = str(request.args['dbType'])
        resourceType = str(request.args['resourceType'])
    elif 'dbType' not in request.args:
        return 'Error: Bad arguments. Please specify valid dbType! (postgres / mongo / oracle)'
    output = get_backup_files_by_type(dbType, resourceType)
    return jsonify(output)


# TODO: Check with wanted user to see if correct owner of db
# http://localhost:5000/api/v1/shavit/dbs/create?dbType=postgres&dbName=testdb
# Creates new db in postgres / mongo / oracle
@app.route('/api/v1/shavit/dbs/create', methods=['GET'])
def api_create_db():
    if ('dbType' in request.args) and ('dbName' in request.args):
        dbType = str(request.args['dbType'])
        dbName = str(request.args['dbName'])
    else:
        return "Error: Bad arguments. Please specify valid db type and new db name!"
    output = crete_db(dbType, dbName)
    return str(output)


# http://localhost:5000/api/v1/shavit/dbs/backup?dbType=postgres
# Takes backup of ALL dbs of postgres / mongo / oracle
@app.route('/api/v1/shavit/dbs/backup', methods=['GET'])
def api_backup_all_dbs():
    if 'dbType' in request.args:
        dbType = str(request.args['dbType'])
    elif 'dbType' not in request.args:
        return 'Error: Bad arguments. Please specify valid dbType! (postgres / mongo / oracle)'
    output = backup_all_dbs(dbType)
    return jsonify(output)


# http://localhost:5000/api/v1/shavit/dbs/restore?dbType=postgres
# Restores ALL dbs of postgres / mongo / oracle
@app.route('/api/v1/shavit/dbs/restore', methods=['GET'])
def api_restore_all_dbs():
    if 'dbType' in request.args:
        dbType = str(request.args['dbType'])
    elif 'dbType' not in request.args:
        return 'Error: Bad arguments. Please specify valid dbType! (postgres / mongo / oracle)'
    output = restore_all_dbs(dbType)
    return jsonify(output)


# TODO: ################################################
# TODO: Add to swagger.json and README.md files!!!!!!! #
# TODO: ################################################
# http://localhost:5000/api/v1/shavit/dbs/master?dbType=postgres
# Retruns the master of the db cluster of postgres / mongo / oracle
@app.route('/api/v1/shavit/dbs/master', methods=['GET'])
def api_get_master_of_db_cluster():
    if 'dbType' in request.args:
        dbType = str(request.args['dbType'])
    elif 'dbType' not in request.args:
        return 'Error: Bad arguments. Please specify valid dbType! (postgres / mongo / oracle)'
    output = get_master_of_db_cluster(dbType)
    return jsonify(output)


# TODO: Login to ocp cluster as wanted user, infra or simple user
# TODO: Change params to func to be not hard-coded
# http://localhost:5000/api/v1/shavit/ocp/login
# Login to ocp cluster
@app.route('/api/v1/shavit/ocp/login/infra', methods=['GET'])
def ocp_root_login():
    output = oc_root_login(MY_USERNAME, MY_PASS, OCP_ROOT_USERNAME, OCP_ROOT_PASSWORD, TEMP_SERVER_NAME)
    return output


# TODO: Change params to func to be not hard-coded
# http://localhost:5000/api/v1/shavit/ocp/projects
# Returns all projects in the ocp cluster
@app.route('/api/v1/shavit/ocp/projects', methods=['GET'])
def ocp_all_projects():
    output = oc_projects(MY_USERNAME, MY_PASS, OCP_ROOT_USERNAME, OCP_ROOT_PASSWORD, TEMP_SERVER_NAME)
    return jsonify(output)


# TODO: Change params to func to be not hard-coded
# http://localhost:5000/api/v1/shavit/ocp/services?project=myproject
# Returns all services in chosen project
@app.route('/api/v1/shavit/ocp/services', methods=['GET'])
def ocp_get_all_svc_in_project():
    if 'project' in request.args:
        project = str(request.args['project'])
    elif 'project' not in request.args:
        return 'Error: Bad arguments. Please specify valid project name!'
    output = oc_services_in_project(MY_USERNAME, MY_PASS, OCP_ROOT_USERNAME, OCP_ROOT_PASSWORD, project, TEMP_SERVER_NAME)
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
