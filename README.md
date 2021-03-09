# HomelabShutdown
Program to shutdown Homelab servers via ssh

This program is intended to be used on a Raspberry Pi as it takes use of its GPIO pins

# CSV Usage
Headers for the CSV file are:
<code>Machine_Name, IPAddress, RemoteUser, Shutdown Command</code>

Entries are required to be in this order or the program will not run properly

Putting Shutdown Commands in CSV file:
  <ul><li>Commands must use the full command path</li>
  <li>For example: <code>/bin/ls</code> rather than <code>ls</code></li>
  <li>You can find the path by running: <code>whereis {command}</code></li></ul>

The default CSV file is <code>test.csv</code> however this may be changed in <code>main.py</code>
  
# Logging
Most operations are recorded to the log in <code>logs.txt</code>

This log records the time and date the program was run

Additionally, the log will record how long from program start an entry was made

If your Shutdown Commands do not work the first place to look is in the log

# Connecting to a Remote Machine and Running the Shutdown Command
In order to connect to a remote machine and run a shutdown command you will need to perform these steps

<ul><li>Create a new user on the remote machine to connect to and run the shutdown command</li>
    <li>Make an SSH key pair for the machine this program is running on</li>
    <li>Copy your public SSH key to the remote machine user that you are connecting to</li>
    <li>One the remote machine give the remote user sudo privilages to run your shutdown command without a password</li></ul>

You must use SSH keys or the program will not be able to connect to the remote machine. You can create a new SSH Key by running this command on most linux distrobutions 
    <code>ssh-keygen -a 100 -t ed25519</code>

It is highly recommended that you create a new user who's only permision is to run your shutdown command
