# -*- coding: utf-8 -*-
# This python code import zabbix-api bib for connect in zabbix 3.4 API from zabbix-server docker host 10.10.10.3 and generate customs reports
import sys
from zabbix_api import ZabbixAPI

#Variables
ZABBIX_SERVER='http://10.10.10.4'
ZUSER='Admin'
ZPASS='zabbix'

#API Rules
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login(ZUSER, ZPASS)

#for host in zapi.host.get({'groupids': '2'}):
#    print host
#for item in zapi.item.get({'host':'zabbix-agent', 'name' : 'Processor load (5 min average per core)'}):
#    print item

#hosts = zapi.host.get({})
#name = 'zabbix-agent'
#for h in hosts:
#    if h["name"] == name:
#        name_id = h["hostid"]

time_from = 1532954700
time_till = 1533121200
system_cpu_util = zapi.history.get({
    "itemids" : [
        28273
    ],
    "history": 0,
    "output": "extend",
    "time_from": time_from,
    "time_till": time_till
})
for h in system_cpu_util:
    print h


