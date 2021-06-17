import subprocess
import CSV_Functions
from lcd_driver import lcdClear, lcdInit, lcdMessage
import sys
import time
from configReader import configReader
from logWriter import logWriter

config = configReader('config.ini') #Get information from config file
log = logWriter() #Initialize logWriter

def mainPowerOn():
    #Global declarations
    global config
    global log

    try:
        csv_file = config.getPowerOnConfig('powerOnCSVfile')
        log_file = 'logs.txt'

        lcdMessage('Homelab Power On', 'Proceeding...')

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
            log.write('Ping Output: ')
            ping_process = subprocess.run(ping_command, shell=True, capture_output=True, text = True)
            log.write(ping_process.stdout.decode('utf-8')) #Get output of ping command
            log.write(f'End of Ping Output')
            
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
                log.write('Power On Command Output: ')
                pwrOnCmd = subprocess.run(command, shell=True, capture_output=True, text = True)
                log.write(pwrOnCmd.stdout.decode('utf-8')) #Get output of power on command
                log.write(f'End of Power On Command Output')
                lcdMessage('Finished', 'Proceeding...')	
                log.write(f"The return code is: {pwrOnCmd.returncode}") #Logs the return code

                
                
                
            #If ping worked 
            else:
                
                #Tell the console what is happening and log it.
                print(f'Ping suceeded for: {ip_address}\n')
                log.write(f"The ping_process suceeded with a code of {ping_code}.")
                lcdMessage(f'{machine_name}', 'Pingable')
                lcdMessage('', 'Proceding...')
            #Set row_number to next row
            row_number += 1

    except Exception as e:  
        log.write(f'mainPowerOn ran into an error') #Log that an error occured
        log.write(f'Exception: {e}') #Log error
        print(f'mainPowerOn ran into an error')
        print(f'Exception: {e}')

#For if user runs in standalone mode
stndAlne = config.getPowerOnConfig('standaloneArgument')

try:        
    if (len(sys.argv) == 2):	
        
        if (sys.argv[1] == stndAlne):
            log.newEntry() #Log that a new entry is being made
            lcdInit() #Initilaize the lcd 
            lcdClear() #Clear the lcd
            
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