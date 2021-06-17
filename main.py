from keypad import keypadMsge 
from lcd_driver import lcdInit, lcdMessage, lcdClear
import timeKeeper
from timeKeeper import dateToLog, deltaStart
from mainShutdown import mainShutdown, shutdownRan
from mainPowerOn import mainPowerOn
import subprocess

#Initilize the lcd 
lcdInit()
prgrmSelected = False
loop = True

#Code for user to shutdown program from main menu
shtDwnCode = 'D'
shtDwnCmd = 'sudo /usr/sbin/shutdown +1'
log_file = "./logs.txt"

try:
    with open('logs.txt', 'a') as log:
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
                
                #Start timeKeeper
                timeKeeper.initialize()
                
                #Record time and date program started to log
                dateToLog(log_file) 
                
                #Log that user selected shutdown
                log.write(f'[{deltaStart()}] ')
                log.write(f'User Selected Shutdown\n')   
                log.flush()

                #Loop until user inputs a valid input
                while(validInput == False):
                    lcdMessage('Selected','Shutdown')
                    lcdMessage('Continue: C', 'Back: D')
                    usrInpt = keypadMsge()
                    
                    #Check if user continues, if true run mainShutdown
                    if(usrInpt == 'C'):
                        validInput = True
                        
                        #Log user continued
                        log.write(f'[{deltaStart()}] ')
                        log.write(f'User continued with Shutdown\n')   
                        log.flush()

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
                        
                        #Log user went back
                        log.write(f'[{deltaStart()}] ')
                        log.write(f'User went back to main menu\n')   
                        log.flush()

                        #User entered valid input
                        validInput = True
                        
                        lcdMessage(' ', 'Exiting...')
                        print('User Exited')
                    else:
                        lcdMessage('Invalid Input', ' ')


            #If user enters B
            elif(usrInpt == 'B'):
                print(f'Selected Power On')
                
                #Start timeKeeper
                timeKeeper.initialize()
                
                #Record time and date program started to log
                dateToLog(log_file) 
                
                while(validInput == False):
                    lcdMessage('Selected','Power On')
                    lcdMessage('Continue: C', 'Back: D')
                    
                    #Log that user selected power on
                    log.write(f'[{deltaStart()}] ')
                    log.write(f'User selected Power On\n')   
                    log.flush()
                    
                    usrInpt = keypadMsge()
                    
                    #Check if user continues
                    if(usrInpt == 'C'):
                        validInput = True
                        
                        #Log that user continued with power on
                        log.write(f'[{deltaStart()}] ')
                        log.write(f'User continued with Power On\n')   
                        log.flush()
                        
                        mainPowerOn()
                        #Reenter the main menu loop after running power on
                        loop = True
                        lcdMessage(' ', 'Continuing...')
                        print('User Continued')
                    
                    #Check if user goes back
                    elif(usrInpt == 'D'):
                        validInput = True
                        
                        #Log that user went back to main menu
                        log.write(f'[{deltaStart()}] ')
                        log.write(f'User went back to main menu\n')   
                        log.flush()
                        
                        lcdMessage(' ', 'Exiting...')
                        print('User Exited')
                    else:
                        lcdMessage('Invalid Input', ' ')
           
            #If user enters the shutdown code
            elif (usrInpt == shtDwnCode):
                
                #Start timeKeeper
                timeKeeper.initialize()

                #Record time and date program started to log
                dateToLog(log_file)
                
                log.write(f'[{deltaStart()}] ')
                log.write(f'User entered {usrInpt} which is the program shutdown code, asking for confirmation\n')
                log.flush()
                #loop until valid user input
                while(validInput == False):
                    lcdMessage('Selected','Program Shutdown')
                    lcdMessage('Continue: C', 'Back: D')
                    usrInpt = keypadMsge()
                    
                    #Check if user continues
                    if(usrInpt == 'C'):
                        validInput = True
                        
                        #Log that user continued with program shutdown
                        log.write(f'[{deltaStart()}] ')
                        log.write(f'User continued with program shutdown\n')   
                        log.flush()

                        #Exit the main menu loop 
                        loop = False
                        lcdMessage(' ', 'Continuing...')
                        print('User Continued')

                        subprocess.run(shtDwnCmd, shell = True, stdout = log, text = True)

                    #Check if user goes back
                    elif(usrInpt == 'D'):
                        validInput = True
                        
                        #Log that user went back to main menu
                        log.write(f'[{deltaStart()}] ')
                        log.write(f'User went back to main menu\n')   
                        log.flush()
                        
                        lcdMessage(' ', 'Exiting...')
                        print('User Exited')
                    
                    else:
                        lcdMessage('Invalid Input', ' ')

            else:
                lcdClear()
                lcdMessage('Invalid Input',' ')

    #Close log
    log.close()
#if user exits program
except KeyboardInterrupt:
    print('User exited program')
    lcdClear()  
    

#if program runs into a problem
except Exception as e:
    print(f'main.py ran into a problem')
    print(f'Exception: {e}')

#Clear lcd when program finishes
lcdClear()

