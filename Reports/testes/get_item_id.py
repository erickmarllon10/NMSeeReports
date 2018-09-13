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

#item = zapi.item.get({
#    "params": {
#        "output": "extend",
#        "hostids": "10254",
#        "itemid": "28290",
#        "search": {
#            "key_": "vm.memory.size[total]"
#        },
#        "sortfield": "lastvalue"
#        }
#    }
#)


#item = zapi.item.get({})
#host_id='10254'
#template_id='10026'
#for i in item:
#    if host_id == i["hostid"] and template_id == i["templateid"]:
#        item_id = i["itemid"]
#        print item_id

cpu_idle_time = zapi.history.get({
    "itemids" : [
        28272
    ],
    "history": 0,
    "output": "extend",
    "time_from": "1530454300",
    "time_till": "1533046300"
})

for i in cpu_idle_time:
    print i


#host_id='10254'
#for i in item:
#    if host_id == i["hostid"] and i["itemid"] == '28290':
#        print i
#        kb_mem = i["lastvalue"]
#        total_mem = int(kb_mem)
#        total_gb = total_mem / 1024.0 / 1024.0 / 1024.0
#        print round(total_gb), "GB"
