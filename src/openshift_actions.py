from .ssh_commands import *
from resources.login_details import *
OC_LOGIN = 'oc login -u {} -p {}'
OC_PROJECT = 'oc project {}'
OC_PROJECTS = 'oc projects -q'
OC_NEW_APP = 'oc new-app {}:{}/{} --insecure-registry'
OC_IMPORT_IMAGE = 'oc import-image {}'
OC_GET_SERVICES = 'oc get svc -o custom-columns=NAME:.metadata.name --no-headers'  # Returns only services names


# Logs into ocp
def oc_root_login(hostUsername, hostPassword, ocUsername, ocPassword, host):
    output = run_command(OC_LOGIN.format(ocUsername, ocPassword), connect_to_server(host, hostUsername, hostPassword))
    return output


# Returns all projects
def oc_projects(hostUsername, hostPassword, ocUsername, ocPassword, host):
    commands = []
    projectsList = []
    login = OC_LOGIN.format(ocUsername, ocPassword)
    projects = OC_PROJECTS
    commands.extend([login, projects])
    output = run_multiple_commands(commands, connect_to_server(host, hostUsername, hostPassword))
    splitedProjects = output[1].splitlines()
    for project in splitedProjects:
        projectsList.append(project.decode('UTF-8'))
    return projectsList


# Returns all services in chosen project
def oc_services_in_project(hostUsername, hostPassword, ocUsername, ocPassword, ocProject, host):
    commands =[]
    login = OC_LOGIN.format(ocUsername, ocPassword)
    project = OC_PROJECT.format(ocProject)
    services = OC_GET_SERVICES
    commands.extend([login, project, services])
    output = run_multiple_commands(commands, connect_to_server(host, hostUsername, hostPassword))
    return output[2].decode('UTF-8').splitlines()


# TODO: Check if working
# Makes new-app in wanted project with wanted image
def oc_new_app(hostUsername, hostPassword, ocUsername, ocPassword, ocProject, ocAppName, host):
    commands = []
    login = OC_LOGIN.format(ocUsername, ocPassword)
    project = OC_PROJECT.format(ocProject)
    newApp = OC_NEW_APP.format(OPENSHIFT_REGISTRY, OPENSHIFT_REGISTRY_PORT, ocAppName)
    commands.extend([login, project, newApp])
    output = run_multiple_commands(commands, connect_to_server(host, hostUsername, hostPassword))
    return output


# TODO: Check if working
# Imports the latest version of the image chosen in the project chosen
def oc_import_image(hostUsername, hostPassword, ocUsername, ocPassword, ocProject, ocAppName, host):
    commands = []
    login = OC_LOGIN.format(ocUsername, ocPassword)
    project = OC_PROJECT.format(ocProject)
    importApp = OC_IMPORT_IMAGE.format(ocAppName)
    commands.extend([login, project, importApp])
    output = run_multiple_commands(commands, connect_to_server(host, hostUsername, hostPassword))
    return output
