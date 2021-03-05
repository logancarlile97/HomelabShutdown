import subprocess
from CSV_Functions import get_remote_info

#The run_ssh_command needs the get_ssh_command to function. 
#These are the reqirements for the get_ssh_command.
file_name = "./test.csv" 
row_number = 1
ssh_command, machine_name, ip, rmt_usr, sht_dwn_cmd = get_remote_info(file_name, row_number)

def run_ssh_command(ssh_command):
	
	#Opens a file to log the command ran.
	with open('ssh_command_log.txt', 'a') as f:
		#Make the Command to ping the connection
		ping_command = "ping -c 3 " + ip
		
		#Ping the network before trying to connect
		ping_process = subprocess.run(ping_command, shell=True, stdout = f, text = True)
		ping_code = ping_process.returncode
		
		#Check the returncode of ping_process to know if it found a connection.
		#If connection failed log it
		if ping_code != 0:
			f.write(f"The ping_process failed with a code of {ping_code} at {ip}.")
			print(f'Connection Failed at: {ip}')
	
		#If connection worked 
		else:
		
			#Calls a subprocess to run the command.
			ssh_process = subprocess.run(ssh_command, shell=True, stdout = f, text = True)
		
			#Logs the return code
			f.write(f"The return code is: {ssh_process.returncode}\n")
			
			#Return code of 0 means 0 errors
			print(str(ssh_process.returncode) + "\n")
	f.close()
	
	
	

#Example
run_ssh_command(ssh_command)
