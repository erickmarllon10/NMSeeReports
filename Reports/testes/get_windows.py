from socket import *

ip = '192.168.1.13'
username = 'username'
password = 'password'

try:
    print "Establishing connection to %s" %ip
    connection = wmi.WMI(ip, user=username, password=password)
    print "Connection established"
except wmi.x_wmi:
    print "Your Username and Password of "+getfqdn(ip)+" are wrong."
