#! python

from scapy.all import *
from datetime import datetime
conf.promisc = False

# track total number of packets when converting to class

def countlayers(pkts: PacketList) -> dict:
    """ Returns the a dictionary with the counts of each protocol in a list of packets. """
    proto = {}
    for i in pkts:
        count = 0
        while True:
            layer = i.getlayer(count)
            if layer is None:
                break
            if layer.name in proto:  proto[layer.name] += 1
            else: proto[layer.name] = 1
            count += 1
    return proto

def countipsrcs(pkts: PacketList) -> dict:
    """ Returns a dictionary of dictionaries with source and destination addresses """
    srcs = {}
    for i in pkts:
        try:
            src = i[IP].src
        except:
            continue
        if src in srcs: srcs[src] += 1
        else:   srcs[i[IP].src] = 1
    return srcs

def countipdsts(pkts: PacketList) -> dict:
    dsts = {}
    for i in pkts:
        try:
            dst = i[IP].dst
        except:
            continue
        if dst in dsts: dsts[dst] += 1
        else:   dsts[i[IP].dst] = 1
    return dsts

def countmacs(pkts: PacketList) -> dict:
    return

def counttimes(pkts: PacketList) -> dict:
    t = {}
    for i,j in enumerate(pkts):
        t[i]=datetime.fromtimestamp(j.time).strftime("%H:%M:%S.%f")
    return t

def displaycount(proto: dict, t: int) -> None:
    """ Pretty prints protocols and counts for each. """
    for i,j in proto["layers"].items():
        print("{} : {}/{}".format(i,j,t))

def displaytimes(proto: dict) -> None:
    for i,j in proto["times"].items():
        print("{} : {}".format(i,j))

def displaysources(proto: dict) -> None:
    for i,j in proto["ipsrcs"].items():
        print("{} : {}".format(i,j))

def displaydestinations(proto: dict) -> None:
    for i,j in proto["ipdsts"].items():
        print("{} : {}".format(i,j))  

if __name__ == """__main__""":

    # assignments
    total = 10
    pcap = sniff(count=total)
    track = {}
    track["layers"] = countlayers(pcap)
    track["times"] = counttimes(pcap)
    track["ipsrcs"] = countipsrcs(pcap)
    track["ipdsts"] = countipdsts(pcap)

    # display
    displaycount(track,total)
    displaytimes(track)
    displaysources(track)
    displaydestinations(track)

#notes: maybe have dictionary of possible protocols for each layer
#       update count of each layer & display counts
#       maybe have it sorted in a specific order
#       maybe can use .aliastypes to get packet layer numbers


    