from visualscanning import *
from savelogfunction import *
from sys import argv
from useroptions import saveoption, save_custom_list_option, customletterflag

if len(argv) == 2:
    file_name = (f"{str(argv[1])}.txt")
elif len(argv) == 1:
    file_name = "results.txt"


rounds = int(input("How many rounds do you want this to go for? "))
correct_answer = 0
user_score = 0
'''Variables for user_score created here as a workaround to data collection as a work around to local variables not saving on return.'''

i = 0
while i != rounds:
    correct_answer = start_game()
    if correct_answer == 1:
        user_score +=1
    i += 1

print(user_score)

percentage_correct = user_score*100/rounds

print(f"Good job!, you got {percentage_correct}% correct out of {rounds} trials. ")

if saveoption == True:
    save_function(file_name, user_score, rounds, percentage_correct)
else:
    pass

if save_custom_list_option == True and customletterflag == True:
    save_the_list(file_name)
else:
    pass


'''Calls the savelog function'''