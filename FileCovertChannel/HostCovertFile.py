import socket
from sys import stdout
from time import time
from binascii import unhexlify
from math import floor

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
TOOHIGH = max(ONE,ZERO)*5

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
        print("\nDELTA: " + str(delta))

    # determine covert bit based on timing
    if(delta>TOOHIGH):
        print("\ndelta: {} is too high\n".format(delta))
        break

    elif(abs(delta - ZERO) < abs(delta - ONE)):       # check if delta is closer to ZERO than ONE
        if(abs(delta - ZERO) < abs(delta - IGNORE)):
            covertBin += "0"

            if(DEBUG):
                print("Covert Bit: 0 \n")

        else:
            print("\ndelta: {} is closer to 0 but not far enough to be sure".format(delta))
            print("consider using ZERO and ONE values that are further apart\n")
            break

    else:
        if(abs(delta - ONE) < abs(delta - IGNORE)):
            covertBin += "1"

            if(DEBUG):
                print("Covert Bit: 1 \n")

        else:
            print("\ndelta: {} is closer to 1 but not far enough to be sure".format(delta))
            print("consider using ZERO and ONE values that are further apart\n")
            break



#output binary form of covert message
print("\nBinary String: {}".format(covertBin))

# convert the binary covert message into bites
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


# close the connection to the server
s.close()

# display messaage
try:
    print ("\nCovert Message: ",covert[:covert.rindex("EOF")])
except ValueError:
    print (covert)
