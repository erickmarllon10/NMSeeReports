#coding: utf-8

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
 
canvas = canvas.Canvas("form.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 10)

canvas.drawString(30,750, 'Data de Revisão:')
canvas.drawString(110,750,"12/12/2010")
canvas.drawString(30,735,"Chamado OTRS:")
canvas.drawString(210,705, 'DADOS GERAIS DO SERVIDOR')
canvas.drawString(30,690, 'Nome: ')
canvas.drawString(62,690, 'Zabbix Agent')
canvas.drawString(30,675, 'IP:')
canvas.drawString(45,675, '10.10.10.10')
canvas.drawString(30,660, 'Sistema Operacional:')
canvas.drawString(130,660, 'Windows Server 2012 R2 Standard')
canvas.drawString(30,645, 'Ambiente:')
canvas.drawString(77,645, 'VMWare')
canvas.drawString(30,630, 'Localidade:')
canvas.drawString(83,630, 'SEDE')

canvas.drawString(213,600, 'Informações de Processamento')
canvas.drawString(30,570, 'Modelo(s) do(s) Processador(es):')
canvas.drawString(182,570, 'Intel Xeon CPU ES-2650 v2 @ 2.60GHz')
canvas.drawString(30,555, 'Quantidade de Processadores/Núcleos:')
canvas.drawString(210,555, '2 Socket(s) / 1 núcleo(s)')

canvas.drawString(206,525, 'Gráfico de Processamento Mensal')
canvas.save() 
