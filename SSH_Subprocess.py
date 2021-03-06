import subprocess
from CSV_Functions import get_remote_info
from datetime import datetime
import timer


#The run_ssh_command needs the get_ssh_command to function. 
#These are the reqirements for the get_ssh_command.

#Debugging
#file_name = "./test.csv" 
#row_number = 1
#ssh_command, machine_name, ip, rmt_usr, sht_dwn_cmd = get_remote_info(file_name, row_number)

def run_ssh_command(machine_name, ip, rmt_usr, sht_dwn_cmd):
	
	#Take nessacery variables and parse them together into a single string forming ssh_command
	ssh_command = "ssh" + " " + rmt_usr + "@" + ip + " " + sht_dwn_cmd 
	
	#Opens a file to log the command ran.
	with open('logs.txt', 'a') as f:
		#Log the command and machine_name
		print(f'Making ssh_command as {machine_name}\nssh_command = {ssh_command}')
		f.write(f'Made ssh_command as {machine_name}\nssh_command = {ssh_command}')
		
		#Make the Command to ping the connection
		ping_command = "ping -c 3 " + ip
		
		#Ping the network before trying to connect and tell the console
		print(f'Pinging ip: {ip}')
		ping_process = subprocess.run(ping_command, shell=True, stdout = f, text = True)
		ping_code = ping_process.returncode
		
		#Check the returncode of ping_process to know if it found a connection.
		#If connection failed
		if ping_code != 0:
			
			#Tell the console what is happening and log it.
			print(f'Connection failed at: {ip}\nWith a code of {ping_code}')
			f.write(f"The ping_process failed with a code of {ping_code}.")
	
		#If connection worked 
		else:
		
			#Tell the console what is happening
			print(f'Connection successful.\nSending ssh command to: {ip}')
			
			#Calls a subprocess to run the command.
			ssh_process = subprocess.run(ssh_command, shell=True, stdout = f, text = True)
		
			#Logs the return code
			f.write(f"The return code is: {ssh_process.returncode}\n")
			
			#Return code of 0 means 0 errors
			print('The process finished with a code of ' + str(ssh_process.returncode) + "\n")
	f.close()
	print(timer.start)
	
	

#Debugging
#run_ssh_command(machine_name, ip, rmt_usr, sht_dwn_cmd))
