## Libaries
import psutil
import os
import time


# Example: Downloads / Desktop / Pictures
# Example: txt / PNG / pdf /exe

filetype = input("Which files would you like to look at? ").split()
filepath = input("What file path would you like to take? ").split()


user_list = psutil.users()


with open('allfiles.txt', 'w') as wf:
    for user in user_list: # files through the list of users 
        username = user.name

        ## goes thoguh all the path files inputs the user wants 
        for mulpaths in filepath:
            path = r"C:\Users"
            path = str(path) + "\\" + str(username) + "\\" + str(mulpaths)
            l = os.listdir(path)

            #####Compare the file type now
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
                                    wf.write('\n')
                                else:
                                    continue
                            break




            
