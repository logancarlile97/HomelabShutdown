# Homelab Shutdown/Power On
Program to shutdown and power on Homelab servers via ssh

This program is intended to be used on a Raspberry Pi as it takes use of its GPIO pins
## Initial Setup
Before the program may be run you must first intall required depencies. To install them run these commands:

* <code>sudo apt update </code>
* <code>sudo apt install python3</code>  
* <code>sudo apt install python3-pip</code>
* <code>sudo apt-get install rpi.gpio</code>
* <code>sudo pip3 install adafruit-circuitpython-charlcd</code>

## Running Automatically upon Boot
Create a cronjob. On the Rasperry Pi this is simple. 
<ul><li>As the PI user run this command in the terminal <code>crontab -e</code>. This will allow you to add a schedualed task.</li>
<li>Append this to the crontab file <code>@reboot sleep 5 && cd /{path_to_HomelabShutdown}/HomelabShutdown/ && python3 ./main.py</code>. This command will run the program upon reboot of the Raspberry Pi.</li>
</ul>


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

The default shutdown CSV file is <code>shutdown.csv</code> however this may be changed in <code>main.py</code>
  
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
