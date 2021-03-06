import paramiko
SSH_PORT = 22
ACTIVE = "ACTIVE"
INACTIVE = "INACTIVE"


# Connects to the server
def connect_to_server(serverName, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(serverName, SSH_PORT, username, password)
    return ssh


# Runs the command on the server
def run_command(command, ssh):
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read()
    error = stderr.readlines()
    if len(error) != 0:
        print(error)
    ssh.close()
    return output


# Runs the commands on the server
def run_multiple_commands(commands, ssh):
    returnOutput = []
    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read()
        returnOutput.append(output)
        error = stderr.readlines()
        if len(error) != 0:
            print(error)
    ssh.close()
    return returnOutput
