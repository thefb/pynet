import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
## email client
server = smtplib.SMTP('smtp.gmail.com', 587)

server.connect("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
with open('C:\\Users\\fabs\\Documents\\Code\\Python\\Network\\pwd.txt', 'r') as file:
    pwd = file.read()

server.login('fabiano.siqueirab@gmail.com', pwd)

msg = MIMEMultipart()
msg['From'] = 'Fabiano Barbosa'
msg['To']  = 'penoji2912@ascaz.net'
msg['Subject'] = 'Just a test'

with open('textfile.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

#p = MIMEBase('application', 'octet-stream')

text = msg.as_string()
server.sendmail('fabiano.siqueirab@gmail.com', 'penoji2912@ascaz.net', text)