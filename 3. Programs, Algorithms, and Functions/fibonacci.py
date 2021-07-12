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