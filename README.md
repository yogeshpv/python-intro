## Python skillz

We'll be getting more comfortable with Python built-in functions and data structures.

The course will heavily use Python for most of its analyses/projects.  It is not
necessary to be an expert in Python coming into the course (that is what we will
teach you!) but it is helpful to be familiar with it's syntax.

Not everyone knows Python (or what parts to focus on it in the classroom).  We
have provided resources here to get any student familiar with another
programming language up to speed with Python quickly (both in terms of syntax
and style). 

## Installing

We use the [Anaconda](https://store.continuum.io/cshop/anaconda/) Python 2.7
(not Python 3) distribution and use [conda](http://www.continuum.io/blog/conda)
to install any additional packages. You should install Anaconda now.

## Python Terminal
Run `python` from a terminal, and you'll get to a Python
terminal where you can test out Python interactively.
You can exit with control-D or `exit`.

There's a better terminal called IPython. Run `ipython` to enter it.

Within the IPython terminal, you can type "`%run <filename>`"
to effectively copy the contents of a file into the terminal.

    In [1]: %run example.py
    
    In [2]: example()
    Hi

You can do something quite similar from an ordinary shell. If you write 
some Python code in a file, then run `python filename.py`, the same thing
happens, except that the Python session ends right after the file is run;
that is, it's as if you copied the contents of the file into the terminal
and then closed the terminal.

### `import`

You load other python files with `import`.  You can use this to load other
files.

    In [1]: import example
    
    In [2]: example.example()
    Hi
    

You can also use this to load system-wide libraries.

    In [1]: import string
    
    In [2]: print string.ascii_letters
    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    
## Assignment

#### 0. Python Basics

1. Go through the [Python tutorial](http://inst.eecs.berkeley.edu/~cs188/sp12/projects/tutorial/tutorial.html) and submit `buyLotsOfFruit.py` and `shopSmart.py`.

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

#### 5. Pandas

Resources:

* [10 Minutes to Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)
* [Pandas top 10](http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/)

Pandas can be a very frustrating and mysterious library, it will be essential to get familiar with its quirks early on.

1. Complete the [pandas workshop](http://nbviewer.ipython.org/github/jvns/talks/blob/master/pydatanyc2013/PyData%20NYC%202013%20tutorial.ipynb) ([video](https://vimeo.com/79835526))

#### 4. Bonus Projects

If you're done with all the above, well done! For additional practice, choose one of these projects to implement:

* Hangman game
* Towers of Hanoi
* Number in words (312 => "three hundred and twelve")

## What you should know

### Python

* Basic data structures and associated methods
  * int, float
  * string
  * list
  * dict
  * set
  * range
* Control structures
  * if, elif, else
  * while
  * for
  * break, continue, pass
* Enumerations
  * for loops
  * list comprehensions
  * enumerate
  * zip
* Functions
  * Declaration
  * Calling
  * Keyword arguments
* Object orientation
  * Classes
  * Methods
  * Properties (instance variables)
  * self
* Modules
  * import
  * aliasing (`import pandas as pd`)
  * global import (`from pandas import *`)
* IO
  * Read a file
  * Write to a file

Test yourself with these questions:

1. What's the difference between a list and a generator? And the advantages of either?
2. What is the advantage of storing a word list in a set rather than a list?

### NumPy

The NumPy workhorse is the `array` which is a high-performance matrix.

Think in matrices and matrix manipulation. Anything that can be vectorized
should be vectorized.

* Create: ones, zeros, eye, empty, random.random, random.randn
* size, shape, ndim
* min, max, mean, var
* Matrix multiplication
* Indexing, slicing, boolean indexing
* Broadcasting
* `np.linalg`: inv, det, solve, eig

### Pandas

* Series
* DataFrame
* Indexing, slicing, boolean indexing
* Broadcasting

### Resources

Here are the some [notes](python.md) on Python.

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

## References
No need to read these -- use them to look up things you encounter that you don't
know.

* [Python introduction](http://docs.python.org/2/tutorial/introduction.html)
* [Intro to Python notebook](http://nbviewer.ipython.org/urls/bitbucket.org/amjoconn/watpy-learning-to-code-with-python/raw/3441274a54c7ff6ff3e37285aafcbbd8cb4774f0/notebook/Learn%20to%20Code%20with%20Python.ipynb)
* [Python Docs](http://docs.python.org/2/)
* [IPython docs](http://ipython.org/ipython-doc/rel-0.13.1/index.html)
* [Think Python](http://www.greenteapress.com/thinkpython/thinkpython.pdf)
* [Intro to Pandas Data Structures](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro)
* [Scipy Lectures](http://scipy-lectures.github.io/)
* [Scikit-learn tutorial](https://github.com/jakevdp/sklearn_pycon2014)
* [Berkeley Python bootcamp](http://www.pythonbootcamp.info/schedule)


