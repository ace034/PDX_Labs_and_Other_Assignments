"""

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bannanas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]
"""

import os
os.system("clear")


char_to_locate = input('What is the and charactor you want me to find? \n:').lower()
word = input('What is you want me to find? \n:').lower()

if char_to_locate in word:
    print([pos for pos, char in enumerate(word) if char == char_to_locate])

if char_to_locate not in word:
    print("I don't see that letter")
