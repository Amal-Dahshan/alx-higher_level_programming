#!/usr/bin/python3
# imports the function def add(a, b): from the file add_0.py
# and prints the result of the addition 1 + 2 = 3
# You can only use the word add_0 once in your code
# You are not allowed to use * for importing or __import__
# Your code should not be executed when imported - by using __import__

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
