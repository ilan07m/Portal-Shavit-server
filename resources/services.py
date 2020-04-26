# SERVICES_LIST =['firewalld', 'docker']

SERVICES_LIST = {'OPENSHIFT': ['atomic-openshift-node', 'docker', 'firewalld', 'iptables'],
                 'POSTGRES': ['firewalld', 'iptables'],
                 'POSTGRES_LOGI': [],
                 'MONGO': ['mongod', 'firewalld', 'iptables'],
                 'ORACLE': ['firewalld', 'iptables'],
                 'KAFKA': ['kafka', 'zookeeper', 'firewalld', 'iptables'],
                 'JENKINS': ['docker', 'firewalld', 'iptables'],
                 'NEXUS': ['nexus', 'docker'],
                 'DOCKER': ['docker', 'firewalld', 'iptables'],
                 'ANSIBLE': ['docker', 'firewalld', 'iptables'],
                 'SPLUNK': ['splunk', 'firewalld', 'iptables']}


def get_all_services_of_server_group(serverGroupName):
    services = []
    for serverGroup in SERVICES_LIST:
        if serverGroup == serverGroupName:
            services.append(SERVICES_LIST[serverGroup])
    return services[0]
