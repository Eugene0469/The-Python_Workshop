"""
The program computes the elements of the Fibonacci sequence
"""
'''
@brief: Function computes elements of a fibonacci sequence
@param: n: the number term in the sequence that we want to return
@retVal: result: the number of position n in the fibonacci sequence
'''
def fibonacciIterative(n):
    previous = 0
    current = 1 
    for i in range(n-1):
        current_old = current
        previous, current = current_old , current + previous
    return current

'''
@brief: Function computes elements of a fibonacci sequence
@param: n: the number term in the sequence that we want to return
@retVal: result: the number of position n in the fibonacci sequence
'''
def fibonacciRecursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacciRecursive(n-2) + fibonacciRecursive(n-1)
    
# Declare a dictionary to store the fibonacci series vales and set hte first 2 terms of the Fibonacci sequence
storedValues = {0:0,1:1}
'''
@brief: Function computes elements of a fibonacci sequence
@param: n: the number term in the sequence that we want to return
@retVal: result: the number of position n in the fibonacci sequence
'''
def fibonacciDynamic(n):
    # Check to see if the value is already stored in the dictionary
    if n in storedValues:
        return storedValues[n]
    else:
        storedValues[n] = fibonacciRecursive(n-2) + fibonacciRecursive(n-1)
        return storedValues[n]
    
    
    