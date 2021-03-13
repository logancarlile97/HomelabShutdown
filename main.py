from keypad import keypadMsge 
import time
from lcd_driver import lcdInit, lcdMessage, lcdClear
import timeKeeper
from timeKeeper import dateToLog
from mainShutdown import mainShutdown, shutdownRan
#Initilize the lcd 
lcdInit()
prgrmSelected = False
loop = True

log_file = "./logs.txt"
#Start timeKeeper
timeKeeper.initialize()

#Record time and date program started to log
dateToLog(log_file) 

try:
    #Loop through main menu 
    # if the shutdown program runs sucessfully this loop will end
    # otherwise the loop will continue indefinatly
    while(loop):
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
                
                #Check if user continues, if true run mainShutdown
                if(usrInpt == 'C'):
                    validInput = True

                    lcdMessage(' ', 'Continuing...')
                    print('User Continued')

                    mainShutdown()
                    
                    #Check to see if shutdown ended up runing 
                    # if not then repeat then reenter loop
                    if (shutdownRan() == False):
                        loop = True
                    else:
                        loop = False

                #If user enters D then reenter loop    
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
                
                #Check if user continues
                if(usrInpt == 'C'):
                    validInput = True
                    
                    #Reenter the main menu loop after running power on
                    loop = True
                    lcdMessage(' ', 'Continuing...')
                    print('User Continued')
                
                #Check if user goes back
                elif(usrInpt == 'D'):
                    validInput = True
                    lcdMessage(' ', 'Exiting...')
                    print('User Exited')
                else:
                    lcdMessage('Invalid Input', ' ')

        else:
            lcdClear()
            lcdMessage('Invalid Input',' ')

#if user exits program
except KeyboardInterrupt:
    print('User exited program')

#if program runs into a problem
except Exception as e:
    print(f'main.py ran into a problem')
    print(f'Exception: {e}')
lcdClear()