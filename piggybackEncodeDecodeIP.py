# IP is a string representation of an encoded IP address
# binary is a string representation of an byte of binary data
def decodeIP(IP):
    ipSplit = IP.split(".")
    decimal = ipSplit[3]
    binary = bin(int(decimal))
    binary = str(binary[2:].zfill(8))

    return binary

# IP is a string representation of a normal IP address
# binary is a string representation of an byte of binary data that you want to hide
# encodedIP is a string representation of an encoded IP address

def encodeIP(IP, binary):
    index = IP.rfind(".")
    decimal = str(int(binary,2))

    encodedIP = IP[:index+1] + decimal
    return encodedIP

# startingIP = "14.64.134.43"
# byteToHide = "10000000"
#
#
# newIP = encodeIP(startingIP,byteToHide)
# print("IP with hidden byte: {}".format(newIP))
# print("Binary hidden within: {}".format(decodeIP(newIP)))
