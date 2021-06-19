from keypad import keypadMsge 
import time
from lcd_driver import lcdMessage, lcdClear
from configReader import configReader
from logWriter import logWriter

log = logWriter()

def userVerified():
    config = configReader('config.ini') #Get information from config file

    #Pin needed from user to authorize access
    pin = config.getAuthConfig('pin')
    maxAttempts = config.getAuthConfig('maxAttempts')
    lockoutTime = config.getAuthConfig('lockoutTime')
    exitAuth = config.getAuthConfig('exitAuthenticatorCode')
    attempt = 1

    #Tell user to input pin on keypad
    print('User Authentification Required!')
    print('Please input your pin on the keypad')

   

    while(True):    
        global log
        try:
            
            #record that authenticator is being used to log
            log.write(f'Authenticator Initialized: Asking user for pin')
            
            #Tell user to input password on lcd
            lcdMessage('', 'Input Password')
            
            #Get user inputed message
            code = keypadMsge()
            print(f'User inputed: {code}') #For debuging
            
            #Record user input to log
            log.write(f'User inputed: {code}')
            
            lcdMessage('', 'Analysing...')
            time.sleep(1)
            
            #If user enters the authenticator exit code then pass False to mainShutdown
            if (code == exitAuth):
                log.write(f'User entered {code} which is the exit code')
                log.write(f'Exiting program')
                
                return False

            #Check to see if code is equal to pin
            elif (code == pin):
                print('User verified')
                
                lcdMessage('', 'Password Valid')
                lcdMessage('', 'Proceeding...')
                #log the a user was verified
                log.write(f'User was verified proceeding with program')
                
                return True

            #See if user made maximum attempts
            elif (attempt == maxAttempts):
                
                print(f'Max attempts made, try again in {lockoutTime} seconds')
                
                lcdMessage('', f'{maxAttempts} Attempts Made')
                lcdMessage('', f'{lockoutTime} sec Timeout')
                #Log that user was locked out
                log.write(f'User used max number of attempts\n')
                log.write(f'User being locked out for {lockoutTime} seconds')
                #Wait for lockoutTime to expire
                time.sleep(lockoutTime)
                attempt = 1
                print(f'Try again')

            else:
                print('Incorrect pin: User not verified')
                print('Try Again')

                lcdMessage('', f'X Attempt {attempt} of {maxAttempts}')
                #Log that a user inputed the wrong pin
                log.write(f'User inputed the wrong pin, attempts are at {attempt} of {maxAttempts}')

                attempt += 1
        
        except Exception as e:

		    #Tell the console something went wrong.
            print(f'Something went wrong while running the authenticator: {str(e)} \n')
                
            log.write(f'Authenticator Failed.')
            log.write(f'Exception: {str(e)}')

            break