from visualscanning import *

rounds = int(input("How many rounds do you want this to go for? "))
correct_answer = 0
user_score = 0
i = 0
while i != rounds:
    correct_answer = start_game()
    if correct_answer == 1:
        user_score +=1
    i += 1

print(user_score)

percentage_correct = user_score*100/rounds

print(f"Good job!, you got {percentage_correct}% correct out of {rounds} trials. ")
