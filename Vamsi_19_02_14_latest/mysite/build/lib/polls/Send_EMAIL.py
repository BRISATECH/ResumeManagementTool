import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    print "header----",header
    message = header + message
    print "message = ",message
    

    if cc_addr_list:
        to_addr_list1 = to_addr_list + cc_addr_list
    else:
        to_addr_list1 = to_addr_list
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list1, message)
    server.quit()

##k=sendemail('kamadi.srikanth@gmail.com',['kamadi.srikanth@gmail.com'],['xavshrid@gmail.com'],'hi','bye','kamadi.srikanth@gmail.com','1168srichi')
##print k
##def send_mail(send_from, send_to, subject, text, files=[], server="localhost"):
##  assert type(send_to)==list
##  assert type(files)==list
##
##  msg = MIMEMultipart()
##  msg['From'] = send_from
##  msg['To'] = COMMASPACE.join(send_to)
##  msg['Date'] = formatdate(localtime=True)
##  msg['Subject'] = subject
##
##  msg.attach( MIMEText(text) )
##
##  for f in files:
##    part = MIMEBase('application', "octet-stream")
##    part.set_payload( open(file,"rb").read() )
##    Encoders.encode_base64(part)
##    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
##    msg.attach(part)
##
##  smtp = smtplib.SMTP(server)
##  smtp.sendmail(send_from, send_to, msg.as_string())
##  smtp.close()
##
##
##
##send_mail('kamadi.srikanth@gmail.com','kamadi.srikanth@gmail.com','hi','
