import os
import time
os.system("clear")

yes = ['yes', 'y']
no = ['no', 'n' ]

#function which return reverse of a string
def reverse(s):
    return s[::-1]

def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)

    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False

while running:
    print("I can check for palidromes would you like me to do that? \n:")
    responce = input()
    if responce.lower() in yes:
        print('Ook whats your word? \n:')
        word = input()

    elif responce.lower() in no:
        print('Very well the decission is yours to make')
        time.sleep(.3)
        print("... even if it is a bad one.")

    else:
        print('So is that a Yes or No')
