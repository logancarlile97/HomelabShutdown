from keypad import keypadMsge 
import time
from timeKeeper import deltaStart

def userVerified():
    #Pin needed from user to authorize access
    pin = '1234'
    loop = True
    attempt = 1
    maxAttempts = 3
    timeOut = 1
    lockoutTime = 5
    
    #Tell user to input pin on keypad
    print('User Authentification Required!')
    print('Please input your pin on the keypad')

    while(loop):    
        try:
            
            #open the log
            with open('logs.txt', 'a') as log:
                #Get user inputed message
                code = keypadMsge()
                print(f'User inputed: {code}') #For debuging
                
                #Record user input to log
                log.write(deltaStart())
                log.write(f'User inputed: {code}\n')
                time.sleep(1)
                
                #If keyboard.py detects user quit program quit this program
                if (code == 'UserExit'):
                    loop = False
                    
                    #If a user attempts to exit program Return False 
                    return False
                
                #Check to see if code is equal to pin
                elif (code == pin):
                    print('User verified')
                    
                    #log the a user was verified
                    log.write(deltaStart())
                    log.write(f'User was verified proceeding with program\n')
                    
                    loop = False
                    return True
            
                #See if user made maximum attempts
                elif (attempt == maxAttempts):
                    
                    #Increase lockoutTime each time user makes make attempts
                    lockoutTime = timeOut * 5
                    print(f'Max attempts made, try again in {lockoutTime} seconds')

                    #Log that user was locked out
                    log.write(deltaStart())
                    log.write(f'User was locked out for {lockoutTime} seconds\n')
                    
                    #Wait for lockoutTime to expire
                    time.sleep(lockoutTime)
                    timeOut += 1
                    attempt = 1
                    print(f'Try again')

                else:
                    print('Incorrect pin: User not verified')
                    print('Try Again')
                   
                    #Log that a user inputed the wrong pin
                    log.write(deltaStart())
                    log.write(f'User inputed the wrong pin, attempts are at {attempt} of {maxAttempts}\n')

                    attempt += 1
            
            #Close the log
            log.close()
        except KeyboardInterrupt:
            print('User closed program')
            loop = False
            log.close()
        except Exception as e:

		#Tell the console something went wrong.
		print(f'Something went wrong while running the authenticator: {str(e)} \n')

		#Log the fail
		with open('logs.txt', 'a') as log:
			
			log.write(f'[{deltaStart()}]')
			log.write(f'Authenticator Failed.\n')
			log.write(f'[{deltaStart()}]')
			log.write(f'Exception: {str(e)}\n')
		
		#Close log
		log.close()
#print(userVerified()) #Debugging