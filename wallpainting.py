import os
from math import ceil
# easiest way o clear screen
os.system('clear')
wall_width = int(input("whats the width of your wall in ? \n:"))
wall_hitgh = int(input("whats the hight of your wall in feet? \n:"))
cost_of_paint = int(input("What is the cost of paint? \n:"))
wall_sqft = (wall_hitgh * wall_width)
gal_needed = ceil(wall_sqft / 400)
#format allows for float inset and it doesn't care about decimals
print("You need {} gallon(s) of paint".format(gal_needed))
print("It will cost you {}".format(gal_needed * cost_of_paint))

    # print("No I need your real age give em a number")
# users_age = users_age + 1
# print("So {} you will be {} next year? \n".format(users_name, users_age + 1))
# print('*' * len(users_name) + users_name + '*' * len(users_name) )
