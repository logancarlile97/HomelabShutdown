import subprocess
import timeKeeper
from timeKeeper import dateToLog, deltaStart, initialize
import CSV_Functions
from lcd_driver import lcdClear, lcdInit, lcdMessage
import sys
import time
from configReader import configReader

config = configReader('config.ini') #Get information from config file

def mainPowerOn():
    global config
    
    try:
        csv_file = config.getPowerOnConfig('powerOnCSVfile')
        log_file = 'logs.txt'

        lcdMessage('Homelab Power On', 'Proceeding...')

        with open(log_file, 'a') as log:
            row_number = 1 

            row_count = CSV_Functions.get_row_count(csv_file)

            #loop through each line of csv_file running each command
            while (row_number < row_count):
                #Get the power on info
                machine_name, ip_address, command = CSV_Functions.getPwrOnInfo(csv_file, row_number)

                #Ping the remote machine to see if its up
                print(f'Pinging {machine_name}')

                #Write to lcd what machine is being pinged
                lcdMessage('Pinging', machine_name)

                #Make the Command to ping the connection
                ping_command = "ping -c 3 " + ip_address
                
                #Ping the network before trying to connect and tell the console
                print(f'Pinging ip: {ip_address}')

                #Run the ping command and record output to log
                log.write(f'[{deltaStart()}]')
                log.write('Ping Output: \n')
                log.flush()
                ping_process = subprocess.run(ping_command, shell=True, stdout = log, text = True)
                log.write('\n')
                log.write(f'[{deltaStart()}]')
                log.write(f'End of Ping Output\n')
                
                #Record the return code as ping_code
                ping_code = ping_process.returncode
                
                #Check the returncode of ping_process to know if it can ping machine.
                #If ping failed
                if ping_code != 0:
                    
                    #Tell the console what is happening
                    print(f'Ping Failed.\n Running power on command to: {ip_address}\n')
                    lcdMessage('Ping Failed', f'{machine_name}')
                    lcdMessage('', 'Proceeding...')
                    lcdMessage('Turning on', machine_name)
                    #Calls a subprocess to run the ssh command and logs it
                    log.write(f'[{deltaStart()}] ')
                    log.write('Power On Command Output: \n')
                    log.flush()
                    pwrOnCmd = subprocess.run(command, shell=True, stdout = log, text = True)
                    log.write('\n')
                    log.write(f'[{deltaStart()}] ')
                    log.write(f'End of Power On Command Output\n')
                    lcdMessage('Finished', 'Proceeding...')	
                    #Logs the return code
                    log.write(f'[{deltaStart()}] ')
                    log.write(f"The return code is: {pwrOnCmd.returncode}\n")
                    log.flush()
                    
                    
                    
                #If ping worked 
                else:
                    
                    #Tell the console what is happening and log it.
                    print(f'Ping suceeded for: {ip_address}\n')
                    log.write(f'[{deltaStart()}] ')
                    log.write(f"The ping_process suceeded with a code of {ping_code}.\n")
                    lcdMessage(f'{machine_name}', 'Pingable')
                    lcdMessage('', 'Proceding...')
                    log.flush()
                #Set row_number to next row
                row_number += 1
        log.close()
    except Exception as e:
        with open(log_file, 'a') as log:
            
            log.write(f'mainPowerOn ran into an error')
            log.write(f'Exception: {e}')
        log.close()
        print(f'mainPowerOn ran into an error')
        print(f'Exception: {e}')

#For if user runs in standalone mode
stndAlne = config.getPowerOnConfig('standaloneArgument')

try:        
    if (len(sys.argv) == 2):	
        
        #Set the log file name
        log_file = './logs.txt'
        
        if (sys.argv[1] == stndAlne):
            #Start timeKeeper
            timeKeeper.initialize()

            #Record time and date program started to log
            dateToLog(log_file) 

            #Initilaize the lcd 
            lcdInit()
        
            #Clear the lcd
            lcdClear()
            
            lcdMessage('Homelab Power On', '')
            print(f'Standalone Mode Detected!')
            print('Proceeding with program in 5 seconds')
            time.sleep(5)
            mainPowerOn()
            lcdMessage('Program has', 'Concluded')
            time.sleep(3)
            lcdClear()
        else:
            print(f'Invalid argument, standalone command is: {stndAlne}')
    elif (len(sys.argv) != 1):
        print(f'To run powerOn in standalone mode use argument {stndAlne}') 

#If user exits
except KeyboardInterrupt:
    print(f'User exited program')