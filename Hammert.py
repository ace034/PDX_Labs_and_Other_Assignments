import os
import random
os.system("clear")
time = int(input("What hour is it? \n:"))

yes = ['yes' , 'y']
no = ['no' , 'n']
question = ['yes' or 'no']
hammer = [10, 11, 12, 1, 2, 3, 4,]
breakfast = [7, 8, 9,]
lunch = [12, 1, 2]
dinner =[7, 8, 9]

qtime = input("Is that am? 'yes' or 'no'")

# if time in breakfast:
#     print("Is that am? 'yes' or 'no' \n:")
if time.lower() in hammer:
    print("Is that am? 'yes' or 'no'")
    if time.lower() in yes:
            print("Then it is hammer time")
    if time.lower() in no:
            print("Then it is lunch duh")

elif time.lower() in breakfast:
    print("Then it is clearly breakfast time \n:")
elif time.lower() in no:
    print("Then wouldn't that make it dinner \n:")
else:
    print("That is an erielvant time.")
