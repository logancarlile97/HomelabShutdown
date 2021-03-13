from authentification import userVerified
from CSV_Functions import get_row_count, get_remote_info
from SSH_Subprocess import run_ssh_command
import timeKeeper
from timeKeeper import dateToLog
import sys
import time
from lcd_driver import lcdInit, lcdMessage, lcdClear

#Function to run program
def runShutdown(file_name, log_file):

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
def mainShutdown(): 
    global prgrmRan
    prgrmRan = False
    userAuthOverride = 'noAuth'
    try:
        #Clear the lcd
        lcdClear()
        
        lcdMessage('Homelab Shutdown', '')

        #Set the file name and log file
        file_name = './test.csv'
        log_file = './logs.txt'
           
        #Make user input password to run the main program
        if (userVerified() == True):
            runShutdown(file_name, log_file)
            prgrmRan = True

        lcdMessage('Program has', 'Concluded')
        time.sleep(3)
        lcdClear()
    except KeyboardInterrupt:
        print('User quit program')
        lcdClear()

    except Exception as e:
        print(f'mainShutdown.py had an error: {e}')
        lcdClear()

#This function will allow main to see if user ended up running up program or not
def shutdownRan():
    return prgrmRan



userAuthOverride = 'noAuth'
#See if the userAuthOverride argument is passed
# if this is passed then it will overrride all authentification 
# it will also record a new date as this is ment to be run on its own
# This will only run if a user expicitly runs this program and passes the override argument
if (len(sys.argv) == 2):
    #Initilaize the lcd 
    lcdInit()
    
    #Clear the lcd
    lcdClear()

    lcdMessage('Homelab Shutdown', '')

    #Set the file name and log file
    file_name = './test.csv'
    log_file = './logs.txt'
    
    if (sys.argv[1] == userAuthOverride):
        #Start timeKeeper
        timeKeeper.initialize()

        #Record time and date program started to log
        dateToLog(log_file) 

        
        print(f'Authentication Override Detected!')
        print('Proceeding with program in 5 seconds')
        time.sleep(5)
        runShutdown(file_name, log_file)
    else:
        print(f'Invalid Argument! User authentification override argument is {userAuthOverride}')

#If an argument is passed and is not an userAuthOverride return an error and exit program
elif (len(sys.argv) != 1):
    print(f'Invalid Arguments! User authentification override argument is {userAuthOverride}')
    print(f'This program takes one argument and you passed {len(sys.argv)-1}')
