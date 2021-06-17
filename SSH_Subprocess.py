import subprocess
from CSV_Functions import get_remote_info
from lcd_driver import lcdMessage, lcdClear
from logWriter import logWriter

#The run_ssh_command needs the get_ssh_command to function. 
#These are the reqirements for the get_ssh_command.

#Debugging
#file_name = "./test.csv" 
#row_number = 1
#ssh_command, machine_name, ip, rmt_usr, sht_dwn_cmd = get_remote_info(file_name, row_number)


log = logWriter() #Initialize logs

def run_ssh_command(machine_name, ip, rmt_usr, sht_dwn_cmd):
	global log

	try:

		
		#Take nessacery variables and parse them together into a single string forming ssh_command
		ssh_command = "ssh" + " -t -t " + "-o BatchMode=yes" + " " + rmt_usr + "@" + ip + " '" + f" echo 'Conection to {machine_name} sucsessful'&& echo && {sht_dwn_cmd}" + "'" 
		lcdMessage('Pinging',f'{machine_name}')
		
		#Log the ssh command and machine_name
		print(f'Making ssh_command for {machine_name}\nssh_command = {ssh_command}')
		log.write(f'Made ssh_command for {machine_name}')
		log.write(f'ssh_command = {ssh_command}')
		
		#Make the Command to ping the connection
		ping_command = "ping -c 3 " + ip
		
		#Ping the network before trying to connect and tell the console
		print(f'Pinging ip: {ip}')

		#Run the ping command and record output to log
		log.write('Ping Output: ')
		
		ping_process = subprocess.run(ping_command, shell=True, capture_output=True, text = True)
		log.write(ping_process.stdout.decode('utf-8')) #Get output of ping command
		log.write(f'End of Ping Output')
		
		#Record the return code as ping_code
		ping_code = ping_process.returncode
		
		#Check the returncode of ping_process to know if it can ping machine.
		#If ping failed
		if ping_code != 0:
			
			#Tell the console what is happening and log it.
			print(f'Connection failed at: {ip} with a code of {ping_code}\n')
			log.write(f"The ping_process failed with a code of {ping_code}.")
			lcdMessage(f'{machine_name}', 'Not Pingable')
		#If ping worked 
		else:
		
			#Tell the console what is happening
			print(f'Ping successful.\nSending ssh command to: {ip}\n')
			lcdMessage('Pinged', f'{machine_name}')
			lcdMessage('', 'Proceeding...')
			lcdMessage('Shutting Down', f'{machine_name}')
			#Calls a subprocess to run the ssh command and logs it
			log.write('SSH Output: ')
			ssh_process = subprocess.run(ssh_command, shell=True, capture_output=True, text = True)
			log.write(ssh_process.stdout.decode('utf-8')) #Get output of ssh command
			log.write(f'End of SSH Output')
			lcdMessage('Finished', 'Proceeding...')	
			#Logs the return code
			log.write(f"The return code is: {ssh_process.returncode}")
			
			

			#Return code of 0 means 0 errors
			print('The remote process finished with a code of ' + str(ssh_process.returncode) + "\n")
	
	except Exception as e:

		#Tell the console something went wrong.
		print(f'Something went wrong while running the ssh command: {str(e)} \n')
			
		log.write(f'Failed to run ssh command.')
		log.write(f'Exception: {str(e)}')
	
	

#Debugging
#run_ssh_command(machine_name, ip, rmt_usr, sht_dwn_cmd))
