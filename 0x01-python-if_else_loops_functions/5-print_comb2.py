#!/usr/bin/python3
# prints numbers from 0 to 99.
# Numbers must be separated by ( ,) followed by a space
# Numbers should be printed in ascending order, with two digits
# The last number should be followed by a new line
# You can only use no more than 2 print functions with string format
# You can only use one loop in your code
for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")
