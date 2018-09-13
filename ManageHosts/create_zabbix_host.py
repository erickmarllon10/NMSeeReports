# -*- coding: utf-8 -*-
# This python code import zabbix-api bib for connect in zabbix 3.4 API from zabbix-server docker host 10.10.10.3 and create hosts

import sys
from zabbix_api import ZabbixAPI

def createhost():
    zapi = ZabbixAPI(server="http://192.168.1.0")
    zapi.login("Admin", "zabbix")
    zabbixhost = raw_input("Defina o nome do host: ")
    zabbixhostip = raw_input("Digite o ip do host %s: "%zabbixhost)
    group = zapi.hostgroup.get({})
    template = zapi.template.get({})
    for i,x in enumerate(group):
        print "Indice:",i, "-","ID:", x["groupid"], "-", x["name"]
    indicegroup = input("Escolha o indice do grupo desejado para o host %s: "%zabbixhost)
    askgroup = raw_input("O grupo %s foi selecionado. Confirma? (s ou n): "%group[indicegroup]["name"])
    if askgroup == 'n':
        print "grupo nao confirmado"
    elif askgroup == 's':
        for i,y in enumerate(template):
            print "Indice:",i,"-","Template ID :", y["templateid"],"-", y["host"]
        indicetemplate = input("Escolha o indice do template desejado para o host %s: "%zabbixhost)
        asktemplate = raw_input("O template %s foi selecionado. Confirma? (s ou n): "%template[indicetemplate]["host"])
        if asktemplate == 'n':
            print "Template nao confirmado"
        elif asktemplate == 's':
            print "Host: %s"%zabbixhost
            print "IP: %s"%zabbixhostip
            print "Grupo: %s"%group[indicegroup]["name"]
            print "Template: %s"%template[indicetemplate]["host"]
            confirmhost = raw_input("Confirma as informacoes e criar host %s? (s ou n): "%zabbixhost)
            if confirmhost == 'n':
                print "O host %s nao foi criado"%zabbixhost
            if confirmhost == 's':
                zapi.host.create({
                    "host": zabbixhost, 
                    "status":0,
                    "interfaces": [
                        {
                            "type": 1,
                            "main": 1,
                            "useip": 1,
                            "ip": zabbixhostip,
                            "dns": "",
                            "port": 10050
                        }
                    ],
                    "groups": [
                        {
                            "groupid": group[indicegroup]["groupid"]
                        }
                    ],
                    "templates": [
                        {
                            "templateid": template[indicetemplate]["templateid"]
                        }
                    ]
                }
            )
            print "O host %s foi criado"%zabbixhost
