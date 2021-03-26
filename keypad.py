import RPi.GPIO as GPIO
import time

def keypadMsge():

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #Holds the values entered on keypad
    message = ''

    #Holds whether the user has enter a message
    noMessage = True

    #Key layout on keypad
    KEYS = [ ['1','2','3','A'],
            ['4','5','6','B'],
            ['7','8','9','C'],
            ['*','0','#','D'] ]

    #Set the GPIO pins for colums and rows, 
    # make sure they are in the right order or keys will be backwards
    ROW = [19,13,6,5]
    COL = [21,20,16,12]

    try:

        #Set all Column pins to output high
        for j in range(len(COL)):
            GPIO.setup(COL[j], GPIO.OUT)
            GPIO.output(COL[j], 1)

        #Set all Row pins to input and pull up to high
        for i in range(len(ROW)):
            GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #Loop untill a message is entered by the user          
        while(noMessage):
            
            #Loop through each column pin and set output to low 
            for j in range(len(COL)):
                GPIO.output(COL[j], 0)
                
                #Loop through each row pin and see if its input is low
                #This will determine not only if a key is pressed but 
                # also what column and row the button press is assosiated with.
                for i in range(len(ROW)):
                    if GPIO.input(ROW[i]) == 0:
                        
                        #For debuging Print the pressed key by refrenceing the KEYS matrix
                        #print(KEYS[i][j])
                        
                        #If the key pressed is a pound then print, return, and clear the message 
                        if (KEYS[i][j] == '#'):
                            
                            #print(message) #For debuging
                            
                            #Return the user entered message
                            return message
                            message = ''

                            #Set noMessage to False
                            noMessage = False
                        
                        #If the key pressed is a astrisk then clear message
                        elif (KEYS[i][j] == '*'):
                            message = ''
                        
                        #Otherwise add inputed key to message
                        else:
                            message += KEYS[i][j]
                            
                        #While a key is being held down this will loop
                        while(GPIO.input(ROW[i]) == 0):
                            
                            #Sleep to prevent key bouncing
                            time.sleep(0.2)
                            pass
                
                #Set the column pin to 
                GPIO.output(COL[j],1)

        #Cleanup GPIO pins when program finishes
        GPIO.cleanup(ROW + COL)

    #Clean GPIO pins if user quits program
    except KeyboardInterrupt:
        GPIO.cleanup(ROW + COL)
        return 'UserExit'

    #Print any other errors to terminal
    except Exception as e:
        print('Keypad test ran into an error')
        print('Exception: ' + str(e))
        GPIO.cleanup(ROW + COL)

#print(keypadMsge())#Debuging
