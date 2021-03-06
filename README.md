# Homelab Shutdown/Power On
Program to shutdown and power on Homelab servers via ssh

This program is intended to be used on a Raspberry Pi as it takes use of its GPIO pins

## Initial Setup
### Automatic Install
If you would like to skip the manual setup steps then copy and paste this command in the terminal:
* <code>curl https://raw.githubusercontent.com/logancarlile97/HomelabShutdown/main/install.sh | sudo bash</code>

It will install the program to the <code>/home/pi</code> directory. It will also install dependencies and a cron job to run the program automatically upon boot. If the install script runs properly you should see the LCD display <code>Shutdown: A</code> on line one, and <code>Power On: B</code> on line two after a few minutes.

### Manual Install
#### Dependencies

Before the program may be run you must first intall required depencies. To install them run these commands:

* <code>sudo apt update </code>
* <code>sudo apt install git</code>
* <code>sudo apt install python3</code>  
* <code>sudo apt install python3-pip</code>
* <code>sudo apt install rpi.gpio</code>
* <code>sudo pip3 install adafruit-circuitpython-charlcd</code>

#### Cloning program
To clone the git hub repository run this command:
* <code>git clone https://github.com/logancarlile97/HomelabShutdown.git</code>
#### Running Automatically upon Boot
Create a cron job. On the Rasperry Pi this is simple. 
<ul><li>As the PI user run this command in the terminal <code>crontab -e</code>. This will allow you to add a schedualed task.</li>
<li>Append this to the crontab file <code>@reboot sleep 5 && cd /{path_to_HomelabShutdown}/HomelabShutdown/ && python3 ./main.py</code>. This command will run the program upon reboot of the Raspberry Pi.</li>
</ul>

## Keypad Usage 

On most menus, the LCD will request a keypad input from you. Here are your options after you have typed your input:

<ul><li>Press the <code>#</code> key to enter your input</li>
	<li>Press the <code>*</code> Key to reset your input</li></ul>
	
On the main menu after boot up, when prompted whether to run the Shudown or Power on program you have an additional option:
	
<ul><li>Enter <code>D</code> to shutdown the PI.</li></ul>

On the Shutdown Program, when prompeted for the password, you have an additional option: 
	
<ul><li>Enter <code>DDD</code> to exit back to the main menu.</li></ul>

## Shutdown Features

### Shutdown CSV File Usage
This program uses entries on a CSV file to gather information needed for logging, remote conections, and to run remote commands.

Headers for the CSV file are:
<code>Machine_Name, IPAddress, RemoteUser, Shutdown Command</code>

Entries are required to be in this order or the program will not run properly

Putting Shutdown Commands in CSV file:
  <ul><li>Commands must use the full command path</li>
  <li>For example: <code>/bin/ls</code> rather than <code>ls</code></li>
  <li>You can find the path by running: <code>whereis {command}</code></li></ul>

The default shutdown CSV file is <code>shutdown.csv</code> however this may be changed in <code>mainShutdown.py</code>
  
### Logging
Most operations are recorded to the log in <code>logs.txt</code>

This log records the time and date the program was run

Additionally, the log will record how long from program start an entry was made

If your Shutdown Commands do not work the first place to look is in the log

### Connecting to a Remote Machine and Running the Shutdown Command
In order to connect to a remote machine and run a shutdown command you will need to perform these steps

<ul><li>Create a new user on the remote machine to connect to and run the shutdown command</li>
    <li>Make an SSH key pair for the machine this program is running on</li>
    <li>Copy your public SSH key to the remote machine user that you are connecting to</li>
    <li>On the remote machine give the remote user sudo privilages to run your shutdown command without a password</li></ul>

You must use SSH keys or the program will not be able to connect to the remote machine. You can create a new SSH Key by running this command on most linux distrobutions 
    <code>ssh-keygen -a 100 -t ed25519</code>

If you are unsure of how to do work with ssh keys then <a href = "https://www.youtube.com/watch?v=vINn1MIrf7o">this</a> is a good video.  

It is highly recommended that you create a new user who's only permision is to run your shutdown command

### Local Shutdown Commands

If you want to perform a shutdown command on the local machine just use the loopback address <code>127.0.0.1</code> in the IP address section of the csv file. An example of this can be found in the test.csv file.

If you want to actually shutdown or reboot the local machine make sure to add a delay of at least one minute before shutdown so that the program has time to close out. 

All local machine commands should be placed at the end of the csv file.

Just like a remote machine you need to place your public ssh key in the <code>authorized_keys</code> file of the local machine. 
### Changing the Shutdown Pin
When attempting to run a shutdown using the keypad, a pin will be required. By default the pin is <code>1234</code>.

To change this you will have to edit the <code>authentification.py</code> file.
* Look for a variable named <code>pin</code>
* The default entry for this line is <code>pin='1234'</code>
## PowerOn Features

### PowerOn CSV File Usage

This program uses entries on a CSV file to gather information needed for logging, pinging machines, and running power on commands. 

Headers for the CSV file are:
<code>Machine_Name, IPAddress, PowerOn Command</code>

Entries are required to be in this order or the program will not run properly

Putting PowerOn Commands in CSV file:
  <ul><li>Commands must use the full command path</li>
  <li>For example: <code>/bin/ls</code> rather than <code>ls</code></li>
  <li>You can find the path by running: <code>whereis {command}</code></li></ul>

The default PowerOn CSV file is <code>powerOn.csv</code> however this may be changed in <code>mainPowerOn.py</code>

### What happens when running PowerOn?
* PowerOn will retrive information from one row in the <code>powerOn.csv</code> file
* PowerOn will ping the Remote Machine's IP address, retrived from <code>powerOn.csv</code>
* If PowerOn is able to ping the IP it will move to the next row in <code>powerOn.csv</code>
* If PowerOn is not able to ping the IP it will run the power on command, retrived from the <code>powerOn.csv</code> then go to the next row
