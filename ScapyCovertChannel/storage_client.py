#! python
from scapy.all import *
from piggybackEncodeDecodeIP import decodeIP
from math import floor
conf.promisc = False

def check_seq_num(p: Packet):
    """Checks the sequence number to ensure its correct."""
    
    
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
    
    while(done):
        covertBin+=binary
        pkt = sniff(filter="src port 10010",count=1)
        done = check_eof(pkt[0][IP].src)
        binary,seq = decodeIP(pkt[0][IP].src)
        
        
        #SEQUENCE_NUM,drop = check_seq_num(pkt[0])
        
        # store pkts in buffer
    

    # convert the binary covert message into bytes
    j = 0
    hexArray=[]
    for i in range(floor(len(covertBin)/8) - 3): # -3 to remove EOF, could be done a better way
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