from art import *
import random
import string

def block_printer(x):
    printed_letter = text2art(x, font='block', chr_ignore=True)
    return printed_letter

'''First we need a random letter generator'''
Letters = string.ascii_uppercase
lucky_letter = random.choice(Letters)
saved_letter = lucky_letter
print(block_printer(lucky_letter))
my_input = input("what letter just popped up? ").upper()

if saved_letter == my_input:
    print("WOW YOU GOT IT RIGHT!")
else:
    print("WRONG!")