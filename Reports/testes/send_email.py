# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
# setup the parameters of the message
password = "741852963369258147"
msg['From'] = "relatorio.automatico.seepe@gmail.com"
msg['To'] = "erickmarllon10@gmail.com"
msg['Subject'] = "Relatorio de NMS"
 
# attach image to message body
msg.attach(MIMEImage(file("linux.jpeg").read()))
  
# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print "successfully sent email to %s:" % (msg['To'])
