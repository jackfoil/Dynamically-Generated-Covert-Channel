from peterFitness import fitnessFunction
from frontEnd import *
from TargetSocketTiming import socketTiming
from TargetActiveStorage  import activeStorage
# from TargetPiggybackStorage import piggybackStorage



if __name__ == "__main__":
    pingThreshhold=64
    sizeThreshhold=2048
    trafficThreshold=1024


    filepath = "Hi.txt"
##    ip_addr = "google.com"
    isPingHigh, isSizeHigh, isTrafficHigh = fitnessFunction(ip_addr, filepath, pingThreshhold, sizeThreshhold, trafficThreshold)

    isSizeHigh = True
    isPingHigh = True
    isTrafficHigh = False
    

    print("hi")

    if (not isSizeHigh and not isPingHigh):
        socketTiming(port, filepath)
        
    elif (isTrafficHigh):
        piggybackStorage(ip_addr, port, filepath)

    else:
        activeStorage(ip_addr, port, filepath)
