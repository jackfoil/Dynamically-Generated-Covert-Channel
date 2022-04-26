from peterFitness import fitnessFunction
from frontEnd import *
from TargetSocketTiming import socketTiming
from TargetActiveStorage  import activeStorage
# from TargetPiggybackStorage import piggybackStorage



if __name__ == "__main__":
    pingThreshhold=64
    sizeThreshhold=2048
    trafficThreshold=1024

    noEXE = True

    if(noEXE):
        with open("variable.txt", "r") as f:
            filepath = f.readline()
            port = f.readline()
            ip_addr = f.readline()

    filepath = "Hi.txt"
##    ip_addr = "google.com"
    print("gathering network statistics...")
    isPingHigh, isSizeHigh, isTrafficHigh = fitnessFunction(ip_addr, filepath, pingThreshhold, sizeThreshhold, trafficThreshold)
    print("gathered\n")
    isSizeHigh = False
    isPingHigh = False
    isTrafficHigh = False


    if (not isSizeHigh and not isPingHigh):
        print("socket")
        socketTiming(port, filepath)

    elif (isTrafficHigh):
        print("piggback storage")
        piggybackStorage(ip_addr, port, filepath)

    else:
        print("active storage")
        activeStorage(ip_addr, port, filepath)