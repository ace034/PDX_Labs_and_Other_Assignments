import os
import random
os.system('clear')

dice = range(0, 150)
sides = range(4, 100)

dice_amount = int(input("Hey how many dice do you have? \n:"))
dice_sides = int(input('How many side do your dice have? \n:' ))
print("You rolled {}" .format(random.choice(dice) * number(dice_amount))
