# This script was written for introductory coding in python practice
# Author: Daniel Schumaker
# Date Created: 26 December 2018

"""Prompt's user to enter two numbers that must be integers, x and y, 
and then prints x to the power of y and the root-2 log of x.
"""

import numpy

# Prompt user to enter integer x
# if x is not entered as an integer, notify user of incorrect input and
# prompt them to enter x again as an integer
while True: # keep iterating until correct input
    x = input("Enter integer x: ")
    if type(x) is not int: # the user did not input correct data type
        print("Input not valid, please only enter an integer")
        continue # try again 
    else: # the user entered the correct data type (int)
        break # exit loop and proceed to entering y
# Prompt user to enter integer y
# if y is not entered as an integer, notify user of incorrect input and
# prompt them to enter y again as an integer
while True:
    y = input("Enter integer y: ")
    if type(y) is not int: # the user did not input correct data type
        print("Input not valid, please only enter an integer")
        continue # try again
    else: # the user entered the correct data type (int)
        break # exit loop and proceed to display output

print("x to the power of y is:", float(x**y)) # display x to the power of y
print("the base-2 log of x is:", float(numpy.log2(x))) # display root-2 log of x