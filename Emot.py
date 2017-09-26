import random
hat_list = [' ' , ' ' , '*<L' , '*<|' , 'd' , 'C| ' , '|' , '']
eye_list = [':' , ';'  , 'B' , ':' , 'X' , '8']
nose_list = ['0' , 'O' , 'o'  , '-' , '^' , 'd']
mouth_list = ['/' , 'S' , 'l' , 'J' , 'D' , 'C' , 'E' , 'K']
print(random.choice(hat_list) + random.choice(eye_list) + random.choice(nose_list) + random.choice(mouth_list))
