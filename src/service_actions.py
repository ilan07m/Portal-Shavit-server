from .ssh_commands import *
from resources.services import SERVICES_LIST
SERVICE_COMMAND = 'sudo systemctl '  # TODO: Remove sudo when all done!
ACTIVE_INDICATOR = 'Active'


def check_service_status(serviceName, serverName, username, password):
    output = run_command(SERVICE_COMMAND + 'status ' + serviceName + ' | grep Active',
                         connect_to_server(serverName, username, password))
    splitLine = str(output).split(":")  # Split the 'Active: active (running) since ...' by ":"
    status = splitLine[1].split(" ")  # Gets the current status from the line
    return status[1]


def stop_service(serviceName, serverName, username, password):
    output = run_command(SERVICE_COMMAND + 'stop ' + serviceName, connect_to_server(serverName, username, password))
    print_new_status(serviceName, serverName, username, password)
    return output


def start_service(serviceName, serverName, username, password):
    output = run_command(SERVICE_COMMAND + 'start ' + serviceName, connect_to_server(serverName, username, password))
    print_new_status(serviceName, serverName, username, password)
    return output


def restart_service(serviceName, serverName, username, password):
    output = run_command(SERVICE_COMMAND + 'restart ' + serviceName, connect_to_server(serverName, username, password))
    print_new_status(serviceName, serverName, username, password)
    return output


def print_new_status(serviceName, serverName, username, password):
    newServiceStatus = check_service_status(serviceName, serverName, username, password)
    print('------------------------------------------------------------------------')
    print('Now the ' + serviceName + ' service on ' + serverName + ' server is: ' + newServiceStatus)
    print('------------------------------------------------------------------------')


# Action type must be status start stop or restart
def action_on_service(args, actionType, username, password):
    if ('serverName' in args) & ('serviceName' in args):
        serverName = str(args['serverName'])
        serviceName = str(args['serviceName'])
        # TODO: check if server is from server list when all done
        if serviceName not in SERVICES_LIST:
            return "Error: No such service. Please specify an valid service!"
    else:
        return "Error: Bad arguments. Please specify valid server and service name!"
    if actionType == 'status':
        print('status is chosen!')
        output = check_service_status(serviceName, serverName, username, password)
    elif actionType == 'start':
        print('start is chosen!')
        output = start_service(serviceName, serverName, username, password)
    elif actionType == 'stop':
        print('stop is chosen!')
        output = stop_service(serviceName, serverName, username, password)
    elif actionType == 'restart':
        print('restart is chosen!')
        output = restart_service(serviceName, serverName, username, password)
    return output
