##Imporivements: error handling, need to add the run fucntion, random qotes

##Front end of the program
from art import *
import sys
import os



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
                    
            
        ##need to add run
        if(commands[0] == "run"):
            return(filetype, filepath)
        
            #print("need to work on this")
            #os.system("python test.py") # calls on the python script and will give it two parameters 



if __name__ == '__main__':
    (filetype, filepath) = console()



##Notes:
###sites that could help
# https://stackoverflow.com/questions/57009481/running-python-script-with-temporary-environment-variables (to give script predefined variables)
# https://www.tutorialspoint.com/How-can-I-make-one-Python-file-run-another (how to import your own file scripts)

# https://www.delftstack.com/howto/python/python-run-another-python-script/
# ^^^^^^^^ solution neeed to make it into a class system 




