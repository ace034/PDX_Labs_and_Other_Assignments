import os
system.os('clear')
cc_num = input('Enter 16-digit credit card number:\n')
# why does line 5 have to exsist?
cc_num = list(cc_num)
print(cc_num)

#did this line flip the code of the list?
check_digit = cc_num[-1]
#or did this line flip the code of the list?
new_cc1 = cc_num[:-1]
print(new_cc1)
'''
what is the differencr between xxx.reverse() xxx.reversed()
.reverse(xxx) and .reversed(xxx) and where do you use which?
'''
new_cc1.reverse()
print(new_cc1)

# I thought this was just a blank list
new_cc2 = []
#is num was a veriable or is it a callout to something
for num in range(len(new_cc1)):
#no idea what is happening here.
    if num % 2 == 0:
#I have no idea what this is suppose to mean or how to translate it
        new_cc2.append(int(new_cc1[num])*2)
'''
Something isnt getting multiplied by 2 no idea what it by
looking at the code.
 know from class but NOT BY READING it
'''
    else:
        new_cc2.append(int(new_cc1[num]))

print(new_cc2)
# another blank list
new_cc3 = []

for num2 in new_cc2:
'''
#still no idea what is happening here other than if
xxx is greater than 9. The rest might as well be noise
line 50 seems errelivant... so that means that num 3 and num 2
are different but i don't know how.
'''
    if num2 > 9:
        num3 = (num2 - 9)
        new_cc3.append(num3)
    else:
        new_cc3.append(num2)

print(new_cc3)

new_cc3 = sum(new_cc3)
print(new_cc3)
'''
# im begining to question whether or not I
know what the difference between stringas and list
'''
new_cc3 = str(new_cc3)
new_cc3 = list(new_cc3)

if check_digit == new_cc3[1]:
#this means it worked
    print('Valid!')
#if it didnt work then print this line... THIS IS THE ONLYTHING THAT MADE SINCE
else:
    print('Invalid!')
