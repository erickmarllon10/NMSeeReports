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

# All CPU scripts bellow are used to calculate the total cpu utilization

# Get CPU Idle Time
item = zapi.item.get({})
host_id='10254'
for i in item:
    if host_id == i["hostid"] and i["itemid"] == '28272':
        cpu_idle = i["lastvalue"]
        cpu_idle_time = float(cpu_idle)

# Get CPU User Time
for i in item:
    if host_id == i["hostid"] and i["itemid"] == '28279':
        cpu_user = i["lastvalue"]
        cpu_user_time = float(cpu_user)

# Get CPU System Time
for i in item:
    if host_id == i["hostid"] and i["itemid"] == '28278':
        cpu_system = i["lastvalue"]
        cpu_system_time = float(cpu_system)

# Get CPU iowait Time
for i in item:
    if host_id == i["hostid"] and i["itemid"] == '28274':
        cpu_iowait = i["lastvalue"]
        cpu_iowait_time = float(cpu_iowait)

# Get CPU Nice Time
for i in item:
    if host_id == i["hostid"] and i["itemid"] == '28275':
        cpu_nice = i["lastvalue"]
        cpu_nice_time = float(cpu_nice)

# Get CPU Interrupt Time
for i in item:
    if host_id == i["hostid"] and i["itemid"] == '28273':
        cpu_interrupt = i["lastvalue"]
        cpu_interrupt_time = float(cpu_interrupt)

# Get CPU Softirq Time
for i in item:
    if host_id == i["hostid"] and i["itemid"] == '28276':
        cpu_softirq = i["lastvalue"]
        cpu_softirq_time = float(cpu_softirq)

# Get CPU Steal Time
for i in item:
    if host_id == i["hostid"] and i["itemid"] == '28277':
        cpu_steal = i["lastvalue"]
        cpu_steal_time = float(cpu_steal)

# Calc cpu utilization
cpu_utilization = 100.0 - cpu_idle_time - cpu_user_time - cpu_system_time - cpu_iowait_time - cpu_nice_time - cpu_interrupt_time - cpu_softirq_time - cpu_steal_time
print round(cpu_utilization,2)," %"

