from CSV_Functions import get_row_count, get_remote_info
from SSH_Subprocess import run_ssh_command
from datetime import datetime
import timeKeeper
from timeKeeper import end_timer

#Start timeKeeper
timeKeeper.initialize()

file_name = './test.csv'
row_number = 1

machine_name, ip,  rmt_user, sht_dwn_cmd = get_remote_info(file_name, row_number)
run_ssh_command(machine_name, ip, rmt_user, sht_dwn_cmd)


#example of ending timer
#end = timeKeeper.end_timer()
#print(end - timeKeeper.start)
