import smtplib
import socket
fromaddr = 'mikkel.raspberry@gmail.com'
toaddr = 'mikkel.svagard@gmail.com'
username = fromaddr
password = 'RaspberryPi'


text = socket.gethostbyname(socket.gethostname())
print text

msg = "\r\n".join([
  "Fom: " + fromaddr,
  "To: " + toaddr,
  "Subject: Just a test",
  "",
  text
  ])


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, msg)
server.quit()
print "message sent"
