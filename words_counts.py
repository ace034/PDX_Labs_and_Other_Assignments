# Open the file and deal with any decoding errror that arise.--
import os
from string import punctuation
from operator import itemgetter
os.system('cls' if os.name == 'NT' else 'clear')
def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as whatever:
        lines = whatever.read()
    return(lines)


# Normalize all of the words so differences in capitalization and
def cleaned_wordlist(doc_string):
    cleaned_doc = ""
    trash = list(punctuation) + ['\n']
    for char in doc_string:
        if char not in trash:
            cleaned_doc += char
# punctuation attached to words don’t affect the counts.

    return [word for word in cleaned_doc.split() if len(word) > 0]

doc = open_file('pg120.txt').lower()
cleaned_doc = cleaned_wordlist(doc)
print(cleaned_doc)

# Count how often each unique word is used, then print the most frequent
 # top 10 out with their counts.
def find_top_ten_n(wrd_lst, n=10):
    word_dict = {}
    for word in wrd_lst:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    counted_word_list = word_dict.items()
    return sorted(counted_word_list, key=itemgetter(1), reverse=True)[:n]


for item in find_top_ten_n(cleaned_doc):
    print(item[0], item[1])
# print(find_top_ten_n(cleaned_wordlist))
# Count how often each unique pair of words is used,
# then print the most frequent top 10 out with their counts.
