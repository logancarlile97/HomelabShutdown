import csv
import sys
from logWriter import logWriter

#For Debug
#csv file to open
#csv_file_name = "./test.csv"

#row to gather values from
#row_number = 1

#Function to form an ssh command from specified row in *.csv file

log = logWriter() #Initialize log writter

def get_remote_info(csv_file, row_number):
	global log

	try:

		#Open the *.csv file and set csv_reader to the open file 
		log.write(f'Opening {csv_file}')

		with open(csv_file, mode = 'r') as file:
			
			log.write(f'Reading row {row_number}')

			csv_reader = csv.reader(file, delimiter=',')
			
			#Serarch csv_reader for specified row and set csv_list equal to it
			counter = 0
			for row in csv_reader:
				if counter == row_number:
					csv_list = row
					break
				else:
					counter+=1
			
		#Closes the file
		file.close()
			
		#Set each value in csv_list equal to a descriptive variable
		machine_name = csv_list[0].strip()
		ip = csv_list[1].strip()
		rmt_usr = csv_list[2].strip()
		sht_dwn_cmd = csv_list[3].strip()

		log.write(f'Machine_Name = {machine_name}')
		log.write(f'IP Address = {ip}')
		log.write(f'Remote User = {rmt_usr}')
		log.write(f'Shutdown Command = {sht_dwn_cmd}')

		return machine_name, ip, rmt_usr, sht_dwn_cmd
	
	except Exception as e:
		
		#Tell the console something went wrong. Give hint of issue to check
		print(f'Something went wrong while getting remote_info. Check your csv file: {str(e)}\n')
		
		log.write(f'Failed to retrieve remote_info. Check the csv file.')
		log.write(f'Exception: {str(e)}')
		
		sys.exit()

#Function to count the number of rows in *.csv file
def get_row_count(csv_file):
	global log
	
	try:

		#Open the *.csv file and set csv_reader to the open file
		with open(csv_file, mode = 'r') as file:
			csv_reader = csv.reader(file, delimiter=',')
			
			#Add one to a counter for every line
			row_number = 0
			for row in csv_reader:
				row_number+=1

		#Closes the file
		file.close()
		return row_number
	
	except Exception as e:

		#Tell the console something went wrong.
		print(f'Something went wrong while reading the CSV file: {str(e)} \n')
		
		log.write(f'Failed to count the rows.')
		log.write(f'Exception: {str(e)}')

		sys.exit()

#Function to retrive information for usage in power on
def getPwrOnInfo(csv_file, row_number):
	global log

	try:
			
		log.write(f'Opening {csv_file}')
		#Open the csv_file for reading
		with open(csv_file, mode = 'r') as file:
		
			#log row curently being read
			log.write(f'Reading row {row_number}')

			csv_reader = csv.reader(file, delimiter=',')
			
			#Serarch csv_reader for specified row and set csv_list equal to it
			counter = 0
			for row in csv_reader:
				if counter == row_number:
					csv_list = row
					break
				else:
					counter+=1
			
		#Closes the file
		file.close()
			
		#Set each value in csv_list equal to a descriptive variable
		machine_name = csv_list[0].strip()
		ip = csv_list[1].strip()
		pwrOnCmd = csv_list[2].strip()
		

		#Enter read values to log
		log.write(f'Machine_Name = {machine_name}')
		log.write(f'IP Address = {ip}')
		log.write(f'Power On Command = {pwrOnCmd}')

		return machine_name, ip, pwrOnCmd

	except Exception as e:
		print(f'getPwrOnInfo ran into an error')
		print(f'Exception: {e}')
			
		log.write(f'Failed to getPwrOnInfo.')
		log.write(f'Exception: {str(e)}')

		sys.exit()

#Debugging
#Sample of using get_row_count
#row_count = get_row_count(csv_file_name)
#print(row_count)

#Sample of using get_ssh_command
#machine_name, ip, rmt_usr, sht_dwn_cmd = get_remote_info('test.csv', 1)
#print(ssh_command) 

