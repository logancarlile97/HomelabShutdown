from CSV_Functions import get_row_count, get_remote_info
from SSH_Subprocess import run_ssh_command
from datetime import datetime
import timeKeeper


#Start timeKeeper
timeKeeper.initialize()

#Set the file name and row number
file_name = './test.csv'

#Start with the row after the header info. 
row_number = 1

#Determine the number of rows in the csv file. 
row_count = get_row_count(file_name)

#Loop through and run the ssh command for every row in the csv file. 
while row_number < row_count:
    machine_name, ip,  rmt_user, sht_dwn_cmd = get_remote_info(file_name, row_number)
    run_ssh_command(machine_name, ip, rmt_user, sht_dwn_cmd)
    row_number += 1 

