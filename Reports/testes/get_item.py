# -*- coding: utf-8 -*-
# This python code import zabbix-api bib for connect in zabbix 3.4 API from zabbix-server docker host 10.10.10.3 and generate customs reports
import sys
import re
from zabbix_api import ZabbixAPI

#Variables
ZABBIX_SERVER='http://10.81.244.56/zabbix'
ZUSER='Admin'
ZPASS='zabbix'

#API Rules
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login(ZUSER, ZPASS)

item = zapi.item.get({
#    "params": {
#        "output": "extend",
#        "hostids": "10254",
#        "itemid": "28272",
#        "time_from": "1530414000",
#        "time_till": "1533006000"
#        "status": 0,
#        "search": {
#            "key_": "vfs.fs.size[C:,free]"
#        },
#        "sortfield": "name"
        }
)
host_id='10256'
item_root = "vfs.fs.size[/,total]"
for i in item:
    if host_id == i["hostid"] and item_root == i["key_"]:
        global part_name
        part_name = "/root"
        disc_root = i["lastvalue"]
        disc_root_int = int(disc_root) / 1024.0 / 1024.0 /1024.0
        global total_root
        total_root = round(disc_root_int)
        total_root = str(total_root)+" GB"

    else:
        part_name = "uyu"
        total_root = "uyu"

print part_name
print total_root

#    elif host_id == i["hostid"] and item_root != i["key_"]:
#        part_name = "Item não encontrado"
#        total_root = "Item não encontrado"

#item_key = 'CPU Model'
#for i in item:
#    if host_id == i["hostid"] and i["name"] == item_key:
#        cpu = i['lastvalue']
#        cpu_slice = cpu.split("\n")[0]
#        cpu_model = cpu_slice[13: ]
#        print cpu_model
#        cpu_list.append(cpu_model)
#        print cpu_list[0:7]
#        os_distro = i['lastvalue']
#        os_system = os_distro.split("Microsoft")[1]
#        print os_system
#        item_id = i['itemid']
#        print item_id
#for i in item:
#    if host_id == i["hostid"] and i["itemid"] == '30234':
#        print i
#        if i['lastvalue'] == '0':
#            print "Sem valor"
#            kb_totalmem = i["lastvalue"]
#            kb_totalmem_int = float(kb_totalmem)
#            gb_totalmem = kb_totalmem_int / 1024.0 / 1024.0 / 1024.0
#            global total_mem
#            total_mem = round(gb_totalmem)

#        os_distro = i['lastvalue']
#        os_system = os_distro.split("Microsoft")[1]
#        cpu_model = i['lastvalue']
#        cpu_model = cpu.split(":")[1]
#        print cpu_model

#        cpu_utilization = i['lastvalue']
#        cpu_utilization = float(cpu_utilization)
#        cpu_utilization = round(cpu_utilization,2)
#        cpu_utilization = str(cpu_utilization)+"%"
#        print cpu_utilization


#        result = re.search('Microsoft', valor)
#        os_system = result.group(0)
#        print os_system
#        for i,v in enumerate(valor):
#            print i,v
#        for v in variavel:
#            print v
#        for l in i['lastvalue']:
#            print l
#        kb_mem = i["prevvalue"]
#        print kb_mem
#        total_mem = int(kb_mem)
#        total_gb = total_mem / 1024.0 / 1024.0 / 1024.0
#        print total_gb, "GB"

#API and python Commands to get total memory. Necessary get itemid first
#item = zapi.item.get({})
#host_id = '10267'
#item_id = '28829'
#for i in item:
#    if host_id == i["hostid"] and item_id == i["itemid"]:
#        total_disk = i["lastvalue"]
#        total_disk_int = int(total_disk) / 1024 / 1024 / 1024
#        total_disk_gb = total_disk_int
#        print total_disk_gb, "GB"
#        if i['name'] == 'Free disk space on $1':
#            partition = 'C:'
#            print partition

#API and python Commands to get total memory. Necessary get itemid first
#item = zapi.item.get({
#    "hostids" : [
#        10254
#    ],
#    "itemids": [
#        28290
#    ]
#})
#for i in item:
#    kb_mem = i["prevvalue"]
#    total_mem = int(kb_mem)
#    total_gb = total_mem / 1024.0 / 1024.0 / 1024.0
#    print total_gb, "GB"

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
