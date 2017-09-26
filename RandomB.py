'''
make a program that spits out 1 and 0 make it as long as the input number
'''
import random
import os
#os.system('cls' if os.name == '**' else 'clear') is a clear screen command that referances the name of OS import os command must be run for this to work
os.system('cls' if os.name == '**' else 'clear')
#this allows the user to ictate an input and the treat the input like an integer
user_length = int(input('Please type the number length\n:'))
binary_list = ['0' , '1']
#everytime you run the for loop you will want to increase the loop by one
bin_string = " "
#
for i in range(0, user_length):
    bin_string = bin_string + random.choice(binary_list)
print(bin_string)
