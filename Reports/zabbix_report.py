# -*- coding: utf-8 -*-

# This python code choose the host or active for generate the NMS report

import sys
from zabbix_api import ZabbixAPI
from template_windows import windowshost
from template_linux import linuxhost

def menu():
    print "Escolha o sistema operacional do servidor: \n \
            1 - Windows \n \
            2 - Linux \n \
            "
    options = input ("Digite a opção desejada: ")
    return options

def choose(x):
    try:
        dict_options = {1:windowshost,2:linuxhost}
        dict_options[x]()
    except Exception as err:
        print "erro %s"%err


def zabbixreport():
    print "Qual NMS deseja gerar o relatório? \n \
            1 - Número de manutenções preventivas em servidores \n \
            2 - Número de manutenções preventivas em ativos de rede\n \
            "
    ask = input("Escolha a NMS: ") 
    if ask == 1:
        choose(menu())
        sys.exit()
    elif ask == 2:
        print "NMS Não disponível para relatório"
    else:
        print "Opção Inválida"


