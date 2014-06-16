import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address_book = ['xxxx@xxx.com', 'xxxx@xxx.com','xxxx@xxx.com']
msg = MIMEMultipart()    
sender = 'xxxx@xxx.com'
subject = "Pi 80 Alarm"
body = "Pi 80 Alarm issue!!!"

msg['From'] = sender
msg['To'] = ','.join(address_book)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()
#print text
# Send the message via our SMTP server
s = smtplib.SMTP('xxxxxxxxxx')
s.sendmail(sender,address_book, text)
s.quit() 
