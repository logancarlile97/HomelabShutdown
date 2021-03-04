import csv
csv_file_name = "D:/python_work/test.csv"
row_number = 1

def get_ssh_command(csv_file, row_number):
	with open(csv_file, mode = 'r') as file:
		csv_reader = csv.reader(file, delimiter=',')
		counter = 0
		for row in csv_reader:
			if counter == row_number:
				csv_list = row
				break
			else:
				counter+=1
				
		machine_name = csv_list[0].strip()
		ip = csv_list[1].strip()
		rmt_usr = csv_list[2].strip()
		sht_dwn_cmd = csv_list[3].strip()
		
		ssh_command = "ssh" + " " + rmt_usr + "@" + ip + " " + sht_dwn_cmd 
		return ssh_command, machine_name

		
ssh_command, machine_name = get_ssh_command(csv_file_name, row_number)
print(ssh_command) 

