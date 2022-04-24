import socket
from time import sleep
from binascii import hexlify

def socketTiming(port, filepath):
    # set the port for client connections
    port = port
    # create the socket and bind it to the port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    # listen for clients
    s.listen(1)

    # a client has connected!
    c, addr = s.accept()

    # timing constants
    ZERO = .1
    ONE = 1


    # import covert file as binary data
    covertBin = ""
    with open(filepath, "rb") as f:
        covert = f.read()
    for line in covert:
        covertBin += bin(line)[2:].zfill(8)

    print(covertBin)

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


if __name__ == '__main__':
    socketTiming(10000, 'Hi.txt')