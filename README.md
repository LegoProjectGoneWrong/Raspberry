#The following code will send a mail to whatever target with the device ip adress
#In order to allow this the following has to be added

sudo vim /etc/rc.local
#vim, nano, vi, text-editor

#add:
(sleep10;python /home/pi/Python/sendMail.py)&
exit 0
#sleep for waiting for it to establish connection
#& for running in background

#or:
sudo crontab -e
@reboot python /home/pi/Desktop/exemple.py &
