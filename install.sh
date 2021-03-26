#!/bin/bash
#Install Dependencies 
apt update -y
apt install python3 -y
apt install python3-pip -y
apt install rpi.gpio -y
pip3 install adafruit-circuitpython-charlcd 

#Set up the Cron tab job
sudo -i -u pi bash << EOF
touch /home/pi/HomelabShutdown/cronfile.txt
/usr/bin/crontab -l > /home/pi/HomelabShutdown/cronfile.txt
echo "@reboot sleep 5 && cd /home/pi/HomelabShutdown && python3 ./main.py" >> /home/pi/HomelabShutdown/cronfile.txt
crontab /home/pi/HomelabShutdown/cronfile.txt
rm /home/pi/HomelabShutdown/cronfile.txt
EOF
