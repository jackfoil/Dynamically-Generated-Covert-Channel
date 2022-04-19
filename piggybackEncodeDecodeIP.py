# IP is a string representation of an encoded IP address
# binary is a string representation of an byte of binary data
def decodeIP(IP):
    ipSplit = IP.split(".")
    decimal = ipSplit[3]
    binary = bin(int(decimal))
    binary = str(binary[2:].zfill(8))
    seq = ipSplit[2]

    return binary, seq

# IP is a string representation of a normal IP address
# binary is a string representation of an byte of binary data that you want to hide
# encodedIP is a string representation of an encoded IP address
def encodeIP(IP, binary, seq):
    dot1Index = IP.find(".")
    dot2Index = IP.find(".",dot1Index+1)

    decimal = str(int(binary,2))

    encodedIP = IP[:dot2Index+1] + str(seq) + "." + decimal
    return encodedIP


# startingIP = "14.64.134.43"
# byteToHide = "10000000"
# for i in range(10):
#     newIP = encodeIP(startingIP,byteToHide,i)
#     print("IP with hidden byte: {}".format(newIP))




# startingIP = "14.64.134.43"
# byteToHide = "10000000"
#
#
# newIP = encodeIP(startingIP,byteToHide)
# print("IP with hidden byte: {}".format(newIP))
# print("Binary hidden within: {}".format(decodeIP(newIP)))
