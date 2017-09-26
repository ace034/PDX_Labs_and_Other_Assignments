import random
import os
os.system('cls' if os.name == '**' else 'clear')
#trying to allow for any input :\n is the new line command preoper use is within the print section
user_respose = input('Do you wanna play rock paper scissors "Y" or "N "?:\n')

no = ['N' , 'n' , 'no' , 'NO' , 'No']
yes = ['Y' , 'y' , 'yes' , 'YES' , 'Yes']

option_list = ['Rock' , 'Paper' , 'Scissors']
#user_choice.lower() = ('Rock' , 'Paper' , 'Scissors')

x = 'Rock'
y = 'Paper'
z = 'Scissors'

if user_respose in yes:
    running = True

if user_respose in no:
    running = False
    print(":- / Well it's your call :-/ ")

#Rock
while running == True:
    user_choice=input ("Ok...Rock, Paper Scissors?:\n")
    print (user_choice)
    computerChoice = random.choice(option_list)
    if user_choice == x:
        if option_list == x:
            print("Ha we tied, Do you wanna play agian?")
        if input in yes:
            running = True
        elif input in no:
            running = False

    computerChoice = random.choice(option_list)
    if user_choice == y:
        if option_list == x:
            print("You win, Do you wanna play agian?")
        if input in yes:
            running = True
        elif input in no:
            running = False

    computerChoice = random.choice(option_list)
    if user_choice == z:
        if option_list == x:
            print("Ha Ha I win, Do you wanna play agian?")
        if input in yes:
            running = True
        elif input in no:
            running = False
    #Scissors x ='Rock'  y ='Paper'=   z = 'Scissors'

    computerChoice = random.choice(option_list)
    if user_choice == z:
        if option_list == z:
            print("Ha we tied, Do you wanna play agian?")
        if input in yes:
            running = True
        elif input in no:
            running = False

    computerChoice = random.choice(option_list)
    if user_choice == x:
        if option_list == z:
            print("You win, Do you wanna play agian?")
        if input in yes:
            running = True
        elif input in no:
            running = False

    computerChoice = random.choice(option_list)
    if user_choice == y:
        if option_list == x:
            print("Ha Ha I win, Do you wanna play agian?")
        if input in yes:
            running = True
        elif input in no:
            running = False

    #Papper x ='Rock'  y ='Paper'=   z = 'Scissors'
    computerChoice = random.choice(option_list)
    if user_choice == y:
        if option_list == y:
            print("Ha we tied, Do you wanna play agian?")
        if input in yes:
            running = True
        elif input in no:
            running = False

    computerChoice = random.choice(option_list)
    if user_choice == y:
        if option_list == z:
            print("You win, Do you wanna play agian?")
        if input in yes:
            running = True
        elif input in no:
            running = False

    computerChoice = random.choice(option_list)
    if user_choice == y:
        if option_list == x:
            print("Ha Ha I win, Do you wanna play agian?")
        if input in yes:
            running = True
        elif input in no:
            running = False


    # this is the cleanest catch all way of if not my options then try my options.
    else:
        input!=''
    print('Umm is that a yes or no')

if input in no:
    running = False
    print("Well it's your call")

option_list = ['Rock' , 'Paper' , 'Scissors']



#computer choices are default listed first
