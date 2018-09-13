# -*- coding: utf-8 -*-
# This python code import zabbix-api bib for connect in zabbix 3.4 API from zabbix-server docker host 10.10.10.3 and generate customs reports
import sys
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://10.10.10.4")
zapi.login("Admin", "zabbix")
events = zapi.event.get({
    "output": "extend",
    "time_from": "1530576000",
    "time_till": "1532703600",
    "sortfield": [
        "clock",
        "eventid"
    ],
    "sortorder": "DESC"
})
print events

