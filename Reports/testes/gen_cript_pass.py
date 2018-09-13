import bcrypt

senha = 'zabbix'
salt = bcrypt.gensalt(8)

print salt

hash = bcrypt.hashpw(senha, salt)
print hash
