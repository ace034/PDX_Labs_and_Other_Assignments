import os
Grade = input('Please type your in your grade "Grade"\n:')
while int(Grade) not in range(0, 111):
    Grade = ('Please type "Grade"\n:')
Grade = int(input('Type in your grade\n:'))
os.system('clear')
#Grade input_list (range 0:110)
if Grade <= 59 and Grade >= 0:
        print('You got an F I award you no points and may God have mercy on your soul')
if Grade >= 60 and Grade <= 69:
        print('You got an D I award you few points next time study more')
if Grade >= 70 and Grade <= 79:
        print("You got a C if thats as far as you go you should be proud of that")
if Grade >= 80 and Grade <= 89:
        print("You got a B I think you should take that home and show your parents")
if Grade >= 90 and Grade <= 100:
        print('You are worthy of my time and teaching')
if Grade >= 101 and Grade <= 110:
        print("You are either cheating or really good either way I'm impressed")
