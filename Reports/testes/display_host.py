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

#hostgroup = zapi.hostgroup.get({})
#for hg in hostgroup:
#    print hg

item = zapi.item.get({})
for i in item:
    print i

hosts = zapi.host.get({})
name = 'zabbix-agent'
for h in hosts:
    if h["name"] == name:
        name_id = h["hostid"]
        print type(name_id)

gethost = zapi.host.get({
    "params": {
        "selectInventory": True,
        "selectitems": [
            "name",
            "lastvalue",
            "units",
            "itemid",
            "lastclock",
            "value_type",
            "itemid"
        ],
        "output":"extend",
        "hostids":name_id,
        "expandDescription":1,
        "expandData":1
    }

})

#
#
#interfaces = zapi.hostinterface.get ({
#    "ouput": [
#        "hostid",
#        "ip",
#        "type"
#    ]
#})
#for i in interfaces:
#    if name_id == i["hostid"]:
#        name_ip = i["ip"]
#        print name_ip
