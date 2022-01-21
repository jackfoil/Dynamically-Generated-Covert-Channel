import socket
from time import sleep
from binascii import hexlify

# set the port for client connections
port = 12003
# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
# listen for clients
s.listen(1)

# a client has connected!
c, addr = s.accept()

# timing constants
ZERO = .025
ONE = .1


# read txt file containing secret message
f = open("secret.txt","r")
covert = f.readlines()
# add EOF to know when the secret message is complete
covert.append("EOF")

# convert each character in hidden message to binary based on ASCII value
covertBin = ""
for line in covert:
    for i in line:
        covertBin += bin(ord(i))[2:].zfill(8)
        #covertBin += bin(int(hexlify(i), 16))[2:].zfill(8)

n = 0
# send garbage messages at covert rate
for i in range(len(covertBin)):     # because we are dealing with large covert messages we need to make it modular
    c.send(".".encode())            # send dots because why not
    if(covertBin[n] == "0"):
        sleep(ZERO)
    else:
        sleep(ONE)
    n = (n + 1)%len(covertBin)

# send EOF to know when to stop listening
c.send("EOF".encode())
c.close()
