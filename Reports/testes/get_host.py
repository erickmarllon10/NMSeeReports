# -*- coding: utf-8 -*-
# This python code import zabbix-api bib for connect in zabbix 3.4 API from zabbix-server docker host 10.10.10.3 and generate customs reports
import sys
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://10.10.10.4")
zapi.login("Admin", "zabbix")

servername = 'zabbix-agent'
hosts = zapi.host.get({})
for h in hosts:
    if h["name"] == servername:
        global host_id
        host_id = h["hostid"]
        global host_name
        host_name = h["name"]
        global host_description
        host_description = h["description"]

        slicex = host_description.split("Ambiente: ")[1]
        print slicex

#for h in hosts:
#    if h['name'] == 'zabbix-agent':
#        print h
    #print "Nome:",h['name']," - Descrição:",h['description']," - Hostid:",h['hostid']," - Status:",h['status']
    #with open('add_host.py', 'a+') as host:
     #   host.append("nao sei")
     #   host.read()

#for line in f:
#    print line
#f.close()

