from os.path import exists
import time

timestamp = time.strftime("%Y-%m-%d %H:%M:%S")


'''Here we're using a system arguement input in the python command line to
pass the name of the file that will be created or amended with the results of the session'''


def save_function(theresults, v0, v1, v2, v3):
    if theresults == True:
        if exists(v0) == True :
            f2 = open(v0, "a")
            f2.write(f"{timestamp} \nScore:{v1}, Rounds: {v2}, Percentage: {v3} \n")
            f2.close()
            print("Data has been written")
        #go to function 2 to amend file and add new lines for results
        else:
            f1 = open(v0, "+w")
            f1.write(f"{timestamp} \nScore:{v1}, Rounds: {v2}, Percentage: {v3} \n")
            print("A file did not exist, so we just made one.")
    else:
        pass