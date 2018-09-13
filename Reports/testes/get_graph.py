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

#graph = zapi.graph.get({
#    "params": {
#        "output": "extend",
#        "hostids": "10254",
#        "graphid": "794",
#        "search": {
#            "key_": "vm.memory.size[total]"
#        },
#        "sortfield": "name"
#        }
#    }
#)
#host_id='10254'
#for g in graph:
#    print g
#for i in item:
#    if host_id == i["hostid"] and i["itemid"] == '28290':
#        kb_mem = i["prevvalue"]
#        total_mem = int(kb_mem)
#        total_gb = total_mem / 1024.0 / 1024.0 / 1024.0
#        print total_gb, "GB"

#API and python Commands to get total memory. Necessary get itemid first
#graph = zapi.graph.get({})
#host = zapi.host.get({})
#graph_name = 'CPU'
#for g in graph:
#    if g['hostids'] == host_id and g['graphid'] == 794:
#        print g
#for g in graph:
#    if g["name"] == graph_name:
#    if g['name'] == 'memory':
#        print g['graphid']
#        processes = i["lastvalue"]
#        uptime_sec_int = int(uptime_sec) / 60
#        total_uptime = uptime_sec_int
#        print total_uptime, "minutos"

########################################################
#################### FUNCIONA ##########################
########################################################

host_id = 10280
graph_name = zapi.graph.get({})
for g in graph_name:
    if g['name'] == 'Memory':
        search_id = g['graphid']

        graph = zapi.graph.get({

        "hostids" : [
            host_id
        ],
        "graphids": [
            search_id
        ],
        "history": 0,
        "output": "extend",
        })
        if g in graph:
            graph_id = g['graphid']
            print graph_id

#########################################################
######################## FIM ############################
#########################################################

#host_id='10254'
#item_id='28290'
#for i in item:
#    if host_id == i["hostid"] and item_id == i["itemid"]:
#        template_id = i["templateid"]
#        print template_id
#        kb_mem = i["prevvalue"]
#        total_mem = int(kb_mem)
#        total_gb = total_mem / 1024.0 / 1024.0 / 1024.0
#        print total_gb, "GB"
