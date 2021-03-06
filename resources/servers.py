#  Dictionary is built as: server-group as KEY, and list of all the servers of the group as the VALUE
SERVERS = [{"OPENSHIFT": [{"name": "openshift-haproxy"},
                          {"name": "openshift-master1"},
                          {"name": "openshift-master2"},
                          {"name": "openshift-master3"},
                          {"name": "openshift-infra1"},
                          {"name": "openshift-infra2"},
                          {"name": "openshift-infra3"},
                          {"name": "openshift-app1"},
                          {"name": "openshift-app2"},
                          {"name": "openshift-app3"},
                          {"name": "openshift-app4"},
                          {"name": "openshift-app5"},
                          {"name": "openshift-app6"}]},
           {"POSTGRES": [{"name": "pg1"},
                         {"name": "pg2"}]},
           {"POSTGRES_LOGI": [{"name": "pglogi1"},
                              {"name": "pglogi2"}]},
           {"MONGO": [{"name": "mongo1"},
                      {"name": "mongo2"},
                      {"name": "mongo3"}]},
           {"ORACLE": [{"name": "mora1"},
                       {"name": "mora2"},
                       {"name": "pora1"},
                       {"name": "pora2"}]},
           {"KAFKA": [{"name": "kafka1"},
                      {"name": "kafka2"},
                      {"name": "kafka3"}, ]},
           {"JENKINS": [{"name": "jenkins1"},
                        {"name": "jenkins2"},
                        {"name": "jenkins3"}, ]},
           {"NEXUS": [{"name": "nexus3"}]},
           {"DOCKER": [{"name": "docker"}]},
           {"ANSIBLE": [{"name": "ansible"}]},
           {"SPLUNK": [{"name": "splunk"}]}
           ]

PASSWORDS = {"ADMIN": {"OPENSHIFT": {"rootUser": "username",
                                     "rootPassword": "password",
                                     "ocUser": "username",
                                     "ocPassword": "password"},
                       "POSTGRES": {"rootUser": "username",
                                    "rootPassword": "password",
                                    "pgUser": "user",
                                    "pgPassword": "password"},
                       "POSTGRES_LOGI": {"rootUser": "username",
                                         "rootPassword": "password",
                                         "pgUser": "user",
                                         "pgPassword": "password"},
                       "MONGO": {"rootUser": "username",
                                 "rootPassword": "password",
                                 "mongodUser": "username",
                                 "mongodPassword": "password",
                                 "dbAdminUser": "username",
                                 "dbAdminPassword": "password"},
                       "ORACLE": {"rootUser": "username",
                                  "rootPassword": "password",
                                  "dbAdminUser": "username",
                                  "dbAdminPassword": "password"},
                       "KAFKA": {"rootUser": "username",
                                 "rootPassword": "password",
                                 "kafkaAdminUser": "username",
                                 "kafkaAdminPassword": "password"},
                       "JENKINS": {"rootUser": "username",
                                   "rootPassword": "password"},
                       "NEXUS": {"rootUser": "username",
                                 "rootPassword": "password",
                                 "nexusAdminUser": "username",
                                 "nexusAdminPassword": "password"},
                       "DOCKER": {"rootUser": "username",
                                  "rootPassword": "password",
                                  "dockerAdminUser": "username",
                                  "dockerAdminPassword": "password"},
                       "ANSIBLE": {"rootUser": "username",
                                   "rootPassword": "password"},
                       "SPLUNK": {"rootUser": "username",
                                  "rootPassword": "password"}},
             "LOGI": {"OPENSHIFT": {"user": "username",
                                    "password": "password",
                                    "ocUser": "username",
                                    "ocPassword": "password"},
                      "POSTGRES": {"user": "username",
                                   "password": "password",
                                   "pgUser": "user",
                                   "pgPassword": "password"},
                      "POSTGRES_LOGI": {"user": "username",
                                        "password": "password",
                                        "pgUser": "user",
                                        "pgPassword": "password"},
                      "MONGO": {"user": "username",
                                "password": "password",
                                "dbUser": "username",
                                "dbPassword": "password"},
                      "ORACLE": {"user": "username",
                                 "password": "password",
                                 "dbUser": "username",
                                 "dbPassword": "password"},
                      "KAFKA": {"user": "username",
                                "password": "password",
                                "kafkaUser": "username",
                                "kafkaPassword": "password"},
                      "JENKINS": {"user": "username",
                                  "password": "password"},
                      "NEXUS": {"user": "username",
                                "password": "password",
                                "nexusUser": "username",
                                "nexusPassword": "password"},
                      "DOCKER": {"user": "username",
                                 "password": "password",
                                 "dockerUser": "username",
                                 "dockerPassword": "password"},
                      "ANSIBLE": {"user": "username",
                                  "password": "password"},
                      "SPLUNK": {"user": "username",
                                 "password": "password"}}
             }

DATABASES = ["postgres", "mongo", "oracle"]


# Returns all servers of server group
def return_all_servers_of_group(serverGroupName):
    results = []
    for servers in SERVERS:
        for serverGroup in servers:
            if serverGroup == serverGroupName:
                for server in servers[serverGroup]:
                    results.append(server['name'])
                    print(server['name'])
    return results


def get_all_servers_by_server_group_as_dict():
    serversDict = {}
    for serverGroups in SERVERS:
        serverGroupName = ''
        for server in serverGroups:
            serverGroupName = server
        serversDict[serverGroupName] = serverGroups
    return(serversDict)


def get_names_of_server_of_server_group(serverGroup):
    serversNames = []
    serversList = get_all_servers_by_server_group_as_dict()[serverGroup].values()
    for dict in serversList:
        for name in dict:
            serversNames.append(name['name'])
    return serversNames
