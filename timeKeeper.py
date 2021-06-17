import time
from datetime import datetime

class timeKeeper:
    def __init__(self):
        #self.start = time.time() #Record start time
        pass
    def getLogTime(self):
        return str(datetime.now()) #Return the current time 

    def getDate():
        crntDate = datetime.now().strftime("%m/%d/%Y %H:%M:%S") #Get formated verision of current time
        return crntDate