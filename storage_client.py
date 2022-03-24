#! python
from scapy.all import *
from piggybackEncodeDecodeIP import decodeIP
conf.promisc = False


if __name__ == "__main__":
    pcap = sniff(filter="src port 10010",count=1)
    for i in pcap:
        print(decodeIP(i[IP].src))

