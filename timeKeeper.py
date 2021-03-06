import time

#Holds the time the program started
def initialize():
    global start 
    start = time.time()

#Returns the time that the program has currently been running for
def deltaStart():
        return round(time.time() - start, 4)

def end_timer():
    end = time.time()
    return end

