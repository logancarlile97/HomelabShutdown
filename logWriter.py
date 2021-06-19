from configReader import configReader
from timeKeeper import timeKeeper

class logWriter:
    def __init__(self):
        config = configReader('config.ini') #Get configuration file
        self.logFile = config.getLogConfig('logFile') #Get log file path
        self.time = timeKeeper()

    def write(self, message):
        with open(self.logFile, 'a') as log:
            log.write(f'[{self.time.getLogTime()}] ') #Record time message to be logged was recieved
            log.write(f'{message}\n') #Log message
            log.flush()
            log.close()
    
    def newEntry(self):
        with open(self.logFile, 'a') as log:
            log.write('\n')
            log.write('-----------------------\n')
            log.write('| !!!New log entry!!! |\n')
            log.write(f'| {self.time.getDate()} |\n')
            log.write('-----------------------\n')
            log.write('\n')
            log.flush()
            log.close()