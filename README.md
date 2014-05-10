## Day 1: Python skillz

Welcome to your first sprint! Today we'll be getting more comfortable with
Python built-in functions and data structures.

### Resources

Python has good documentation.
The [Python tutorial](https://docs.python.org/2/tutorial/) and
[Python library](https://docs.python.org/2/library/) are great resources if
you need to look up how something is done in Python.

Here are a few pages that may be particularly
useful to you as you're working through today's exercise:
* [Data Structures](https://docs.python.org/2/tutorial/datastructures.html):
[lists](https://docs.python.org/2/tutorial/datastructures.html#more-on-lists)
(particularly map, filter and list comprehensions) and
[dictionaries](https://docs.python.org/2/tutorial/datastructures.html#dictionaries)
* [Strings](https://docs.python.org/2/library/string.html): particularly
strip and split


### Goals

After today, you should be comfortable with these topics in python:
* Functions
* Lists
* List comprehensions
* map and filter
* Dictionaries


### Assignment

#### 1. Practice with lists

Fill in the functions in problems.py.

These are all one-liners that use list comprehension, map and filter.

#### 2. Generating text

Fill in the functions `word_counts`, `associated_words` and `make_random_story`
in words.py. These will give you practice with reading files, strings and dictionaries.

#### 3. Extra fun with Python

FizzBuzz is infamous for being a simple programming problem that [a lot of software
engineers struggle with](http://blog.codinghorror.com/why-cant-programmers-program/).

* Implement the function in `fizzbuzz.py`.

* Make note of how the default and keyword parameters work. What will all of these
calls do?
([documentation](https://docs.python.org/2/tutorial/controlflow.html#default-argument-values))

        fizzbuzz(12)
        fizzbuzz(12, buzz=4)
        fizzbuzz(12, fizz=5, buzz=7)

* Look at how the main function uses `sys.argv`. You can run your program with this
command in the command line:

        python fizzbuzz 20

    Modify `words.py` so that you can run your program like this:

        python words.py alice.txt 200

You'll have to import the `sys` module and use `sys.argv` ([documentation](https://docs.python.org/2/library/sys.html))

#### 4. Bonus Projects

If you're done with all the above, well done! For additional practice, choose one of these projects to implement:

* Hangman game
* Towers of Hanoi
* Number in words (312 => "three hundred and twelve")

