import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address_book = ['jwoods@micro100.com', 'dharris@micro100.com','sbooth@micro100.comm']
msg = MIMEMultipart()    
sender = 'Alert@micro100.com'
subject = "Pi 80 Alarm"
body = "Pi 80 Alarm issue!!!"

msg['From'] = sender
msg['To'] = ','.join(address_book)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()
#print text
# Send the message via our SMTP server
s = smtplib.SMTP('10.103.1.17:25')
s.sendmail(sender,address_book, text)
s.quit() 
