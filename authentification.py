from keypad import keypadMsge 
import time

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
            #Get user inputed message
            code = keypadMsge()
            print(f'User inputed: {code}') #For debuging

            time.sleep(1)
            
            #If keyboard.py detects user quit program quit this program
            if (code == 'UserExit'):
                loop = False
            
            #Check to see if code is equal to pin
            elif (code == pin):
                print('User verified')
                loop = False
                return True
        
            #See if user made maximum attempts
            elif (attempt == maxAttempts):
                
                #Increase lockoutTime each time user makes make attempts
                lockoutTime = timeOut * 5
                print(f'Max attempts made, try again in {lockoutTime} seconds')
                time.sleep(lockoutTime)
                timeOut += 1
                attempt = 1
                print(f'Try again')

            else:
                print('Incorrect pin: User not verified')
                print('Try Again')
                attempt += 1

        except KeyboardInterrupt:
            print('User closed program')
            loop = False

#print(userVerified()) #Debugging