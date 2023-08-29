#!/usr/bin/python3

# safe_print_list -  prints x elements of a list
#  Returns: The number of elements printed.

def safe_print_list(my_list=[], x=0):
     count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
