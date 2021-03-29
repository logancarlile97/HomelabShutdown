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
  git clone --branch powerIndicator+ShutdownButton https://github.com/logancarlile97/HomelabShutdown.git


EOF

#Ask user if they want to create an autostart job for the program to start after boot
echo 
read -p 'Create a job to run program at boot? (y/n): ' crnJb <&1
echo
case $crnJb in

#Create a cron job to run program upon boot
y|Y )
	sudo -i -u pi bash << EOF
	touch /home/pi/HomelabShutdown/cronfile.tmp
	/usr/bin/crontab -l > /home/pi/HomelabShutdown/cronfile.tmp
	echo "@reboot sleep 5 && cd /home/pi/HomelabShutdown && python3 ./main.py" >> /home/pi/HomelabShutdown/cronfile.tmp
	crontab /home/pi/HomelabShutdown/cronfile.tmp
	rm /home/pi/HomelabShutdown/cronfile.tmp
	
EOF
;;

* ) echo "Skipped installing cron job" ;; 
esac

#Ask user if they are using a shutdown button
echo
read -p 'Are you using a power button on GPIO 24 (Pin 18)? (y/n): ' shtBtn <&1
echo
case $shtBtn in
#Create a cron job to run shutdown-button.py upon boot
y|Y )
        sudo -i -u pi bash << EOF
        touch /home/pi/HomelabShutdown/cronfile.tmp
	/usr/bin/crontab -l > /home/pi/HomelabShutdown/cronfile.tmp
	echo "@reboot cd /home/pi/HomelabShutdown && python3 ./shutdown-button.py" >> /home/pi/HomelabShutdown/cronfile.tmp
	/usr/bin/crontab /home/pi/HomelabShutdown/cronfile.tmp
	rm /home/pi/HomelabShutdown/cronfile.tmp
EOF
  ;;
* ) echo 'User said not using shutdown button';;
esac

#Ask user if they are using a power indicator
echo
read -p 'Are you using a power indicator led connected to GPIO 14 (Pin 8)? (y/n): ' pwrIndctr <&1
echo
case $pwrIndctr in
y|Y ) echo 'enable_uart=1' >> /boot/config.txt ;;
* ) echo 'User said not using a power indicator led'
esac

#Ask user to reboot the pi to make the program run
echo 
echo "Reboot needed to finish install"
read -p 'Reboot now? (y/n): ' rbtNw <&1
echo

case $rbtNw in 
  y|Y ) echo "Rebooting in 10sec press Ctrl-c to cancel" && sleep 10 && reboot;;
  
  * ) echo "Please reboot manualy later";;
esac
