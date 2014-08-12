# Python Terminal

We recommend using `ipython` rather than the standard python terminal to test out your code. Here are some cool things you can do with `ipython`:

1. Press UP to cycle back through previous commands.

1. Use `_` for a variable containing the result of the last executed command:

    ```python
    In [1]: 9 * 54
    Out[1]: 486

    In [2]: _
    Out[2]: 486

    In [3]: x = _

    In [4]: x
    Out[4]: 486
    ```

1. You can re-run a line you've already run:

    ```python
    In [10]: exec _i6
    ```

    This will run the code in line 6.

1. You can edit the line before you re-run it:

    ```python
    In [11]: %rep 6
    ```

1. This will run python code from a file:

    ```python
    In [1]: %run example.py
    ```

1. You can paste text using this:

    ```python
    In [2]: %paste
    ```

1. You can edit a function that you've already defined:

    ```python
    In [3]: %edit foo
    ```

    It will open in your chosen editor (defaults to vi)


# Advanced Python

This is a bunch of syntax and special tools that are available in python that come in very handy.

## Generators

First look at this bit of code:

```python
for i in range(1000):
    print i
```

The `range` function will create a list of length 1000 and then we iterate over it. This is very wasteful for space! We don't need to create a list of 1000 elements and store it in memory! We can use a *generator* to save the memory:

```python
for i in xrange(1000):
    print i
```

The `xrange` function will generate the next value when it's needed, but won't pre-generate everything like the `range` function.

You'll see other examples of generators below.


## Looping tools

There are a couple handy tools in python that help you clean up your code when you're looping through a list. First, when possible, use the most simple pythonic loop:

```python
for item in L:
    print item
```

### Enumerate

If you need to know the index, you've probably seen code like this:

```python
for i in xrange(len(L)):
    print i, L[i]
```

But you should really use `enumerate` (a generator!):

```python
for i, item in enumerate(L):
    print i, item
```

Isn't that cleaner?


### Zip

Let's say you have two lists and you want to loop over both of them at the same time. You could do this:

```python
first_names = ['Giovanna', 'Ryan', 'Jon']
last_names = ['Thron', 'Orban', 'Dinu']

for i in xrange(len(first_names)):
    print first_names[i], last_names[i]
```

But python has a handy `zip` function to zip two lists together:

```python
In [3]: zip(first_names, last_names)
Out[3]: [('Giovanna', 'Thron'), ('Ryan', 'Orban'), ('Jon', 'Dinu')]
```

If you're going to loop over it, you should use `izip` instead, since it's a generator. You'll need to import `izip` from the `itertools` module.

```python
from itertools import izip

for first, last in izip(first_names, last_names):
    print first, last
```


## List comprehensions

For simple things, you can do your for loop on one line. Let's say you want to create a new list that has all the items from the first list doubled. You could do this:

```python
doubled = []
for item in L:
    doubled.append(item)
```

But using a list comprehension, you can do this:

```python
doubled = [item * 2 for item in L]
```

### 2D list comprehensions

You can similarly do a double for loop. This is what it would look like the standard way:

```python
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
doubled = []
for row in L:
    row = []
    for item in row:
        row.append(item * 2)
    doubled.append9=(row)
```

And with a list comprehension:

```python
doubled = [[item * 2 for item in row] for row in L]
```

And if you wanted to flatten a 2-dimesionsional list:

```python
In [1]: L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

In [2]: [item for row in L for item in row]
Out[2]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Note the order of the loop statements.


### If statements in list comprehensions

If statements have a weird syntax in a list comprehension:

```python
In [3]: L = [4, 6, 3, 2, 5]

In [4]: ["even" if item % 2 == 0 else "odd" for item in L]
Out[4]: ['even', 'even', 'odd', 'even', 'odd']
```

You can also use an if statement as a filter, to only include some of the items. Here we include only the even numbers:


### Generator comprehensions

You can make it a generator instead of a list if you're just going to be looping over the result anyways. You do this by using round brackets instead of square ones:

```python
L = [("giovanna", "thron"), ("ryan", "orban"), ("jonathan", "dinu")]
for name in (L[0] for item in L):
    print name
```


## Lambda Functions

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


## Sets and Dictionaries


## Counter and defaultdict


## File input


## Exception Handling


## Python style


    