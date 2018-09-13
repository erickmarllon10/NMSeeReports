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

# Get Total Memory
item = zapi.item.get({})
host_id = '10254'
item_id_totalmem = '28290'
for i in item:
    if host_id == i["hostid"] and item_id_totalmem == i["itemid"]:
        kb_totalmem = i["prevvalue"]
        kb_totalmem_int = int(kb_totalmem)
        gb_totalmem = kb_totalmem_int / 1024.0 / 1024.0 / 1024.0
        total_mem = round(gb_totalmem)
        total_mem = str(total_mem)

#API and python Commands to get available memory. Necessary get itemid first. Available memory is defined as free, cache and buffers memory
item_id_free = '28289'
for i in item:
    if host_id == i["hostid"] and item_id_free == i["itemid"]:
        kb_freemem = i["prevvalue"]
        kb_freemem_int = int(kb_freemem)
        gb_freemem = kb_freemem_int / 1024.0 / 1024.0 / 1024.0
        total_freemem = round(gb_freemem)
        total_freemem = str(total_freemem)

# Calc Memory utilization in percent
total_mem_used = float(total_mem) - float(total_freemem)
total_mem_calc = float(total_mem) / 100
total_mem_utilization = total_mem_used / total_mem_calc
total_mem_utilization = str(total_mem_utilization)


