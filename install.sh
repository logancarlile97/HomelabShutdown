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


#Change to the pi user until EOF is reached
sudo -i -u pi bash << EOF

#Clone the githup repo
git --branch installScript clone https://github.com/logancarlile97/HomelabShutdown.git

#Create a cron job to run program upon boot
touch /home/pi/HomelabShutdown/cronfile.tmp
/usr/bin/crontab -l > /home/pi/HomelabShutdown/cronfile.tmp
echo "@reboot sleep 5 && cd /home/pi/HomelabShutdown && python3 ./main.py" >> /home/pi/HomelabShutdown/cronfile.tmp
crontab /home/pi/HomelabShutdown/cronfile.tmp
rm /home/pi/HomelabShutdown/cronfile.tmp
EOF
