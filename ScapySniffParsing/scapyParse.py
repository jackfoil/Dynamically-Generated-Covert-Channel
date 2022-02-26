#! python

from scapy.all import *
# my ip: 10.172.188.122 2022-02-25

# this should collect statistics on systems such as
# frequency of protocols
# destination ip
# number of packets sent
# number of packets received
def _getDataL(pkts: list) -> list:
    return proto
    
def _getTransL(pkts: list) -> dict:
    """ Returns a dictionary with the counts of each IP protocol in a list of packets. """
    proto = {}
    for i in pkts:
        protocol = i.sprintf("%IP.proto%")
        if protocol in proto:
            proto[protocol] += 1
        else:
            proto[protocol] = 1
    return proto

def _getNetL(pkts: list) -> list:
    """ Returns a dictionary with the counts of each Network protocol in a list of packets. """
    return proto


if __name__ == """__main__""":
    conf.promisc = False
    pcap = sniff(count=50)
    print(_getTransL(pcap))
   
    