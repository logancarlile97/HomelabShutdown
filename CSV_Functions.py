import csv

#csv file to open
csv_file_name = "D:/python_work/test.csv"

#row to gather values from
row_number = 1

#Function to form an ssh command from specified row in *.csv file
def get_ssh_command(csv_file, row_number):
	
	#Open the *.csv file and set csv_reader to the open file 
	with open(csv_file, mode = 'r') as file:
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
		
	#Take nessacery variables and parse them together into a single string forming ssh_command
	ssh_command = "ssh" + " " + rmt_usr + "@" + ip + " " + sht_dwn_cmd 
		
	return ssh_command, machine_name

#Function to count the number of rows in *.csv file
def get_row_count(csv_file):
	
	#Open the *.csv file and set csv_reader to the open file
	with open(csv_file, mode = 'r') as file:
		csv_reader = csv.reader(file, delimiter=',')
		
		#Add one to a counter for every line
		row_number = 0
		for row in csv_reader:
			row_number+=1
	return row_number
		
	#Closes the file
	file.close()

#Sample of using get_row_count
row_count = get_row_count(csv_file_name)
print(row_count)

#Sample of using get_ssh_command
ssh_command, machine_name = get_ssh_command(csv_file_name, row_number)
print(ssh_command) 

