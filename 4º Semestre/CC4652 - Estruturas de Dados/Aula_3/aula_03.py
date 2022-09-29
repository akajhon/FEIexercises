from time import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import datetime

def Envio_Email(self):
    meu_email = 'joaopedrorosa03@gmail.com'
    minha_senha = '*Doentedeamor123!@#*'
    msg = MIMEMultipart()
    msg['FROM'] = 'joaopedrorosa03@gmail.com'
    msg['TO'] = meu_email
    data = datetime.datetime.now()
    msg['SUBJECT'] = f'Presença do dia {data.strftime("%d/%m/%y")} marcada! :D'
    body = MIMEText(f"""
    Presença do dia {data.strftime("%d/%m/%y")} marcada! :D
            
    Atenciosamente,

    Comite de Análise e Risco
    Centro Universitário FEI""")
    msg.attach(body)
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('joaopedrorosa03@gmail.com', minha_senha)
        smtp.send_message(msg)

if __name__ == '__main__':
    Envio_Email(self)