import subprocess
from CSV_Functions import get_ssh_command

#The run_ssh_command needs the get_ssh_command to function. 
#These are the reqirements for the get_ssh_command.
file_name = "" 
row_number = 1
ssh_command = get_ssh_command(file_name, row_number)

def run_ssh_command(ssh_command):
	
	#Opens a file to log the command ran.
	with open('ssh_command_log.txt', 'a') as f:
		
		#Calls a subprocess to run the command.
		ssh_process = subprocess.run(ssh_command, shell=True, stdout = f, text = True)
	f.close()

#Example
run_ssh_command(ssh_command)
