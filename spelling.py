import os
os.system("clear")

word = input("Please give me a word to check for the I before E rule \n:")

exeptions = ["zeitgeist feisty counterfeit heifer protein freight heists reining weird deified beige beings their veiny eidetic atheist foreign schlockmeister neighbors, either aweigh feigned absenteeism, seized heightened heirloom forfeitures albeit deigned kaleidoscope ceiling weighted seismic geisha keister sleighs leisurely reimbursing sovereign receipt or surveillance of eight veiled and neighing Rottweilers herein referred their caffeinated sheik Weimaraner poltergeist wieners Pleiades"]

def ie_search(word):
    return "ie" in word.lower() or 'cie' not in word.lower()

if word in exeptions:
    print('Hmm...this word is an exception to the rule.')

if ie_search(word) == True:
    print('{} follows the i-before-e rule!'.format(word))
else:
    print('{} does NOT follow the i-before-e rule!'.format(word))
