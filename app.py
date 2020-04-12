import flask
from flask import request, jsonify, send_from_directory
from resources.servers import *
from src.service_actions import *
from src.db_actions import *
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


# TODO: Make it without the /all --> check if there is no params in the url then return all servers
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


# http://localhost:5000/api/v1/shavit/dbs/postgres/dbs
# Returns all postgres dbs
@app.route('/api/v1/shavit/dbs/postgres/dbs', methods=['GET'])
def api_pg_dbs():
    return jsonify(pg_dbs())


# http://localhost:5000/api/v1/shavit/dbs/mongo/dbs
# Returns all mongo dbs
@app.route('/api/v1/shavit/dbs/mongo/dbs', methods=['GET'])
def api_mongo_dbs():
    return jsonify(mongo_dbs())

# TODO: Return Oracle dbs API


if __name__ == '__main__':
    app.run(host='0.0.0.0')
