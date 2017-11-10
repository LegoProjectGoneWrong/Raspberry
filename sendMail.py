#!usr/bin/env python3

import smtplib
import socket
from datetime import datetime
toaddr = 'mikkel.svagard@gmail.com'

fromaddr = 'mikkel.raspberry@gmail.com'
password = 'RaspberryPi'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
yourIP = (s.getsockname()[0])
s.close()
text = "Current IP: " + str(yourIP)
print(text)

#create the message
msg = "\r\n".join([
  "Fom: " + fromaddr,
  "To: " + toaddr,
  "Subject: " + text,
  "",
  ""
  ])

#create a reciept of mail sent
f = open("mailReceipt.txt","w+")
time  = str(datetime.now())
log = time + "\n" + msg
f.write(log)
f.close()

#Send the mai through smtp
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(fromaddr,password)
server.sendmail(fromaddr, toaddr, msg)
server.quit()


print("message sent")
