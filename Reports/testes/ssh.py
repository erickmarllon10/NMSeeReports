from paramiko import SSHClient
import paramiko

class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname='10.10.10.5',username='root',password='123456')

    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command("cat /etc/*release | grep DISTRIB_DESCRIPTION | sed -e 's/DISTRIB_DESCRIPTION=//g' | sed -e 's/\"//g'")
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            os_version = stdout.read()
            files = open('os_version', 'w')
            files.write(os_version)
            files.close()
            print os_version

if __name__ == '__main__':
    ssh = SSH()
    ssh.exec_cmd("apt-get update")
