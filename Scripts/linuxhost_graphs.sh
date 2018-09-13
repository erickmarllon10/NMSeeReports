#!/bin/bash

#################
### VARIABLES ###
#################

cpu_imagedir="/home/see/NMSeePlusv4.2_env/Images/cpu_utilization.png"
mem_imagedir="/home/see/NMSeePlusv4.2_env/Images/memory_usage.png"
#---------------------------------------------------------------#

echo "#############################################################################"
echo "# Periodo de coleta dos dados dos servidores. Ex: (01/07/2018 a 31/07/2018) #"
echo "#############################################################################"
echo "Digite o periodo inicial abaixo"
echo "dia (01..31):"
read DAY_FROM

echo "Mes (01..12):"
read MONTH_FROM

echo "Ano (2018):"
read YEAR_FROM

echo "Digite o periodo final abaixo"
echo "Dia (01..31):"
read DAY_TILL

echo "Mes (01..12):"
read MONTH_TILL

echo "Ano (2018):"
read YEAR_TILL

stime=$YEAR_FROM$MONTH_FROM$DAY_FROM'000000'

date_from_sec=$YEAR_FROM$MONTH_FROM$DAY_FROM'000000'
date_from="${date_from_sec:0:4}-${date_from_sec:4:2}-${date_from_sec:6:2}T${date_from_sec:8:2}:${date_from_sec:10:2}:${date_from_sec:12:2}"
epoch_from=$(date -d "$date_from" +%s)

date_till_sec=$YEAR_TILL$MONTH_TILL$DAY_TILL'235900'
date_till="${date_till_sec:0:4}-${date_till_sec:4:2}-${date_till_sec:6:2}T${date_till_sec:8:2}:${date_till_sec:10:2}:${date_till_sec:12:2}"
epoch_till=$(date -d "$date_till" +%s)

result=`expr $epoch_till - $epoch_from`

############################################################
#### Read the file and get the cpu utilization graph id ####
############################################################
for arq in `cat /home/see/NMSeePlusv4.2_env/TempGraphId/Linux/cpu_utilization.txt `; do
  cpu_graphid=$arq
done

############################################################
#### Read the file and get the mem utilization graph id ####
############################################################

for arq2 in `cat /home/see/NMSeePlusv4.2_env/TempGraphId/Linux/memory_usage.txt `; do
  mem_graphid=$arq2
done

#######################
# Save session cookie #
#######################
wget --save-cookies=/home/see/NMSeePlusv4.2_env/Cookie/zabbix.cookie -4 --keep-session-cookies -q -O "/dev/null" --post-data='name=Admin&password=zabbix&enter=Sign in&autologin=1&request=' 'http://192.168.1.0/zabbix/index.php?login=1' > /dev/null

####################################################################################################################################################
# Load saved cookie and search Utilizations'CPU graphs from Zabbix web with the month period specified. It is necessary adjusting images directory #
####################################################################################################################################################
wget -4 --load-cookies=/home/see/NMSeePlusv4.2_env/Cookie/zabbix.cookie -q -O $cpu_imagedir "http://192.168.1.0/zabbix/chart2.php?graphid=$cpu_graphid&period=$result&stime=$stime&isNow=0&profileIdx=web.graphs&profileIdx2=794&width=1462&sid=155b9d076cfee3f3&screenid" > /dev/null

####################################################################################################################################################
# Load saved cookie and search Available Memory graphs from Zabbix web with the month period specified. It is necessary adjusting images directory #
####################################################################################################################################################
wget -4 --load-cookies=/home/see/NMSeePlusv4.2_env/Cookie/zabbix.cookie -q -O $mem_imagedir "http://192.168.1.0/zabbix/chart2.php?graphid=$mem_graphid&period=$result&stime=$stime&isNow=0&profileIdx=web.graphs&profileIdx2=794&width=1462&sid=155b9d076cfee3f3&screenid" > /dev/null
