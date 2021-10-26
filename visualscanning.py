from art import *
import random
import string
import time
from useroptions import customletterflag, custom_letters, fontSelect

def block_printer(x):
    printed_letter = text2art(x, font=fontSelect, chr_ignore=True)
    return printed_letter

if customletterflag == False:
    Letters = string.ascii_uppercase
elif customletterflag == True:
    Letters = [letter.upper() for letter in custom_letters]

'''Function used to create and show the block letters randomly here or through a user generated list'''
def start_game():
    x = 0
    '''First we need a random letter generator'''
    lucky_letter = random.choice(Letters)
    print(block_printer(lucky_letter))
    my_input = input("what letter just popped up? ").upper()
    if lucky_letter == my_input:
        time.sleep(0.2)
        print("WOW YOU GOT IT RIGHT! You got 1 point!")
        x += 1
        return x
    else:
        time.sleep(0.2)
        print(f"WRONG! This was the letter {lucky_letter}. Do better next time!")
        return x

'''We need to also include code into this that would create a function that would save results
this information could be detailed as in letters, or could be as simple as just rights and wrongs
More detail can be used to actually create datametrics for difficulty scales.'''