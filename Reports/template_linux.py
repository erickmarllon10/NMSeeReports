#coding: utf-8

# This python code import zabbix-api bib for connect in zabbix 3.4 API from zabbix-server docker host 10.10.10.3 and generate customs reports

##################
#      Bibs      #
##################
import sys
import os
from datetime import datetime,date
from zabbix_api import ZabbixAPI
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
import smtplib

#################################################################
# Declaration of credentials variables and values of Zabbix Web #
#################################################################
ZABBIX_SERVER='http://10.81.244.56/zabbix'
ZUSER='Admin'
ZPASS='zabbix'

###################################################################
# Conection with Zabbix API from zabbix web variables declaration #
###################################################################
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login(ZUSER, ZPASS)

######################################################################################
# declaring API objects for using on the items, interfaces, hosts and graphs searchs #
######################################################################################
hosts = zapi.host.get({})
hostg = zapi.hostgroup.get({})
item = zapi.item.get({})
interfaces = zapi.hostinterface.get ({})
graph_name = zapi.graph.get({})

def apifunctions():

    #############################################################################################################
    # This code match the variable 'name' and get the id, name and description of host identified by servername #
    #############################################################################################################

    for hg in hostg:
        if hg["name"] == "Linux servers":
            group_id = hg["groupid"]

    hosts = zapi.host.get({"groupids":group_id})
    zabbix_hosts = []
    for h in hosts:
        zabbix_hosts.append(h["name"])

    global servername
    servername = raw_input("Digite o nome do host: ")
    while servername not in zabbix_hosts:
        servername = raw_input("%s não encontrado ou não faz parte do grupo 'Linux servers'. Digite o nome do servidor corretamente: "%servername)
    for h in hosts:
        if servername in h["name"]:
            print "Coletando informações. Este processo pode demorar alguns instantes. Favor aguardar..."
            global host_id
            host_id = h["hostid"]
            global host_name
            host_name = h["name"]
            global host_description
            host_description = h["description"]
            global so
            so = host_description.split("SO: ")[1]
            global host_desc
            host_desc = host_description.split("Ambiente: ")[0]
            global chassis
            chassis = host_description.split("Ambiente: ")[1]
            chassis = chassis[0:10]
            break

    #################################################################
    # This code get the ip address of host identified by servername #
    #################################################################
    for i in interfaces:
        if host_id == i["hostid"]:
            global host_ip
            host_ip = i["ip"]

    ###############################################################################################################
    # All scripts bellow are used to calculate the memory utilization in percent in host identified by servername #
    ###############################################################################################################
    # API and python commands to get Total memory.
    item_totalmem = 'Total memory'
    for i in item:
        if host_id == i["hostid"] and item_totalmem == i["name"]:
            kb_totalmem = i["lastvalue"]
            kb_totalmem_int = float(kb_totalmem)
            gb_totalmem = kb_totalmem_int / 1024.0 / 1024.0 / 1024.0
            global total_mem
            total_mem = round(gb_totalmem)

    # API and python Commands to get available memory. Available memory is defined as free, cache and buffers memory
    item_freemem = 'Available memory'
    for i in item:
        if host_id == i["hostid"] and item_freemem == i["name"]:
            kb_freemem = i["lastvalue"]
            kb_freemem_int = float(kb_freemem)
            gb_freemem = kb_freemem_int / 1024.0 / 1024.0 / 1024.0
            global total_freemem
            total_freemem = round(gb_freemem)

    # Calc Memory utilization in percent
    try:
        total_mem_used = float(total_mem) - float(total_freemem)
        total_mem_calc = float(total_mem) / 100.0
        global total_mem_utilization
        total_mem_utilization = total_mem_used / total_mem_calc
        total_mem_utilization = str(total_mem_utilization)+"%"
    except ZeroDivisionError:
        total_mem_utilization = "Não coletado"

    total_mem = str(total_mem)+" GB"
    total_freemem = str(total_freemem)+" GB"

    #############################################################################################################################
    # API and python Commands to get uptime itemid and print in days, hours and minutes format in host identified by servername #
    #############################################################################################################################
    item_uptime = 'System uptime'
    for i in item:
        if host_id == i["hostid"] and item_uptime == i["name"]:
            uptime_sec = i["lastvalue"]
            uptime_hour = int(uptime_sec) // 3600
            uptime_day = int(uptime_hour) // 86400
            uptime_sec_rest = int(uptime_sec) % 3600
            uptime_min = int(uptime_sec_rest) // 60

            if uptime_hour >= 24:
                uptime_day = int(uptime_hour / 24)
                uptime_hour = int(uptime_hour % 24)

            global total_uptime
            total_uptime = str(uptime_day)+" Dia(s), "+str(uptime_hour)+" Hora(s) e "+str(uptime_min)+" minuto(s)"

    ###########################################################################################
    # API and python Commands to get total processes actives in host identified by servername #
    ###########################################################################################
    item_procs = 'Number of running processes'
    for i in item:
        if host_id == i["hostid"] and item_procs == i["name"]:
            global active_procs
            active_procs = i["lastvalue"]

    ########################################################################################
    # API and python Commands to get total root partition in host identified by servername #
    ########################################################################################
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
            break
        else:
            part_name = ""
            totall_root = ""

    ##########################################################################################
    # API and python Commands to get of free root partition in host identified by servername #
    ##########################################################################################
    item_freeroot = "vfs.fs.size[/,free]"
    for i in item:
        if host_id == i["hostid"] and item_freeroot == i["key_"]:
            disc_root_free = i["lastvalue"]
            disc_root_free_int = int(disc_root_free)
            disc_root_freegb = disc_root_free_int / 1024.0 / 1024.0 / 1024.0
            global total_root_free
            total_root_free = round(disc_root_freegb)
            total_root_free = str(total_root_free)+" GB"
            break
        else:
            total_root_free = ""

    ###########################################################################################################
    # All CPU scripts bellow are used to calculate the total cpu utilization in host identified by servername #
    ###########################################################################################################
    # Get CPU Idle Time
    item_cputime = "system.cpu.util[,idle]"
    for i in item:
        if host_id == i["hostid"] and item_cputime == i["key_"]:
            cpu_idle = i["lastvalue"]
            cpu_idle_time = float(cpu_idle)

    # Calc cpu utilization
    global cpu_utilization
    cpu_utilization = 100.0 - cpu_idle_time
    cpu_utilization = round(cpu_utilization,2)
    cpu_utilization = str(cpu_utilization)+"%"

    #############################################################################
    # API and python commands to get cpu model in host identified by servername #
    #############################################################################
    item_cpumodel = "CPU Model"
    for i in item:
        if host_id == i["hostid"] and item_cpumodel == i["name"]:
            cpu = i['lastvalue']
            cpu_slice = cpu.split("\n")[0]
            global cpu_model
            cpu_model = cpu_slice[13: ]

    #####################################################################################
    # API and python commands to get Total Logical CPU in host identified by servername #
    #####################################################################################
    item_cpucount = "CPU Count"
    for i in item:
        if host_id == i["hostid"] and item_cpucount == i["name"]:
            global cpu_logical
            cpu_logical = i['lastvalue']

    ##############################################################################################################################
    # API and python commands to get and save to file the graphid of CPU utilization graph name in host identified by servername #
    ##############################################################################################################################
    for g in graph_name:
        if g['name'] == 'CPU utilization':
            search_id = g['graphid']

        graph = zapi.graph.get({
            "hostids" : [
                host_id
            ],
            "graphids": [
                search_id
            ],
        "history": 0,
        "output": "extend",
        })
        if g in graph:
            graph_id = g['graphid']
            filename = 'TempGraphId/Linux/cpu_utilization.txt'
            with open(filename, 'w') as file_object:
                file_object.write(graph_id)
                
    ###########################################################################################################################
    # API and python commands to get and save to file the graphid of Memory usage graph name in host identified by servername #
    ###########################################################################################################################
    for g in graph_name:
        if g['name'] == 'Memory usage':
            search_id = g['graphid']

            graph = zapi.graph.get({

            "hostids" : [
                host_id
            ],
            "graphids": [
                search_id
            ],
            "history": 0,
            "output": "extend",
            })
            if g in graph:
                graph_id = g['graphid']
                filename = 'TempGraphId/Linux/memory_usage.txt'
                with open(filename, 'w') as file_object:
                    file_object.write(graph_id)


#########################################
# Functions not related to APIs objects #
#########################################

##########################################################################################################################
# This shell script is responsible to get and save the images graphs above based on data source and end, calculate stime # 
# and seconds interval between then, generate zabbix web cookie file and read the graphid located in filename variable   #                                                  
##########################################################################################################################
def monthperiod():
    os.system("Scripts/linuxhost_graphs.sh")

############################################################
# OTRS is a helpdesk system and this number is got earlier #
############################################################
def otrsnum():
    global otrs
    otrs = raw_input("Digite o número do OTRS: ")

#########################################################
# Manual user informations to supplement the pdf report #
#########################################################
def otherinfo():
    ask = raw_input("Deseja incluir outras informações? (s ou n): ")
    if ask == 's':
        global pendinfo
        pendinfo = raw_input("Atualizações pendentes? (sim ou não): ")
        global pendreboot
        pendreboot = raw_input("Reboot pendente? (sim ou não): ")
        contask = raw_input("Deseja incluir outras observações? (s ou n): ")
        if contask == 's':
            global obs
            obs = raw_input("Digite: ")
        elif contask == 'n':
            print "Sem observações"
            obs = "Sem informações"
        else:
            print "Opção inválida"
    elif ask == 'n':
        pendinfo = "Não informado"
        pendreboot = "Não informado"
        contask2 = raw_input("Deseja incluir outras observações? (s ou n): ")
        if contask2 == 's':
            obs = raw_input("Digite: ")
        elif contask2 == 'n':
            obs = "Sem observações"
    else:
        print "Opção inválida"

##################################################################################################################
# Reportlab bib for pdf report, generate report's name by reading servername variable and save it to filepdf dir #
##################################################################################################################
def pdfcanvas():
    global filepdf
    filepdf = "/home/see/NMSeePlusv4.2_env/PdfReports/"+servername+" - Manutencao Preventiva de Servidores.pdf"
    global canvas
    canvas = canvas.Canvas(filepdf, pagesize=letter)

##################################################################################################################################
# Generate PDF report based on all API itens, interfaces, hosts, graphs and previous informations identified by global variables #
##################################################################################################################################
def pdf_report():
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 8)

    cpu_graph = Image.open("Images/cpu_utilization.png")
    memory_graph = Image.open("Images/memory_usage.png")

    canvas.drawString(30,750, 'Data de Revisão:')
    canvas.drawString(95,750, datetime.now().strftime("%d/%m/%Y"))
    canvas.drawString(263,750,"Chamado OTRS:")
    canvas.drawString(325,750, otrs)

    canvas.drawString(255,720, 'Dados Gerais do Servidor')
    canvas.drawString(30,695, 'Nome: ')
    canvas.drawString(55,695, host_name)
    canvas.drawString(115,695, 'IP:')
    canvas.drawString(127,695, host_ip)
    canvas.drawString(257,695, 'SO:')
    canvas.drawString(274,695, so)
    canvas.drawString(490,695, 'Ambiente:')
    canvas.drawString(528,695, chassis)
    canvas.drawString(30,685, 'Serviço:')
    canvas.drawString(62,685, host_desc)

    canvas.drawString(245,655, 'Informações de Processamento')
    canvas.drawString(30,640, 'Modelo(s) do(s) Processador(es):')
    canvas.drawString(150,640, cpu_model)
    canvas.drawString(30,630, 'Quantidade de Processadores Lógicos:')
    canvas.drawString(173,630, cpu_logical)

    canvas.drawString(240,595, 'Gráfico de Processamento Mensal')
    canvas.drawInlineImage(cpu_graph, 50, 460, width=500, height=130)
    canvas.drawString(30,450, 'Consumo atual:')
    canvas.drawString(88,450, cpu_utilization)

    canvas.drawString(240,420, 'Gráfico de uso da memória mensal')
    canvas.drawInlineImage(memory_graph, 50, 285, width=500, height=130)
    canvas.drawString(30,270, 'Consumo atual:')
    canvas.drawString(88,270, total_mem_utilization)

    canvas.drawString(255,235, 'Informações de memória')
    canvas.drawString(30,210, 'Memória Total:')
    canvas.drawString(85,210, total_mem)
    canvas.drawString(30,200, 'Memória disponível:')
    canvas.drawString(103,200, total_freemem)

    canvas.drawString(260,175, 'Informações de Disco')
    canvas.drawString(30,150, 'Partições')
    canvas.drawString(40,140, part_name)
    canvas.drawString(88,150, 'Total')
    canvas.drawString(86,140, total_root)
    canvas.drawString(136,150, 'Livre')
    canvas.drawString(133,140, total_root_free)

    canvas.drawString(264,120, 'Outras informações')
    canvas.drawString(30,95, 'Uptime:')
    canvas.drawString(60,95, total_uptime)
    canvas.drawString(30,85, 'Atualizações pendentes:')
    canvas.drawString(120,85, pendinfo)
    canvas.drawString(245,95, 'Reboot pendente:')
    canvas.drawString(311,95, pendreboot)
    canvas.drawString(427,95, 'Processos ativos:')
    canvas.drawString(491,95, active_procs)

    canvas.drawString(276,65, 'Observações')
    canvas.drawString(30,50, obs)

    canvas.save()

################################
# Send the pdf report by email #
################################
def sendemail():
    email_login = 'relatorio.automatico.seepe@gmail.com'
    senha = '741852963369258147'
    send_mail_to = 'erickmarllon10@gmail.com'
    caminho_arquivo = filepdf
    smtp_server = 'smtp.gmail.com'
    smtp_server_port = '587'

    #############################################

    msg = MIMEMultipart()
    msg_file = MIMEBase('application', 'pdf')
    msg_file.set_payload(file(caminho_arquivo).read())
    Encoders.encode_base64(msg_file)
    msg_file.add_header('Content-Disposition', 'attachment', filename=servername+" - Manutenção Preventiva de Servidores.pdf")
    msg.attach(msg_file)

    #############################################

    mailer = smtplib.SMTP(smtp_server, smtp_server_port)
    mailer.ehlo()
    mailer.starttls()
    mailer.login(email_login,senha)
    mailer.sendmail(email_login, send_mail_to, msg.as_string())
    mailer.close()

    print "Email enviado com sucesso"

#################
# Main function #
#################
def linuxhost():
    while True:
        apifunctions()
        monthperiod()
        otrsnum()
        if len(otrs):
            otherinfo()
            pdfcanvas()
            pdf_report()
#            sendemail()
            print "Relatório gerado com sucesso"
            break
