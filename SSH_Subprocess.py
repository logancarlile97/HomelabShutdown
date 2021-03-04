import subprocess
from CSV_Functions import get_ssh_command

#The run_ssh_command needs the get_ssh_command to function. 
#These are the reqirements for the get_ssh_command.
file_name = "./test.csv" 
row_number = 1
ssh_command = get_ssh_command(file_name, row_number)

def run_ssh_command(ssh_command):
	
	#Opens a file to log the command ran.
	with open('ssh_command_log.txt', 'a') as f:
		
		#Calls a subprocess to run the command.
		ssh_process = subprocess.run(ssh_command, shell=True, stdout = f, text = True)
		
		#Logs the return code
		f.write(f"The return code is: {ssh_process.returncode}")
	f.close()
	
	#Return code of 0 means 0 errors
	print(ssh_process.returncode)

#Example
run_ssh_command(ssh_command)
