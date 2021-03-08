import time
from datetime import datetime

#Holds the time the program started
def initialize():
    global start 
    start = time.time()

#Returns the time that the program has currently been running for
def deltaStart():
        return round(time.time() - start, 4)

#Prints the date and time to the log
def dateToLog(logFile):
    
    #Holds the current date
    crntDate = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    #Open the log
    with open(logFile, 'a') as log:
        log.write('\n')
        log.write('-----------------------\n')
        log.write('| !!!New log entry!!! |\n')
        log.write(f'| {crntDate} |\n')
        log.write('-----------------------\n')
        log.write('\n')

    #Close log
    log.close()    