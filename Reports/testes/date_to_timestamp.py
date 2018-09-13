# -*- coding: utf-8 -*-
# This python code import zabbix-api bib for connect in zabbix 3.4 API from zabbix-server docker host 10.10.10.3 and generate customs reports
import sys
import time
import datetime
from zabbix_api import ZabbixAPI

#Variables
ZABBIX_SERVER='http://10.10.10.4'
ZUSER='Admin'
ZPASS='zabbix'

#API Rules
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login(ZUSER, ZPASS)

# Datetime opcao1

print "Digite a data inicial abaixo: "
day_from = raw_input("Digite o dia: ")
month_from = raw_input("Digite o mês: ")
year_from = raw_input("Digite o ano: ")

print "Digite a data final abaixo: "
day_till = raw_input("Digite o dia: ")
month_till = raw_input("Digite o mês: ")
year_till = raw_input("Digite o ano: ")
stime = year_from+month_from+day_from+"000000"

date1 = datetime.datetime(int(year_from), int(month_from), int(day_from), 00, 00, 00)
date2 = datetime.datetime(int(year_till), int(month_till), int(day_till), 00, 00, 00)
date_seconds = (date2-date1).total_seconds()
date_seconds = int(date_seconds)

print "Total de segundos é: ",date_seconds
print "Stime é: ",stime



#cpu_idle_time = zapi.history.get({
#    "itemids" : [
#        28272
#    ],
#    "history": 0,
#    "output": "extend",
#    "time_from": date_from,
#    "time_till": date_till,
#})
#for h in cpu_idle_time:
#    cpu_idle_time_id = h['itemid']
#    cpu_idle_time_id = str(cpu_idle_time_id)
#
#cpu_interrupt_time = zapi.history.get({
#    "itemids" : [
#        28273
#    ],
#    "history": 0,
#    "output": "extend",
#    "time_from": date_from,
#    "time_till": date_till,
#})
#for h in cpu_interrupt_time:
#    cpu_interrupt_time_id = h['itemid']
#    cpu_interrupt_time_id = str(cpu_interrupt_time_id)
#
#cpu_iowait_time = zapi.history.get({
#    "itemids" : [
#        28274
#    ],
#    "history": 0,
#    "output": "extend",
#    "time_from": date_from,
#    "time_till": date_till,
#})
#for h in cpu_iowait_time:
#    cpu_iowait_time_id = h['itemid']
#    cpu_iowait_time_id = str(cpu_iowait_time_id)
#
#cpu_user_time = zapi.history.get({
#    "itemids" : [
#        28279
#    ],
#    "history": 0,
#    "output": "extend",
#    "time_from": date_from,
#    "time_till": date_till,
#})
#for h in cpu_user_time:
#    cpu_user_time_id = h['itemid']
#    cpu_user_time_id = str(cpu_user_time_id)
#
#cpu_system_time = zapi.history.get({
#    "itemids" : [
#        28278
#    ],
#    "history": 0,
#    "output": "extend",
#    "time_from": date_from,
#    "time_till": date_till,
#})
#for h in cpu_system_time:
#    cpu_system_time_id = h['itemid']
#    cpu_system_time_id = str(cpu_system_time_id)
#
#cpu_steal_time = zapi.history.get({
#    "itemids" : [
#        28277
#    ],
#    "history": 0,
#    "output": "extend",
#    "time_from": date_from,
#    "time_till": date_till,
#})
#for h in cpu_steal_time:
#    cpu_steal_time_id = h['itemid']
#    cpu_steal_time_id = str(cpu_steal_time_id)
#
#cpu_nice_time = zapi.history.get({
#    "itemids" : [
#        28275
#    ],
#    "history": 0,
#    "output": "extend",
#    "time_from": date_from,
#    "time_till": date_till,
#})
#for h in cpu_nice_time:
#    cpu_nice_time_id = h['itemid']
#    cpu_nice_time_id = str(cpu_nice_time_id)
#
#cpu_softirq_time = zapi.history.get({
#    "itemids" : [
#        28276
#    ],
#    "history": 0,
#    "output": "extend",
#    "time_from": date_from,
#    "time_till": date_till,
#})
#for h in cpu_softirq_time:
#    cpu_softirq_time_id = h['itemid']
#    cpu_softirq_time_id = str(cpu_softirq_time_id)
#
#create_graph = zapi.graph.create({
#    "name":"Informações de processamento mensal",
#    "width":900,
#    "height":200,
#    "gitems": [{
#        "itemid":cpu_idle_time_id,
#        "color": "009900",
#        "drawtype":1,
#        "graphtype":2,
#        "yaxismin":0.000,
#        "yaxismax":100.0000,
#        "yaxisside":0
#        },
#        {"itemid":cpu_user_time_id,
#        "color": "000099",
#        "drawtype":1,
#        "graphtype":2,
#        "yaxismin":0.000,
#        "yaxismax":100.0000,
#        "yaxisside":0
#        },
#        {"itemid":cpu_system_time_id,
#        "color": "990000",
#        "drawtype":1,
#        "graphtype":2,
#        "yaxismin":0.000,
#        "yaxismax":100.0000,
#        "yaxisside":0
#        },
#        {"itemid":cpu_iowait_time_id,
#        "color": "999900",
#        "drawtype":1,
#        "graphtype":2,
#        "yaxismin":0.000,
#        "yaxismax":100.0000,
#        "yaxisside":0
#        },
#        {"itemid":cpu_nice_time_id,
#        "color": "990099",
#        "drawtype":1,
#        "graphtype":2,
#        "yaxismin":0.000,
#        "yaxismax":100.0000,
#        "yaxisside":0
#        },
#        {"itemid":cpu_interrupt_time_id,
#        "color": "009999",
#        "drawtype":1,
#        "graphtype":2,
#        "yaxismin":0.000,
#        "yaxismax":100.0000,
#        "yaxisside":0
#        },
#        {"itemid":cpu_softirq_time_id,
#        "color": "55FF55",
#        "drawtype":1,
#        "graphtype":2,
#        "yaxismin":0.000,
#        "yaxismax":100.0000,
#        "yaxisside":0
#        },
#        {"itemid":cpu_steal_time_id,
#        "color": "FF5555",
#        "drawtype":1,
#        "graphtype":2,
#        "yaxismin":0.000,
#        "yaxismax":100.0000,
#        "yaxisside":0
#        }
#        ]
#    }
#)
