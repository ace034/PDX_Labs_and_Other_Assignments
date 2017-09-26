input os
import sys

USER_Answr = input ('Hey do you want to convert your score to a letter?\n:')
if USER_Answr == 'yes':
    user_number = int(input('What is your numerical grade?'))
    if 125 > user_number >100:
        print('THe only way to have gotten a score this high is to have cheater')
    if 99 > user_number > 90:
        print('You\'re either an over achiever or a cheater either way good job')
    elif USER_Answr = 'No':
    print ('Well its your choice feel free to use the mighty grade con agian later')''
