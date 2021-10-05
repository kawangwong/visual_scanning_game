from art import *
import random
import string
import time

def block_printer(x):
    printed_letter = text2art(x, font='block', chr_ignore=True)
    return printed_letter

'''Function used to create and show the block letters randomly here'''

def start_game():
    '''First we need a random letter generator'''
    Letters = string.ascii_uppercase
    lucky_letter = random.choice(Letters)
    print(block_printer(lucky_letter))
    my_input = input("what letter just popped up? ").upper()
    if lucky_letter == my_input:
        time.sleep(0.2)
        print("WOW YOU GOT IT RIGHT!")
    else:
        time.sleep(0.2)
        print(f"WRONG! This was the letter {lucky_letter}")