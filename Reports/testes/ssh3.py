from paramiko import SSHClient
import paramiko

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.10.10.5',username='root',password='123456')

stdin2,stdout2,stderr2 = ssh.exec_command("cat /proc/cpuinfo | grep name | sed -e 's/model name://g' | awk '{print $4,$5,$6,$7,$8,$9,$10}' | tail -n 1")
if stderr2.channel.recv_exit_status() != 0:
    print stderr2.read()
else:
    os_version = stdout2.read()
    print os_version
