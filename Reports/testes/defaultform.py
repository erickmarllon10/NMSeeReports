from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

servername = "linuxteste2"
filepdf = "/home/see/Indra/NMSeePlusv4.2/PdfReports/"+servername+" - Manutencao Preventiva de Servidores.pdf"
print filepdf
canvas = canvas.Canvas(filepdf, pagesize=letter)

def pdf():
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)
 
    canvas.drawString(30,750,'COMUNICADO OFICIAL')
    canvas.drawString(30,735,'EMPRESAS ACME')
    canvas.drawString(500,750,"12/12/2011")
    canvas.line(480,747,580,747)
 
    canvas.drawString(275,725,'SALDO DEVEDOR:')
    canvas.drawString(500,725,"R$ 1.000,00")
    canvas.line(378,723,580,723)
 
    canvas.drawString(30,703,'RECEBIDO POR:')
    canvas.line(130,700,580,700)
    canvas.drawString(130,703,"JOHN DOE")
 
    canvas.save()
