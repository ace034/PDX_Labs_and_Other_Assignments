import os
# os.sytem("clear")
os.system('cls' if os.name == '**' else 'clear')

yes = ['yes', 'y']
no = ['no', 'n']
vowels = "aeIouyAEiOUY"


running = True
while running:
    print("I can create Pig latin words would you like to try? \n:")
    responce = input()
    if responce.lower() in yes:
        print('Ook whats your word? \n:')
        word = input()
        if word[0] in vowels:
            print('{}{}yay'.format(word[1:], word[0]))
        else:
# it is not nesicarry to identify the place holders insingle f format
            print('{}ay'.format(word))
    elif responce.lower() in no:
        running = False
        print("Ok I didn't wanna show you anyway \n:")
        break
    else:
        print('So is that a Yes or No')
