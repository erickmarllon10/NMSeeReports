import time

# show date in timestamp format
data_atual = time.time()
data = '30/07/2018 09:00:00'
print "Tempo atual em timestamp e: ", data_atual

# Convert timestamp date in a legible format
print time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(data_atual))

# Convert a legible date to timestamp format
print time.mktime(time.strptime('30/07/2018 10:30:00', '%d/%m/%Y %H:%M:%S'))
