import socket
from sys import stdout
from time import time
from binascii import unhexlify

# set the server's IP address and port
ip = "192.168.0.162"
port = 12003
# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
s.connect((ip, port))

# 1 for debug mode otherwise 0
DEBUG = 0

# timing constants
ZERO = .025
ONE = .1
IGNORE = (ZERO + ONE)/2

# message variables
covertBin = ""
covert = ""

# receive data until EOF
data = s.recv(4096)
data = data.decode()

# receive data and determine covert message by timing
while (data.rstrip("\n") != "EOF"):
    # output the data
    stdout.write(data)
    stdout.flush()
    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    data = data.decode()

    # gather binary covert message using timing
    delta = round(t1 - t0, 3)
    if(DEBUG):
        stdout.write("\nDELTA: " + str(delta) + "\n")
        stdout.flush()

    # determine covert bit based on timing
    if(abs(delta - ZERO) < abs(delta - ONE)):       # check if delta is closer to ZERO than ONE
        if(abs(delta - ZERO) < abs(delta - IGNORE)):
            covertBin += "0"
    else:
        if(abs(delta - ONE) < abs(delta - IGNORE)):
            covertBin += "1"

#output binary form of covert message
print("\nBinary String: {}".format(covertBin))

# convert the binary covert message into english
i = 0
while(i < len(covertBin)):
    b = covertBin[i:i + 8]
    #n = int("0b{}".format(b),2)
    try:
        covert += chr(int(b, 2))
        #covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    i+=8


# close the connection to the server
s.close()

# display messaage
try:
    print ("\nCovert Message: ",covert[:covert.rindex("EOF")])
except ValueError:
    print (covert)
