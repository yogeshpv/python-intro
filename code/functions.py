from collections import Counter
from itertools import izip, count


def write_to_file(lst, f):
    """
    INPUT: list, open file object
    OUTPUT: None

    Write the list to the file with line numbers, starting at 1.
    INPUT: ["a", "b", "c"]
    FILE CONTENTS:
    1 a
    2 b
    3 c

    Hint: Use enumerate for cleaner code
    """
    for i,v in enumerate(lst):
        f.write(str(i+1) + ' ' + str(v) + '\n')




def merge_files(f1, f2, out):
    """
    INPUT: open file, open file, open file
    OUTPUT: None

    f1 and f2 are two files with the same number of lines. Merge the contents
    together, separated with a comma.

    INPUT FILES:
    cat
    dog

    mouse
    rabbit

    OUTPUT FILE:
    cat,mouse
    dog,rabbit

    Hint: Use izip
    """
    l1 = f1.readlines()
    l2 = f2.readlines()

    for a,b in izip(l1,l2):
        out.write(a.rstrip('\n') + ',' + b)



def key_in_value(d):
    """
    INPUT: dict
    OUTPUT: list

    Return the keys from the dictionary where the key is a member in the
    associated value.

    example:
    INPUT: {"a": ["b", "c", "a"], "b": ["a", "c"], "c": ["c"]}
    OUTPUT: ["a", "c"]

    Hint: Use iteritems
    (Can be done on one line with a list comprehension)
    """
    return [k for k,v in d.iteritems() if k in v]



def most_common_letters(sentence):
    """
    INPUT: string
    OUTPUT: list of strings

    Given a sentence, give the most common letter for each word.
    You should lowercase the letters. If there's a tie, include any of them.

    example:
    INPUT: "Welcome to Zipfian Academy!"
    OUTPUT: 'e t i a'

    Hint: use Counter and the string join method
    (It is possible to do this in one line, but you might lose some
    readability)
    """
    
    return ' '.join([i[0] for i in [sorted(Counter(words),key=Counter(words).get,reverse=True) for words in sentence.lower().split(' ')]])

def merge_dictionaries(d1, d2):
    """
    INPUT: dict (string => int), dict (string => int)
    OUTPUT: dict (string => int)

    example:
    INPUT: {"a": 2, "b": 5}, {"a": 7, "c":10}
    OUTPUT: {"a": 9, "b": 5, "c": 10}

    Create a new dictionary that contains all the key, value pairs from d1 and
    d2. If a key is in both dictionaries, sum the values.
    """
    k1 = set(d1.keys())
    k2 = set(d2.keys())

    sumDict = {}
    newDict = d1.copy()
    common_keys = list(k1 & k2)
    for k in common_keys:
        sumDict[k] = d1[k] + d2[k]

    newDict.update(d2)
    newDict.update(sumDict)

    return newDict