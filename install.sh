#!/bin/bash

#Install Dependencies 
apt update -y
apt install git -y
apt install python3 -y
apt install python3-pip -y
apt install rpi.gpio -y
pip3 install adafruit-circuitpython-charlcd 

#Go to the pi users directory
cd /home/pi

#Clone the githup repo
git clone https://github.com/logancarlile97/HomelabShutdown.git

#Set up a cron job to auto start the program upon boot
#Change to the pi user
sudo -i -u pi bash << EOF
touch /home/pi/HomelabShutdown/cronfile.tmp
/usr/bin/crontab -l > /home/pi/HomelabShutdown/cronfile.tmp
echo "@reboot sleep 5 && cd /home/pi/HomelabShutdown && python3 ./main.py" >> /home/pi/HomelabShutdown/cronfile.tmp
crontab /home/pi/HomelabShutdown/cronfile.tmp
rm /home/pi/HomelabShutdown/cronfile.tmp
EOF
