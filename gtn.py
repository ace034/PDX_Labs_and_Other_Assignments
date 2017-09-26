import os
import random
os.system("clear")

num_list = [0,101]
i = ['yes', '' ,  'no']
guess_count is 0

def comp_num(guess):
    guess = random.choice(num_list)
print("Do you wanna play a game 'yes' or 'no'")
# i is user respoce to question

if i.lower == 'no':
    running = False
    print("Very well have a horri... lovily day :-)")
elif i.lower == 'yes':
         print("Ok I'm going to pick a number and you have seven tries to get it. \n It'll be a whole number between 1 - 100")

running = True
if i < computerChoice:
    print("Nope your to low")
    guess_count += 1

elif i > computerChoice:
    print("Nope your to low")
    guess_count += 1

elif i == computerChoice:
    print("Wow you win...:-)")


if guess_count == 7
    print("HAH HAH you lose *THUMBS DOWN*")
    running = False
