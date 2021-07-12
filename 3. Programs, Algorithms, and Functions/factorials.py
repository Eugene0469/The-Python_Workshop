"""
The program computes the factorial of a number using iterative and recursive approaches
"""
'''
@brief: Computes the factorial of a number iteratively
@param: num: factorial number
@retVal: res: factorial result
'''
def factIter(num):
    res = 1
    for i in range(num):
        res *= i+1
    return res
'''
@brief: Computes the factorial of a number recursively
@param: num: factorial number
@retVal: res: factorial result
'''
def factRec(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factRec(num-1)

number = int(input("Enter number: "))
print("(Iterative)Factorial of " + str(number) + " is:", factIter(number)) 
print("(Recursive)Factorial of " + str(number) + " is:", factRec(number)) 