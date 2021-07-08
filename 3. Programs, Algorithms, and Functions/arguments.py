"""
Arguments
Example: 
    def function(a, b):
    return a / b
Positional Arguments.
Order of the passed paramenters matters
function(1,2) returns a different value as compared to function(2,1)

Keyword arguments
One can assign values directly to a function's arguments and therefore the order in which the parameters are passed does not matter.
function(a=1,b=2) returns the SAME value as function(b=2,a=1)

NOTE: One can have both position and keyword arguments in a function definition. However, positional arguments should always come before keyword arguments
function(1, b = 2)
The rule of thumb is to simply use positional arguments for required inputs that must be provided each time the function is called, and keyword arguments for optional inputs.

*args and 8**kwargs Arguments
They allow one to pass any number of arguments
*args allows you to pass any number of non-keyworded arguments
**kwargs allows you to pass any number of keyworded arguments that can then be accessed in a dictionary called kwargs
"""

PSTNL_KW_ARG = False
ARG_KWARG = True

if PSTNL_KW_ARG:
    print('*'*20,'Positional & Keyword Arguments','*'*20,'\n')
    '''
    @brief: Converts US dollar to Australian dollar
    @param: amount: value in USD to be converted
    @param: rate: rate of conversion from USD to AUD
    '''
    def convertUSDToAUD(amount, rate = 0.75):
        return amount / rate

    print("Rate is not passed as a parameter:",convertUSDToAUD(100))
    print("Rate is passed as an parameter:",convertUSDToAUD(100, 0.78))
    print("-"*40)

if ARG_KWARG:
    print('*'*20,'*args & **kwargs Arguments','*'*20,'\n')
    print("-"*10,"*args Argument","-"*10)
    '''
    @brief: Provides the sum of the values passed to it
    @param: *args: allows us to pass any number of values to sum up.
    @retVal: total: the total sum of the numbers
    '''
    def sumOfNumbers(*args):
        total = 0
        for number in args:
            total += number
        return total
    print('Using *args to pass values, sumOfNumbers(1,2,3,4,5):',sumOfNumbers(1,2,3,4,5))
    
    print("\n","-"*10,"**kwargs Argument","-"*10)
    '''
    @brief: Allows us to print out an undefined number of personal information
    @param: **kwargs: the information to be printed out
    '''
    def personalDetails(**kwargs):
        print("Personal Details")
        for key in kwargs:
            print('{} : {}'.format(key, kwargs[key]))
    
    # Passing values using keyword arguments
    print("Passing values using keyword arguments")
    personalDetails(firstName = "Eugene", lastName = "Mwangi", country = "Kenya")
    print("\nVarying the keyword")
    personalDetails(name = "Abigael", school = "JKUAT", age = "23")
    
    # Passing values using a dictionary
    print("\nPassing values using a dictionary(personalDetails(**inputDict))")
    # Initiailize the dictionary
    inputDict = {
        'name' : "Rose",
        'gender' : "Female"
    }
    personalDetails(**inputDict)
