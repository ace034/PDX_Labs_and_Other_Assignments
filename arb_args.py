
"""
>>> arb(1, 2, 3, 4, 5, True, None, False, 'Python')
The 9 args are: (1, 2, 3, 4, 5, True, None, False, 'Python')

>>> arb(1, None)
The 2 args are: (1, None)


>>> stats(1, 67, 88, 44, 55, 33, 44, 22, 55, 7, 88, 9, 55, 66, 44, 33, 876)
Sum: 1587
Max: 876
Min: 1
Avg: 93
Range: 875
Entries: 17

"""





import os
#this let you do the average function effectively
import statistics as s


os.system('cls' if os.name == 'NT' else 'clear')

def arb(*args):
    length_arb = len(args)
    print("The {} args are: {}".format(length_arb, args))

# def arb(*args):
#     length_arb = len(args)
#     print("The {} args are: {}".format(length_arb, arb))
#

def stats(*args):
    u_sum = sum(args)
    u_max = max(args)
    u_min = min(args)
    #this line is only capable if you have import statistics from s
    u_avg = int(s.mean(args))
    u_rng = max(args) - 1
    u_ent = len(args)

    print(
    """Sum: {}
Max: {}
Min: {}
Avg: {}
Range: {}
Entries: {}""".format(u_sum, u_max, u_min, u_avg, u_rng, u_ent))
