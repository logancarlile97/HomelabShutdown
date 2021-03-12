from keypad import keypadMsge 
import time
from lcd_driver import lcdInit, lcdMessage, lcdClear
import timeKeeper
from timeKeeper import dateToLog
from mainShutdown import mainShutdown, shutdownRan
#Initilize the lcd 
lcdInit()
prgrmSelected = False

log_file = "./logs.txt"
#Start timeKeeper
timeKeeper.initialize()

#Record time and date program started to log
dateToLog(log_file) 

while(prgrmSelected == False):
    validInput = False
    
    lcdMessage('Shutdown: A', 'Power On: B')
    usrInpt = keypadMsge()
    
    #If user enters A
    if(usrInpt == 'A'):
        print(f'Selected Shutdown')
        while(validInput == False):
            lcdMessage('Selected','Shutdown')
            lcdMessage('Continue: C', 'Back: D')
            usrInpt = keypadMsge()
            
            #Check if user continues or goes back
            if(usrInpt == 'C'):
                validInput = True
                prgmSelected = True
                lcdMessage(' ', 'Continuing...')
                print('User Continued')
                mainShutdown()
                print(shutdownRan())
                #Check to see if shutdown ended up runing 
                # if not then repeat the prgrmSelected loop
                if (shutdownRan() == False):
                    prgrmSelected = False
            print(prgrmSelected)
            elif(usrInpt == 'D'):
                validInput = True
                lcdMessage(' ', 'Exiting...')
                print('User Exited')
            else:
                lcdMessage('Invalid Input', ' ')


    #If user enters B
    elif(usrInpt == 'B'):
        print(f'Selected Power On')
        while(validInput == False):
            lcdMessage('Selected','Power On')
            lcdMessage('Continue: C', 'Back: D')
            usrInpt = keypadMsge()
            
            #Check if user continues or goes back
            if(usrInpt == 'C'):
                validInput = True
                prgmSelected = True
                lcdMessage(' ', 'Continuing...')
                print('User Continued')
            elif(usrInpt == 'D'):
                validInput = True
                lcdMessage(' ', 'Exiting...')
                print('User Exited')
            else:
                lcdMessage('Invalid Input', ' ')

    else:
        lcdClear()
        lcdMessage('Invalid Input',' ')

lcdClear()