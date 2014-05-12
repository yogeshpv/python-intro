## Python lecture notes

### Lists

References with lots of examples:
* [list intro including slicing](https://docs.python.org/2/tutorial/introduction.html#lists)
* [more with list methods](https://docs.python.org/2/tutorial/datastructures.html#more-on-lists)

### Sets

Reference:
* [sets](https://docs.python.org/2/tutorial/datastructures.html#sets)

Sets are very useful if you are going to be checking membership regularly. Let's say you're building a wordlist and want to check if a string of characters is a word. If your wordlist is a Python List, it will be super slow. If it's a Python Set, it'll be fast!


### Dictionaries

Reference:
* [dictionaries](https://docs.python.org/2/tutorial/datastructures.html#dictionaries)

Dictionaries are a collection of data that is indexed by keys. They are called associative arrays or hashmaps in other languages. They are a really efficient way to store data if you'll be needing to access the data by the key.

Note that the keys must be [immutable](https://docs.python.org/2/reference/datamodel.html), so they cannot be lists, but can be strings, ints, floats or tuples.

	def word_counts(phrase):
	    d = {}
	    for word in phrase.split():
	        d[word] = d.get(word, 0) + 1
	    return d


### Collections module

Reference:
* [collections](https://docs.python.org/2/library/collections.html)

Two really useful data structures from the collections module are `Counter` and `defaultdict`.
For `Counter`, the default value is 0 for a new element. For `defaultdict`, you can set the default as is appropriate (a common use case is if the value of your dictionary is going to be a list).

See how we can rewrite the above `word_count` function using `Counter`.

	from collections import Counter

	def word_counts(phrase):
	    d = Counter()
	    for word in phrase.split():
	        d[word] += 1
	    return d


### List comprehensions

Reference:
* [list comprehensions](https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)

In Python, in may use cases we can write for loops consisely with list comprehensions.

Here is the standard way to implement a double function:

	def double_list(L):
	    result = []
	    for item in L:
	        result.append(item * 2)
	    return result

And here is how we can do it using list comprehensions:

	def double_list(L):
	    return [2 * x for x in L]

Isn't that so short and clean?

Let's say you have a 2-dimensional list that you want to flatten. Here's the old school way:

	def flatten(L):
	    result = []
	    for lst in L:
	        for x in lst:
	            result.append(x)
	    return result

	# example: flatten([[1, 2, 3], [4, 5]]) => [1, 2, 3, 4, 5]

But here's our nice list comprehension way of doing this code:

	def flatten(L):
	    return [x for lst in L for x in lst]

And one more 2-d array example:

    def double_2d_list(L):
        return [[x * 2 for x in lst] for lst in L]

    # example: double_2d_list([[1, 2, 3], [4, 5, 6]]) => [[2, 4, 6], [8, 10, 12]]

If you want to use an if statement, here's an example where we are doubling positive numbers but not negative numbers:

    [x * 2 if x > 0 else x for x in L]

### Lambda

In Python, you can use lambda to define unnamed functions. This is really useful for being able to customize `sort` and use functions like `map`, `filter` and `reduce`.

    # Sort by first element of tuple
    L = [(2, 4), (5, 3), (6, 8), (4, 1)]
	L.sort(key=lambda x: x[0])

All things you can do with list comprehensions you can also do with `map`. It's more "Pythonic" to use list comprehensions, but understanding how to write maps is key for numpy and pandas, modules we will be using heavily.

    # Double every element of a list
    def double_list(L):
        return map(lambda x: x * 2, L)

The if statement syntax is very similar to in list comprehensions. Here's the same example (double positive numbers but not negative numbers):

    map(lambda x: x * 2 if x > 0 else x, L)

You can also use `map` with already implemented functions, like `abs` (absolute value):

    L = [0, 5, -8, 9, -3, -2]
    M = map(abs, L)  # [0, 5, 8, 9, 3, 2]

The build-in `reduce` can be used to implement agregate functions. Here's an implementation of sum (if sum wasn't already implemented in python):

    def sum(L):
        total = 0
        for x in L:
            total += x
        return total

But we can do this so much quicker if we use `reduce`. Here `total` is the running total and `x` is the new element from the list.

    def sum(L):
        return reduce(lambda total, x: total + x, L)

And here's a `len` function. Note that we gave an initial value of 0. The default initial value is the first element of the list, which works fine for sum, but not for len.

    def len(L):
        return reduce(lambda total, x: total + 1, L, 0)

