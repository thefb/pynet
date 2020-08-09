import os


# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
with open('textfile') as fp:
    # Create a text/pain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the receiver's email address

msg['Subject'] = f'The contents of Lore Ipsum'
msg['From'] = 'fabiano.siqueirab@gmail.com'
msg['To'] = 'fabiano.sqb@gmail.com'

# Send the message via our own SMTP server;

s = smtplib.SMTP('smtp.gmail.com', '587')

with open('C:\\Users\\fabs\\Documents\\Code\\Python\\Network\\pwd.txt', 'r') as file:
    pwd = file.read() 

s.login('fabiano.siqueirab@gmail.com', pwd)
s.send_message(msg)
s.quit()
