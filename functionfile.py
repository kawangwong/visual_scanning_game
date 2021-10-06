from visualscanning import *

rounds = int(input("How many rounds do you want this to go for? "))

i = 0
while i != rounds:
    start_game()
    i += 1

print(start_game(correct)/rounds)
