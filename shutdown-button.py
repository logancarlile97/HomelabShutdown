import RPi.GPIO as GPIO
import subprocess
import lcd_driver

#Setup GPIO pins
GPIO.setmode(GPIO.BCM)

#Set GPIO 24 (pin 18) to input and connect to an internal pull up resistor
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Wait until button is pressed
GPIO.wait_for_edge(24, GPIO.FALLING)

#Clear the LCD
lcd_driver.lcdInit()
lcd_driver.lcdClear()

#Run the shutdown
subprocess.call(['sudo', 'shutdown', 'now'], shell=False)
