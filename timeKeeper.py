import time

#Holds the time the program started
def initialize():
    global start 
    start = time.time()

#Returns the time that the program has currently been running for
def deltaStart():
        return round(time.time() - start, 4)