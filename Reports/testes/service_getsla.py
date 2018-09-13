# -*- coding: utf-8 -*-
# This python code import zabbix-api bib for connect in zabbix 3.4 API from zabbix-server docker host 10.10.10.3 and generate customs reports
import sys
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://10.10.10.4")
zapi.login("Admin", "zabbix")
sla = zapi.service.getsla({
    "serviceids": "1",
    "intervals": [
        {
            "from":"1532887200",
            "to": "1532889600",
        }
    ]
}
)
print sla
