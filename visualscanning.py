from art import *
import random
import string
import time

def block_printer(x):
    printed_letter = text2art(x, font='block', chr_ignore=True)
    return printed_letter

'''Function used to create and show the block letters randomly here'''
correct = 0

def start_game(correct):
    '''First we need a random letter generator'''
    Letters = string.ascii_uppercase
    lucky_letter = random.choice(Letters)
    print(block_printer(lucky_letter))
    my_input = input("what letter just popped up? ").upper()
    if lucky_letter == my_input:
        time.sleep(0.2)
        print("WOW YOU GOT IT RIGHT! You got 1 point!")
        correct += 1
        return correct
    else:
        time.sleep(0.2)
        print(f"WRONG! This was the letter {lucky_letter}. Do better next time!")
        return correct

print(start_game(correct))

'''We need to also include code into this that would create a function that would save results
this information could be detailed as in letters, or could be as simple as just rights and wrongs
More detail can be used to actually create datametrics for difficulty scales.'''

'''We need to create a function here to created or amend a text file with time and results'''