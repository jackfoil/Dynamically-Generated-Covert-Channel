import socket
from time import sleep
from binascii import hexlify

'''declare destination to send packets'''


# timing constants
ZERO = .025
ONE = .1


# import covert file as binary data
covertBin = ""
with open("Bruh-Sound-Effect.mp3", "rb") as f:
    covert = f.read()
for line in covert:
    covertBin += bin(line)[2:].zfill(8)


n = 0
# send new packets at covert rate
for i in range(len(covertBin)):     

    '''send packet'''

    if(covertBin[n] == "0"):
        sleep(ZERO)
    else:
        sleep(ONE)
    n = (n + 1)%len(covertBin)

# send EOF to know when to stop listening
c.send("EOF".encode())
c.close()
