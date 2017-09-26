import random
import os
os.system('cls' if os.name == '**' else 'clear')

yes = ('yes' , 'y')
no = ('no' , 'n')

numbers = range(0, 10)
second_question = range(0, 10)

user_guess = input("Do you want to play a game? \n:")
user_number = int(input("What is your number? \n:"))
if user_guess.lower() in yes:
    print('Try and guess my number between its a number 1 - 10')
    pc_pick = random.choice(numbers)
    if user_number > pc_pick:
        print('Whoops to high try agian')
        running = True
    if user_number < pc_pick:
        print('Whoops to low try agian')
        running = True
    if user_number == pc_pick:
        print("YOU GOT IT")
        running = False

elif user_guess.lower() in no:
    print('Ok maybe next time')

else:
    print('So you do wanna play "yes" or "no"')
