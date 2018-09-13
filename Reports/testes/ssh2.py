from paramiko import SSHClient
import paramiko

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.10.10.5',username='root',password='123456')

stdin,stdout,stderr = ssh.exec_command("cat /etc/*release | grep DISTRIB_DESCRIPTION | sed -e 's/\"//g' | sed -e 's/DISTRIB_DESCRIPTION=//g'")
if stderr.channel.recv_exit_status() != 0:
    print stderr.read()
else:
    os_version = stdout.read()
    print os_version
