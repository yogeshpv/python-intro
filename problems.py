### Fill in each function below. Each function should be a one-liner.

def sort_rows(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: 2 dimensional list of integers (matrix)

    Use list comprehension to modify each row of the matrix to be sorted.

    Example:
    >>> M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    >>> sort_rows(M)
    >>> M
    [[2, 4, 5, 8], [3, 6, 7, 9]]
    '''
    pass

def average_rows1(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Use list comprehension to take the average of each row in the matrix and
    return it as a list.

    Example:
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    pass

def average_rows2(mat):
    '''
    INPUT: 2 dimensional list of integers (matrix)
    OUTPUT: list of floats

    Use map to take the average of each row in the matrix and
    return it as a list.
    '''
    pass

def word_lengths1(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers

    Use list comprehension to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Example:
    >>> word_lengths1("Welcome to Zipfian Academy!")
    [7, 2, 7, 8]
    '''
    pass

def word_lengths2(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers

    Use map to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.
    '''
    pass

def filter_words(word_list, letter):
    '''
    INPUT: list of words, string
    OUTPUT: list of words

    Use filter to return the words from word_list which start with letter.

    Example:
    >>> filter_words(["salumeria", "dandelion", "yamo", "doc loi", "rosamunde",
                      "beretta", "ike's", "delfina"], "d")
    ['dandelion', 'doc loi', 'delfina']
    '''
    pass

def factors(num):
    '''
    INPUT: integer
    OUTPUT: list of integers

    Use filter to return all of the factors of num.
    '''
    pass

def acronym(phrase):
    '''
    INPUT: string
    OUTPUT: string

    Given a phrase, return the associated acronym by breaking on spaces and
    concatenating the first letters of each word together capitalized.

    Example:
    >>> acronym("zipfian academy")
    'ZA'

    Hint: You can do this on one line using list comprehension and the join
    method. Python has a builtin string method to uppercase strings.
    '''
    pass
