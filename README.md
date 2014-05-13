## Day 1: Python skillz

Welcome to your first sprint! Today we'll be getting more comfortable with
Python built-in functions and data structures.

### Resources

Here are the [lecture notes](python.md) from the day's lecture.

And also Python has good documentation.
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
* lambda functions
* map, filter and reduce
* zip and enumerate
* Dictionaries
* Sets
* itertools & collections modules (some familiarity)

Test yourself with these questions:

1. What's the difference between a list and a generator? And the advantages of either?
2. What is the advantage of storing a word list in a set rather than a list?


### Assignment

There are three parts to this sprint. Part 1 is by far the longest.

#### 1. Practice with built-ins

Fill in the functions in problems.py.

These are all one-liners that use a bunch of handy built-in functions.

#### 2. Generating text

Fill in the functions `word_counts`, `associated_words` and `make_random_story`
in words.py. These will give you practice with reading files, strings and dictionaries.

Take a look at the [Collections module](https://docs.python.org/2/library/collections.html).
You may be able to use `DefaultDict` and `Counter` to simplify your code.

#### 3. Extra fun with Python

FizzBuzz is infamous for being a simple programming problem that [a lot of software
engineers struggle with](http://blog.codinghorror.com/why-cant-programmers-program/).

* Implement the function `fizzbuzz` in fizzbuzz.py. Don't worry, this is not the main point of this question.

* Modify the function definition so that the following calls all work. You should have 3 and 5 be the default parameters.
([documentation](https://docs.python.org/2/tutorial/controlflow.html#default-argument-values))

        fizzbuzz(15)                  # "FizzBuzz"
        fizzbuzz(15, fizz=4)          # "Buzz"
        fizzbuzz(15, buzz=4)          # "Fizz"
        fizzbuzz(15, fizz=6, buzz=7)  # ""

    Now in the main block you should be able to remove the 2nd and 3rd parameters.

* Look at how the main function uses `sys.argv`. You can run your program with this
command in the command line:

        python fizzbuzz.py 20

    Modify `words.py` so that you can run your program like this:

        python words.py alice.txt 200

    You'll have to import the `sys` module and use `sys.argv` ([documentation](https://docs.python.org/2/library/sys.html))

#### 4. Bonus Projects

If you're done with all the above, well done! For additional practice, choose one of these projects to implement:

* Hangman game
* Towers of Hanoi
* Number in words (312 => "three hundred and twelve")

