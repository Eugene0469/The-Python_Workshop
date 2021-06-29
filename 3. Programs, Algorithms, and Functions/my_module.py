'''
We shall create a module and import it into a python shell

Shebangs in Ubuntu
#!/usr/bin/env python: for unix systems(Ubuntu, macOS X), this path specifies the
program that the computer should use to execute the file
'''
import math

'''
@brief Computes for the factorials of numbers stored in a list
@param numbers: the list of numbers
@return Returns a list of the resulting factorials
'''
def compute(numbers):
    return([math.factorial(n) for n in numbers])