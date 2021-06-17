from keypad import keypadMsge 
from lcd_driver import lcdInit, lcdMessage, lcdClear
from mainShutdown import mainShutdown, shutdownRan
from mainPowerOn import mainPowerOn
import subprocess
from logWriter import logWriter

#Initilize the lcd 
lcdInit()
prgrmSelected = False
loop = True

#Code for user to shutdown program from main menu
shtDwnCode = 'D'
shtDwnCmd = 'sudo /usr/sbin/shutdown +1'

log = logWriter() #Initialize logWriter

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
            
            log.newEntry() #Log a new entry
            
            log.write(f'User Selected Shutdown') #Log that user selected shutdown   

            while(validInput == False): #Loop until user inputs a valid input
                lcdMessage('Selected','Shutdown')
                lcdMessage('Continue: C', 'Back: D')
                usrInpt = keypadMsge()
                
                if(usrInpt == 'C'): #Check if user continues, if true run mainShutdown
                    validInput = True
                    
                    log.write(f'User continued with Shutdown') #Log user continued  

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
                    
                    log.write(f'User went back to main menu') #Log user went back  

                    #User entered valid input
                    validInput = True
                    
                    lcdMessage(' ', 'Exiting...')
                    print('User Exited')
                else:
                    lcdMessage('Invalid Input', ' ')


        #If user enters B
        elif(usrInpt == 'B'):
            print(f'Selected Power On')
            
            log.newEntry() #Log a new entry
            
            while(validInput == False):
                lcdMessage('Selected','Power On')
                lcdMessage('Continue: C', 'Back: D')
                
                log.write(f'User selected Power On') #Log that user selected power on  
                
                usrInpt = keypadMsge()
                
                #Check if user continues
                if(usrInpt == 'C'):
                    validInput = True
                    
                    log.write(f'User continued with Power On') #Log that user continued with power on  
                    
                    mainPowerOn()
                    #Reenter the main menu loop after running power on
                    loop = True
                    lcdMessage(' ', 'Continuing...')
                    print('User Continued')
                
                #Check if user goes back
                elif(usrInpt == 'D'):
                    validInput = True
                    
                    log.write(f'User went back to main menu') #Log that user went back to main menu 

                    lcdMessage(' ', 'Exiting...')
                    print('User Exited')
                else:
                    lcdMessage('Invalid Input', ' ')
        
        elif (usrInpt == shtDwnCode): #If user enters the shutdown code
            
            log.newEntry() #Log a new entry
            
            log.write(f'User entered {usrInpt} which is the program shutdown code, asking for confirmation')
               
            while(validInput == False): #loop until valid user input
                lcdMessage('Selected','Program Shutdown')
                lcdMessage('Continue: C', 'Back: D')
                usrInpt = keypadMsge()
                
                
                if(usrInpt == 'C'): #Check if user continues
                    validInput = True
                    
                    
                    log.write(f'User continued with program shutdown') #Log that user continued with program shutdown   

                    #Exit the main menu loop 
                    loop = False
                    lcdMessage(' ', 'Continuing...')
                    print('User Continued')

                    proc = subprocess.run(shtDwnCmd, shell = True, text = True, capture_output=True)
                    log.write(proc.stdout.decode("utf-8"))
                
                #Check if user goes back
                elif(usrInpt == 'D'):
                    validInput = True
                    
                    log.write(f'User went back to main menu') #Log that user went back to main menu  
                    
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
    lcdClear()  
    

#if program runs into a problem
except Exception as e:
    print(f'main.py ran into a problem')
    print(f'Exception: {e}')

#Clear lcd when program finishes
lcdClear()

