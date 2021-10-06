from sys import argv
from os.path import exists



if len(argv) == 2:
    results = True
    file_name = (f"{str(argv[1])}.txt")
else:
    results = False
'''Here we're using a system arguement input in the python command line to
pass the name of the file that will be created or amended with the results of the session'''


if exists(file_name) == True :
    #go to function 2 to amend file and add new lines for results
    print("the file exists")
else:
    #go to function 1 for creating and amending
    print("a file doesn't exist and we will make one.")



print(file_name)