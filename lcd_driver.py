import adafruit_character_lcd.character_lcd as characterLCD
import board
import digitalio
import time

def lcdInit():
    #Assign each lcd pin to GPIO 
    lcd_rs = digitalio.DigitalInOut(board.D17) #GPIO 17 pin 11
    lcd_en = digitalio.DigitalInOut(board.D27) #GPIO 27 pin 13
    lcd_d4 = digitalio.DigitalInOut(board.D22) #GPIO 22 pin 15
    lcd_d5 = digitalio.DigitalInOut(board.D10) #GPIO 10 pin 19
    lcd_d6 = digitalio.DigitalInOut(board.D9)  #GPIO 9 pin 21
    lcd_d7 = digitalio.DigitalInOut(board.D11) #GPIO 11 pin 23
    lcd_columns = 16
    lcd_rows = 2
    global lcd 
    lcd = characterLCD.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

def lcdMessage(top, bottom):
    print(str(len(top)))
    if (len(top) == 0):
        adjTop = top
    else:
        adjTop = top.ljust(16)
    if (len(bottom) == 0):
        adjBottom = bottom
    else:
        adjBottom = "\n" + bottom.ljust(16)

    #lcd.message = "Top" + "\n Bottom"
    #time.sleep(5)
    #lcd.message = "" + "\n Test"
    lcd.message = adjTop + adjBottom

def lcdClear():
    lcd.clear()