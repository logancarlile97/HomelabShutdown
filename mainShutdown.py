from authentification import userVerified
from CSV_Functions import get_row_count, get_remote_info
from SSH_Subprocess import run_ssh_command
import sys
import time
from lcd_driver import lcdInit, lcdMessage, lcdClear
from configReader import configReader
from logWriter import logWriter

config = configReader('config.ini') #Get information from config file
log = logWriter() #Initialize logWriter

#Function to run program
def runShutdown(file_name):

    #Start with the row after the header info. 
    row_number = 1

    #Determine the number of rows in the csv file. 
    row_count = get_row_count(file_name)

    #Loop through and run the ssh command for every row in the csv file. 
    while (row_number < row_count):
        machine_name, ip,  rmt_user, sht_dwn_cmd = get_remote_info(file_name, row_number)
        run_ssh_command(machine_name, ip, rmt_user, sht_dwn_cmd)
        row_number += 1 


#Check for user verification
def mainShutdown(): 
    global config
    global prgrmRan
    prgrmRan = False

    try:
        #Clear the lcd
        lcdClear()
        
        lcdMessage('Homelab Shutdown', '')

        #Set the file name and log file
        file_name = config.getShutdownConfig('shutdownCSVfile')
           
        #Make user input password to run the main program
        if (userVerified() == True):
            runShutdown(file_name)
            prgrmRan = True

        lcdMessage('Program has', 'Concluded')
        time.sleep(3)
        lcdClear()

    except Exception as e:
        print(f'mainShutdown.py had an error: {e}')
        lcdClear()

#This function will allow main to see if user ended up running up program or not
def shutdownRan():
    return prgrmRan


try:    
    if (__name__ == "__main__"):

        file_name = config.getShutdownConfig('shutdownCSVfile')

        log.newEntry() #Log a new entry
        lcdInit() #Initilaize the lcd
        lcdClear() #Clear the lcd
        lcdMessage('Homelab Shutdown', '')
        print(f'Authentication Override Detected!')
        print('Proceeding with program in 5 seconds')
        time.sleep(5)
        runShutdown(file_name)
        lcdMessage('Program has', 'Concluded')
        time.sleep(3)
        lcdClear()

except KeyboardInterrupt:
    print('User quit program')
    time.sleep(1)
    lcdClear()

except Exception as e:
    print(f"An exception occured: {e}")