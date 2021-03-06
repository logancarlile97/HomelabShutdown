from CSV_Functions import get_row_count, get_remote_info
from SSH_Subprocess import run_ssh_command
from datetime import datetime
import timer
from timer import end_timer

#Start a timer
timer.initialize()

file_name = './test.csv'
row_number = 1

machine_name, ip,  rmt_user, sht_dwn_cmd = get_remote_info(file_name, row_number)
run_ssh_command(machine_name, ip, rmt_user, sht_dwn_cmd)


#example of ending timer
#end = timer.end_timer()
#print(end - timer.start)
