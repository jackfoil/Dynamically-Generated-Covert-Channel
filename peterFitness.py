from ping3 import ping
import os
from scapy.all import sniff, conf

def fitnessFunction(hostAddr, targetPath, pingThreshhold, sizeThreshhold, trafficThreshold):

    conf.promisc = False

    isPingHigh=None
    isSizeHigh=None
    isTrafficHigh=None

    # pingThreshhold=pingThreshhold
    # sizeThreshhold=sizeThreshhold
    # trafficThreshold=trafficThreshold
    #
    #
    # targetPath=targetPath
    # hostAddr=hostAddr

    response=[]

    #ping and average response time
    for _ in range(10): response.append(ping(hostAddr))
    isPingHigh=(sum(response)/len(response))>pingThreshhold
    # print(isPingHigh)

    #find file size and compare to threshold
    size = os.path.getsize(targetPath)
    isSizeHigh=size>sizeThreshhold
    # print (isSizeHigh)

    # add filter for TCP packets
    packets=sniff(count=0, timeout=10)

    numPackets = len(packets)
    isTrafficHigh=numPackets>trafficThreshold
    # print (isTrafficHigh)

    return isPingHigh, isSizeHigh, isTrafficHigh
