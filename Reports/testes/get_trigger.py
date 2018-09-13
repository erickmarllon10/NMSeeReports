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

item = zapi.trigger.get({})
for i in item:
    print i
