from authentification import userVerified
from CSV_Functions import get_row_count, get_remote_info
from SSH_Subprocess import run_ssh_command
import timeKeeper
from timeKeeper import dateToLog
import sys
import time

#Function to run program
def mainProgram():
    #Set the file name and row number
    file_name = './test.csv'
    log_file = './logs.txt'
    #Record a new entry and date to log
    dateToLog(log_file)

    #Start with the row after the header info. 
    row_number = 1

    #Determine the number of rows in the csv file. 
    row_count = get_row_count(file_name)

    #Loop through and run the ssh command for every row in the csv file. 
    while row_number < row_count:
        machine_name, ip,  rmt_user, sht_dwn_cmd = get_remote_info(file_name, row_number)
        run_ssh_command(machine_name, ip, rmt_user, sht_dwn_cmd)
        row_number += 1 


#Check for user verification
userAuthOverride = 'noAuth'
try:
    #Start timeKeeper
    timeKeeper.initialize()

    #See if the userAuthOverride argument is passed
    if (len(sys.argv) == 2):
        if (sys.argv[1] == 'noAuth'):
            print(f'Authentication Override Detected!')
            print('Proceeding with program in 5 seconds')
            time.sleep(5)
            mainProgram()
        else:
            print(f'Invalid Argument! User authentification override argument is {userAuthOverride}')
   
    #If an argument is passed and is not an userAuthOverride return an error and exit program
    elif (len(sys.argv) != 1):
        print(f'Invalid Arguments! User authentification override argument is {userAuthOverride}')
        print(f'This program takes one argument and you passed {len(sys.argv)-1}')
   
    #If no auth override override is passed then...
    else:
        #Make user input password to run the main program
        if (userVerified() == True):
            mainProgram()

except KeyboardInterrupt:
    print('User quit program')

except Exception as e:
    print(f'main.py had an error: {e}')
