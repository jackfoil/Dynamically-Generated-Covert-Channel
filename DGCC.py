from peterFitness import fitnessFunction
from jack import *
from TargetSocketTiming import socketTiming
from TargetActiveStorage  import activeStorage
# from TargetPiggybackStorage import piggybackStorage



if __name__ == "__main__":
    pingThreshhold=64
    sizeThreshhold=2048
    trafficThreshold=1024


    filepath = "D:/HI.txt"
    ip_addr = "google.com"

    isPingHigh, isSizeHigh, isTrafficHigh = fitnessFunction(ip_addr, filepath, pingThreshhold, sizeThreshhold, trafficThreshold)

    isSizeHigh = False
    isPingHigh = False

    print("hi")
    if (not isSizeHigh and not isPingHigh):
        socketTiming(port, filepath)
    print("bye")
    elif (isTrafficHigh):
        piggybackStorage(ip_addr, port, filepath)

    else:
        pass
        # activeStorage(ip_addr, port, filepath)
