from os.path import exists
import time
from useroptions import custom_letters

timestamp = time.strftime("%Y-%m-%d %H:%M:%S")


'''Here we're using a system arguement input in the python command line to
pass the name of the file that will be created or amended with the results of the session'''

'''results and v0 to v3 are parameter place holders for use in the save_function when it gets called by functionfile.py'''

def save_function(v0, v1, v2, v3):
    if exists(v0) == True :
        f2 = open(v0, "a")
        f2.write(f"{timestamp} \nScore:{v1}, Rounds: {v2}, Percentage: {v3} \n")
        f2.close()
        print(f"Data has been written to {v0} ")
    else:
        f1 = open(v0, "+w")
        f1.write(f"{timestamp} \nScore:{v1}, Rounds: {v2}, Percentage: {v3} \n")
        f1.close()
        print("A file did not exist, so we just made one.")

def save_the_list(v4):
    f1 = open(v4, "a")
    f1.write(f"{custom_letters} \n")
    f1.close()