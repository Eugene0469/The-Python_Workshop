"""
Iterative Functions
"""
'''
@brief: Sums up the first n integers.
@param: n: integer value
'''

def sumFirstN(n):
    result = 0
    for i in range(n):
        result += i + 1
    return result

'''
@brief: Checks if a number greater than 2 is a prime number
@param: num: number to check
@retVal: returns True or False
'''
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


number = int(input("Enter a number: \n"))
print("sum = ", sumFirstN(number))
if isPrime(number):
    print('{} is a Prime Number'.format(number))
else:
    print('{} is not a Prime Number'.format(number))
