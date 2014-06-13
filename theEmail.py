import smtplib
#import email modules
from email.mime.text import MIMEText
# Emails to use
addr_to   = 'jwoods@micro100.com'
addr_from = 'jdwoodsy1@gmail.com' 

#SMTP info
smtp_server = 'smtp.gmail.com:587'
smtp_user   ='jdwoodsy1@gmail.com'
smtp_pass   ='cooper2010'

msg = MIMEText('This is a test')
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Test Email from RPI'

s= smtplib.SMTP(smtp_server)
s.login(smtp_user, smtp_pass)
s.sendmail(addr_from, addr_to, msg.as_string())
s.quit()
