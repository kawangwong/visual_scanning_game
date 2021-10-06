from sys import argv
from os.path import exists
from sampeldatafile import user_score, rounds, percentage_correct
import time

if len(argv) == 2:
    results = True
    file_name = (f"{str(argv[1])}.txt")
else:
    results = False
'''Here we're using a system arguement input in the python command line to
pass the name of the file that will be created or amended with the results of the session'''



if results == True:
    if exists(file_name) == True :
        f2 = open(file_name, "+w")
        f2.close()
        print("the file exists")
    #go to function 2 to amend file and add new lines for results
    else:
        f1 = open(file_name, "+w")
        ()
        print("a file doesn't exist and we just made one")
else:
    pass


timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

print(timestamp)