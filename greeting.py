import os
# easiest way o clear screen
os.system('cls' if os.name == '**' else 'clear')
users_name = input("Psst Hey whats your name? \n:")

os.system('cls' if os.name == '**' else 'clear')
while True:

    users_age = input("Hey old are you?\n:")
# this line creates a list of string for 0-1
    if users_age in [str(i) for i in range(0 ,150)]:
        os.system('cls' if os.name == '**' else 'clear')
        users_age = int(users_age)
        break

    print("No I need your real age give em a number")
# users_age = users_age + 1
print("So {} you will be {} next year? \n".format(users_name, users_age + 1))
print('*' * len(users_name) + users_name + '*' * len(users_name) )
