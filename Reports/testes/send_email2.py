from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
import smtplib

#############################################

email_login = 'relatorio.automatico.seepe@gmail.com'
senha = '741852963369258147'

send_mail_to = 'erickmarllon10@gmail.com'

caminho_arquivo = '/home/see/Dropbox/Indra/Sprint 51/NMSeePlusv2.6/Reports/testes/zabbix_agent.pdf'

smtp_server = 'smtp.gmail.com'
smtp_server_port = '587'

#############################################

msg = MIMEMultipart()

msg_file = MIMEBase('application', 'pdf')

msg_file.set_payload(file(caminho_arquivo).read())

Encoders.encode_base64(msg_file)

msg_file.add_header('Content-Disposition', 'attachment', filename='zabbix_agent.pdf')

msg.attach(msg_file)

#############################################

mailer = smtplib.SMTP(smtp_server, smtp_server_port)
mailer.ehlo()
mailer.starttls()
mailer.login(email_login,senha)
mailer.sendmail(email_login, send_mail_to, msg.as_string())
mailer.close()
