##SCANS FOR ALL OF THE FILES ON THE SYSTEM
import time
import os

#start_time = time.time()

path = r"C:\Users"

l = os.listdir(path)


with open('allfiles.txt', 'w') as wf:
    for root, dirs, files in os.walk(path):
        for f in files:
            wf.write(os.path.join(root, f))
            wf.write('\n')

#end_time = time.time()

#print(str(end_time-start_time) + " in seconds file has been created")
