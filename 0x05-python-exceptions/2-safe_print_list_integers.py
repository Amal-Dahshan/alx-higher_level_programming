#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ''' prints the first x elements of a list and only integers.
    my_list can contain any type (integer, string, etc.)
    All integers have to be printed on the same line followed by a new line
    other type of value in the list must be skipped (in silence).
    x represents the number of elements to access in my_list
    x can be bigger than the length of my_list 
    Returns the real number of integers printed
    You have to use try: / except:
    You have to use "{:d}".format() to print an integer'''
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
