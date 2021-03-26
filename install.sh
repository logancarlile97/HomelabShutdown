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
#Create a file called cronfile.tmp
touch /home/pi/HomelabShutdown/cronfile.tmp
#Copy crontab contents to cronfile.tmp
/usr/bin/crontab -l > /home/pi/HomelabShutdown/cronfile.tmp
#Append the cron job to cronfile.tmp
echo "@reboot sleep 5 && cd /home/pi/HomelabShutdown && python3 ./main.py" >> /home/pi/HomelabShutdown/cronfile.tmp
#Write cronfile.tmp to the crontab
crontab /home/pi/HomelabShutdown/cronfile.tmp
#Delete the cronfile.tmp file
rm /home/pi/HomelabShutdown/cronfile.tmp
EOF
