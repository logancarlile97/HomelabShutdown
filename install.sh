#!/bin/bash

#Install Dependencies 
apt update -y
apt install git -y
apt install python3 -y
apt install python3-pip -y
apt install rpi.gpio -y
pip3 install adafruit-circuitpython-charlcd 

#Update packages on pi
apt upgrade -y

#Go to the pi users directory
cd /home/pi


#Change to the pi user until EOF is reached
sudo -i -u pi bash << EOF

#Clone the githup repo
git clone https://github.com/logancarlile97/HomelabShutdown.git

#Ask user if they want to create an autostart job for the program to start after boot
echo 
read -p 'Create a job to run program at boot? (y/n): ' crnJb <&1
echo

case $crnJb in
  #Create a cron job to run program upon boot
  y|Y )
  touch /home/pi/HomelabShutdown/cronfile.tmp
  /usr/bin/crontab -l > /home/pi/HomelabShutdown/cronfile.tmp
  echo "@reboot sleep 5 && cd /home/pi/HomelabShutdown && python3 ./main.py" >> /home/pi/HomelabShutdown/cronfile.tmp
  crontab /home/pi/HomelabShutdown/cronfile.tmp
  rm /home/pi/HomelabShutdown/cronfile.tmp
  ;;
  
  * ) echo "Skipped installing cron job" ;; 
EOF

#Delay to give user time to see previous message
sleep 5

#Ask user to reboot the pi to make the program run
echo 
echo "Reboot needed to finish install"
read -p 'Reboot now? (y/n): ' rbtNw <&1
echo

case $rbtNw in 
  y|Y ) echo "Rebooting in 10sec press Ctrl-c to cancel" && sleep 10 && reboot;;
  
  * ) echo "Please reboot manualy later";;
esac
