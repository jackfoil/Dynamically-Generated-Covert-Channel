#! python
from scapy.all import *
from heapq import heappop, heappush
from piggybackEncodeDecodeIP import decodeIP
from math import floor
conf.promisc = False


def check_eof(ip: str) -> bool:
    """Checks if received EOF IP."""
    if ip == "69.69.69.69":
        return False
    else:
        return True


if __name__ == "__main__":

    SEQUENCE_NUM=0
    covertBin=""
    binary=""
    done = True
    priority=[]
    expectedValue=0
    pack = 0
    print("[*] Listening...")
    while(done):
        pkt = sniff(filter="src port 10010",count=1)
        pack += 1
        done = check_eof(pkt[0][IP].src)
        #if not done: break
        binary,seq = decodeIP(pkt[0][IP].src)
        print("[*] Received Packet",seq)
        heappush(priority, [int(seq), binary])

        while(len(priority) > 0 and expectedValue == priority[0][0]):
            covertBin += heappop(priority)[1]
            #print(covertBin)
            expectedValue=(expectedValue+1)%256
    print()
    print("Priority: ",priority)
    print("Expected Value: ",expectedValue)
    print("Total Packets Received: {}".format(pack))


    # convert the binary covert message into bytes
    j = 0
    hexArray=[]
    print(covertBin)
    for i in range(floor(len(covertBin)/8)): 
        j=i*8
        if(covertBin[j:j+8].zfill(8) == None):
            print("NONE")
        dec = (int(covertBin[j:j+8],2))
        hexArray.append(dec)

    # write to binary file data to "output"
    with open("output", "wb") as output:
        output.seek(0)
        output.truncate()
        for char in hexArray:
            output.write(bytes((char,)))
