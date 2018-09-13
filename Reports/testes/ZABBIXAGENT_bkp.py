#coding: utf-8

# This python code import zabbix-api bib for connect in zabbix 3.4 API from zabbix-server docker host 10.10.10.3 and generate customs reports

import sys
from datetime import datetime,date
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://10.10.10.4")
zapi.login("Admin", "zabbix")

# collect ip from host using zabbix api
hosts = zapi.host.get({
    "output": [
    "hostid",
    "name"
]})

name = 'zabbix-agent'
for h in hosts:
    if h["name"] == name:
        name_id = h["hostid"]

interfaces = zapi.hostinterface.get ({
    "ouput": [
    "hostid",
    "ip",
    "type"
]})

for i in interfaces:
    if name_id == i["hostid"]:
        name_ip = i["ip"]


def zabbixagent():
    print "\
            Manutenção preventiva de servidores \n \
            Data de revisão:",datetime.now().strftime("%d/%m/%Y")," \n \
            DADOS GERAIS DO SERVIDOR \n \
            Nome: SEETFS04 | IP:",name_ip," | Windows Server 2012 R2 Standard | Ambiente: VMWARE \n \
            Serviço: Servidor de build TFS 2 | Localidade: SEDE \n \
            Modelo(s) do(s) Processado(res): Intel® Xeon® CPU ES - 2650 v2 @ 2.60GHz | Quantidade de Processadoress/Núcleos: 2 socket / 1 núcleo(s)"

