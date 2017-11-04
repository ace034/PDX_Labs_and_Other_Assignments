"""

>>> combine(7, 4)
11

>>> combine(42)
42

>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney")
'Rooney'

>>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""
def combine(*args):
    u_sum = sum(args)
    return u_sum

def combine_many(*args):
    u_sum = sum(args)
    return u_sum

def choose_longest(*args):
    longest = None
    cur_len = 0
    for item in args:
        if len(item) > longest:
            cur_len = len(item)
            longest = item
    return longest
