import random
import os
os.system('cls' if os.name == '**' else 'clear')
#trying to allow for any input :\n is the new line command preoper use is within the print section
user_respose = input('Do you wanna play rock paper scissors "Y" or "N "?:\n')
no = ['N' , 'n' , 'no' , 'NO' , 'No']
yes = ['Y' , 'y' , 'yes' , 'YES' , 'Yes']

option_list = ['Rock']
computerChoice = ['Rock' , 'Paper' , 'Scissors']
x = 'Rock'
y = 'Paper'
z = 'Scissors'

if user_respose in no:
    running = False
    print(":- / Well it's your call :-/ ")

if user_respose in yes:
    running = True

    while running == True:
        print("Ok...Rock, Paper Scissors?:\n")
        computerChoice = random.choice(option_list)
        print(user_choice + (random.choice(option_list))
    if computerChoice == 'Rock':
    if option_list == 'Rock':
        print("Ha we tied, Do you wanna play agian?")
            if input in yes:
                running = True
            elif input in no:
                running = False

    computerChoice = random.choice(option_list)
    if user_choice == Paper:
        if option_list == Rock:
            print("You win, Do you wanna play agian?")
            if input in yes:
                running = True
            elif input in no:
                running = False

    computerChoice = random.choice(option_list)
    if user_choice == Scissors:
        if option_list == Rock:
            print("Ha Ha I win, Do you wanna play agian?")
            if input in yes:
                running = True
            elif input in no:
                running = False
