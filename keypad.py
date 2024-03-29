import RPi.GPIO as GPIO
import time
from configReader import configReader

config = configReader('config.ini')

def keypadMsge():
    global config

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #Holds the values entered on keypad
    entry = ''

    #Key layout on keypad
    KEYS = config.getKeypadConfig('keypadLayout')

    #Set the GPIO pins for colums and rows, 
    # make sure they are in the right order or keys will be backwards
    ROW = config.getKeypadConfig('rowPins')
    COL = config.getKeypadConfig('columnPins')

    try:

        #Set all Column pins to output high
        for j in range(len(COL)):
            GPIO.setup(COL[j], GPIO.OUT)
            GPIO.output(COL[j], 1)

        #Set all Row pins to input and pull up to high
        for i in range(len(ROW)):
            GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #Loop untill a entry is entered by the user          
        while(True):
            
            #Loop through each column pin and set output to low 
            for j in range(len(COL)):
                GPIO.output(COL[j], 0)
                
                #Loop through each row pin and see if its input is low
                #This will determine not only if a key is pressed but 
                # also what column and row the button press is assosiated with.
                for i in range(len(ROW)):
                    if GPIO.input(ROW[i]) == 0:
                        
                        #If the key pressed is a pound then print, return, and clear the entry 
                        if (KEYS[i][j] == '#'):
                            
                            #Return the user entered entry
                            return entry
                        
                        #If the key pressed is a astrisk then clear entry
                        elif (KEYS[i][j] == '*'):
                            entry = ''
                        
                        #Otherwise add inputed key to entry
                        else:
                            entry += KEYS[i][j]
                            
                        #While a key is being held down this will loop
                        while(GPIO.input(ROW[i]) == 0):
                            
                            #Sleep to prevent key bouncing
                            time.sleep(0.2)
                            pass
                
                #Set the column pin to 
                GPIO.output(COL[j],1)

        #Cleanup GPIO pins when program finishes
        GPIO.cleanup(ROW + COL)

    #Print any other errors to terminal
    except Exception as e:
        print('Keypad test ran into an error')
        print('Exception: ' + str(e))
        GPIO.cleanup(ROW + COL)


