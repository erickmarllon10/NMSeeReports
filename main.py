#coding: utf-8

from ManageHosts.create_zabbix_host import createhost
from ManageHosts.del_zabbix_host import delhost
from Reports.zabbix_report import zabbixreport
import sys

def logout():
    print "Logout realizado"
    sys.exit()

def menu():
    try:
        print "\n\
               \n\
               \n\
                  ####          ## ####          #### ############ \n\
                  ## ##         ## #####        ## ## ############ \n\
                  ##  ##        ## ##  ##      ##  ## ### \n\
                  ##   ##       ## ##   ##    ##   ## ### \n\
                  ##    ##      ## ##    ######    ## ############ \n\
                  ------SECRETARIA DE EDUCAÇÃO DE PERNAMBUCO------\n\
                  ##      ##    ## ##              ## ############ \n\
                  ##       ##   ## ##              ##         #### \n\
                  ##        ##  ## ##     v1.0     ##         #### \n\
                  ##         ## ## ##              ## ############ \n\
                  ##          #### ##              ## ############ \n\
                  \n\
                                    Menu principal \n\
                                            \n\
                            1 - Criar host no Zabbix\n\
                            2 - Excluir host no Zabbix\n\
                            3 - Gerar relatorio de NMS\n\
                            4 - Logout\n"
        option = input ("Digite a opção desejada: ")
        return option
    except Exception as err:
        print "Erro: %s"%err

def choose(x):
    try:
        dict_options = {1:createhost,2:delhost,3:zabbixreport,4:logout}
        dict_options[x]()
    except Exception as err:
        print "Opcão inválida %s"%err

while True:
    choose(menu())
