#!WARNING! 
#You must use log.flush() before any subprocesses that writes to the log.txt file,
#or it will not log properly


import subprocess
from CSV_Functions import get_remote_info
from datetime import datetime
import timeKeeper
import time
from timeKeeper import deltaStart

#The run_ssh_command needs the get_ssh_command to function. 
#These are the reqirements for the get_ssh_command.

#Debugging
#file_name = "./test.csv" 
#row_number = 1
#ssh_command, machine_name, ip, rmt_usr, sht_dwn_cmd = get_remote_info(file_name, row_number)

def run_ssh_command(machine_name, ip, rmt_usr, sht_dwn_cmd):
	
	#Take nessacery variables and parse them together into a single string forming ssh_command
	ssh_command = "ssh" + " " + rmt_usr + "@" + ip + " " + sht_dwn_cmd 
	
	#Opens a file to log to
	with open('logs.txt', 'a') as log:
		
		#Log the ssh command and machine_name
		print(f'Making ssh_command for {machine_name}\nssh_command = {ssh_command}')
		log.write(f'[{deltaStart()}] ')
		log.write(f'Made ssh_command for {machine_name}\n')
		log.write(f'[{deltaStart()}] ')
		log.write(f'ssh_command = {ssh_command}\n')
		
		#Make the Command to ping the connection
		ping_command = "ping -c 3 " + ip
		
		#Ping the network before trying to connect and tell the console
		print(f'Pinging ip: {ip}')

		#Run the ping command and record output to log
		log.write(f'[{deltaStart()}]')
		log.write('Ping Output: \n')
		log.flush()
		ping_process = subprocess.run(ping_command, shell=True, stdout = log, text = True)
		log.write('\n')
		log.write(f'[{deltaStart()}]')
		log.write(f'End of Ping Output\n')
		
		#Record the return code as ping_code
		ping_code = ping_process.returncode
		
		#Check the returncode of ping_process to know if it can ping machine.
		#If ping failed
		if ping_code != 0:
			
			#Tell the console what is happening and log it.
			print(f'Connection failed at: {ip}\nWith a code of {ping_code}')
			log.write(f'[{deltaStart()}]')
			log.write(f"The ping_process failed with a code of {ping_code}.")
	
		#If ping worked 
		else:
		
			#Tell the console what is happening
			print(f'Ping successful.\nSending ssh command to: {ip}\n')
			
			#Calls a subprocess to run the ssh command and logs it
			log.write(f'[{deltaStart()}]')
			log.write('SSH Output: \n')
			log.flush()
			ssh_process = subprocess.run(ssh_command, shell=True, stdout = log, text = True)
			log.write('\n')
			log.write(f'[{deltaStart()}]')
			log.write(f'End of SSH Output\n')
				
			#Logs the return code
			log.write(f'[{deltaStart()}]')
			log.write(f"The return code is: {ssh_process.returncode}\n")
			
			

			#Return code of 0 means 0 errors
			print('The process finished with a code of ' + str(ssh_process.returncode) + "\n")
	log.close()
	print(timeKeeper.start)
	
	

#Debugging
#run_ssh_command(machine_name, ip, rmt_usr, sht_dwn_cmd))
