'''
Python Scripts and Modules

A script is a file that is designed to be executed, usually from the command line
A module is usually imported into another part of the code or an interactive shell 
to be executed.

The script below uses the math.factorial function and list comprehension to compute
for the sum of the factorials of numbers stored in a list
'''
import math

# Initialize a list of numbers
numbers = [5, 7, 11]

# Find the sum of the factorials of the numbers
result = sum([math.factorial(n) for n in numbers])
print("{}! + {}! + {}! = {}".format(numbers[0],numbers[1], numbers[2], result))