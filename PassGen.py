import os
import random
import string
#string.ascii_letters is A-Z upper and lower string.digits is 0-9 in order to use string list you must import strings
passchar_list = list(string.ascii_letters +string.digits)
#string.punctuation is a list of special characters !@#$%^&*()_+
special_passchar_list = list(string.punctuation + string.ascii_letters + string.digits)
#os.system('cls' if os.name == '**' else 'clear') is a clear screen command that referances the name of OS import os command must be run for this to work

no = ['n' , 'no']
yes = ['y' , 'yes']

os.system('cls' if os.name == '**' else 'clear')
# This line treats the user input as in integer
user_length = int(input('How many characters would like your password to be?\n:'))

second_question = input('Do you want special characters?\n:')
#because we have a second question you can tie if than loops to it
#by writing the question --- second_question---.lower() I dont have to have so many options in my list and it converts the user resposce to lower case
if second_question.lower in no:
    CharLength = ''
    for i in range(0, user_length):
# this line will let it add characters from passchar_list
        CharLength = CharLength + random.choice(passchar_list)
    print(CharLength)
#by writing the question --- second_question---.lower() I dont have to have so many options in my list and it converts the user resposce to lower case
elif second_question.lower() in yes:
    CharLength = ''
    for i in range(0, user_length):
# this line will let it add characters from passchar_list
            CharLength = CharLength + random.choice(special_passchar_list)
    print(CharLength)

else:
    print('Wait you lost me')
    #print(random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + '-' + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + '-' + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + '-' + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + '-' + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list) + random.choice(passchar_list))
