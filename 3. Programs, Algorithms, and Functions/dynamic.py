"""
The program calculates for the sum of n terms dynamically
"""
import time
# Declare a dictionary to store our results
storedResult = {}

'''
@brief: Computes the sum of n integers
@param: n: number of integers
@retVal: result: sum of integers upto n
'''
def sumToN(n):
    startTime = time.perf_counter()
    result = 0;
    for i in reversed(range(n)):
        # Check if the value has already been computed
        if i+1 in storedResult:
            print("Result of %s has already been computed"%str(i+1))
            result += storedResult[i+1]
            break
        else:
            result += i+1
    storedResult[n] = result
    print(time.perf_counter() - startTime, "seconds")
    return result
     