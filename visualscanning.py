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
    saved_letter = lucky_letter
    '''This will put the letter in a saved variable to be compared later with user response'''
    print(block_printer(lucky_letter))
    my_input = input("what letter just popped up? ").upper()
    if saved_letter == my_input:
        time.sleep(0.2)
        print("WOW YOU GOT IT RIGHT!")
    else:
        time.sleep(0.2)
        print(f"WRONG! This was the letter {saved_letter}")