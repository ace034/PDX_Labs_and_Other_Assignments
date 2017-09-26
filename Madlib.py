import os
# easiest way o clear screen
os.system('cls' if os.name == '**' else 'clear')
# .upper() is a comand outside of the input that forces the input into capitolized format
int1 = input("Give me a size i.e 'small' 'medium' 'large':\n").upper()
int2 = input("Give me a different size i.e 'small' 'medium' 'large' :\n").upper()
# {} lets insert the inputs of different intigers
print("One {} step for man, one {} leep for mankind? \n".format(int1, int2))
