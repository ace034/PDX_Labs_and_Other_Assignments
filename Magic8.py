import os
import random
import sys
first_question = input("The magic 8 ball knows all, what is your question? \n:")
print('HMM...')

possible_responce = [" It is certian" , " It is decidedly so" , ' Without a doubt' , " Yes definitely" , ' You may rely on it' , ' Most likely' , ' Outlook good' , ' Yes' , ' Concentrate and ask agian ' , ' Signs point to yes' , ' As I see it' , ' Yes definitely' , ' Reply hazy try agian' , ' Ask agian later' , ' Better not tell you now' , ' Dont count on it'  , 'My reply is no' , 'My reply is no' ]

if first_question != None:
    print(random.choice(possible_responce))

keep_going = input('Do you have another question?\n:')

running = True
while running:
    if keep_going.lower() in ['yes' , 'y' , 'yep']:
        if possible_responce != None:
            print ("The magic 8 ball knows all... but chooses to ignore you")
            running = False
            #sys.exit
            #print(random.choice(possible_responce))
    elif keep_going.lower() in ['no' , 'n' , 'nope']:
        running = False
        print('Very well have a lovily day')
    #elif keep_going.find("?"):
        #print("The magic 8 ball knows all... but chooses to ignore you"):
        #sys.exit
    else:
        keep_going = input("I'm looking for a yes or no?\n:")
