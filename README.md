The following code will send a mail to whatever target with the device ip adress
In order to allow a few lines have to be added

1.Navigate to the folder with sendMail.py

2.Edit toaddr in sendMail.py with your favorite editor to mail target

3. Find the absolute path  with pwd

>pwd

possible result: /home/robot/SendMailFolder/Raspberry

4. Open rc.local with your preferred text editor such as vim or nano

>sudo vim /etc/rc.local

5. add (sleep10;python *pwdpathtodirectory*/sendMail.py)& 
to the bottom of the file above exit 0

>(sleep 10; python3 /home/robot/SendMailFolder/Raspberry/sendMail.py)&

sleep for waiting for it to establish connection
& for running in background

6. Your pie should now send a mail to the target on boot
Check /var/log/syslog to find whatever went wrong
>vim /var/log/syslog
>Find "rc" by possbily using ctrl-f or ?rc

