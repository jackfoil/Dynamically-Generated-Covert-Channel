#! python
from peterFitness import fitnessFunction
from frontEnd import *
from TargetSocketTiming import socketTiming
from TargetActiveStorage  import activeStorage
from TargetPiggybackStorage import piggybackStorage



if __name__ == "__main__":
    pingThreshhold=64
    sizeThreshhold=64
    trafficThreshold=2048

    noEXE = True

    if(noEXE):
        with open("variables.txt", "r") as f:
            filepath = f.readline().strip("\n")
            port = int(f.readline().strip("\n"))
            ip_addr = f.readline().strip("\n")

    print(f"{filepath}\n{port}\n{ip_addr}")

    print("gathering network statistics...")
    isPingHigh, isSizeHigh, isTrafficHigh = fitnessFunction(ip_addr, filepath, pingThreshhold, sizeThreshhold, trafficThreshold)
    print("gathered\n")


    if (not isSizeHigh and not isPingHigh):
        print("socket")
        socketTiming(port, filepath)

    elif (isTrafficHigh):
        print("piggback storage")
        piggybackStorage(ip_addr, port, filepath)

    else:
        print("active storage")
        activeStorage(ip_addr, port, filepath)
