"""
Variable Scope
Global keyword tells Python to use the existing globally defined variable, where the default behaviour would be to define it locally in the function:
    score = 0
    def myFunc(newScore):
        score = newScore
    myFunc(100)
    print(score)
    
    The result will be 0.

    score = 0
    def myFunc(newScore):
        global score = newScore
    myFunc(100)
    print(score)
    
    The result will be 100.
Nonlocal keyword is similar to the global keyword but it does not go straight to the global definition but first looks at the closest enclosing scope, i.e., it will look one level up in the code:
    score = 0
    def myFunc():
        score = 3
        def inner():
            nonlocal score
            print(score)
        inner()
    myFunc()
    
    The result will be 3
Lambda Functions are small, anonymous functions that can be define in a simple one-line syntax:
    lambda arguments : expression
For example:
    def add_up(x,y):
        return x + y
can be re-written as:
    add_up = lambda x,y : x + y
the function is then called as follows: 
    print(add_up(2,3)
    
    The result is 5
Lambda functions can only contain a single statement
"""
# Global keyword
print("*"*20,"Global Keyword", "*"*20)
score = 0
print("Initial value for global variable score:",score)
def updateScore(newScore):
    score = newScore
updateScore(100)
print("Value of score WITHOUT using the global keyword:",score)
def updateScoreGlobal(newScore):
    global score
    score = newScore
updateScoreGlobal(100)
print("Value of score USING the global keyword:",score)

#Nonlocal keyword
print("\n"+"*"*20,"Nonlocal Keyword","*"*20)
x = 5
print("Value of global variable x:", x)
def myFunc():
    x = 3 
    print("Value of local variable x:",x)
    def inner():
        nonlocal x
        print("Value of nonlocal variable x:",x)
    inner()
myFunc()

#Lambda Function
print("\n"+"*"*20, "Lambda Functions","*"*20)
# Create a lambda function
first_item = lambda my_list: my_list[0]
# Initialize a list
pet = ['cat', 'dog', 'mouse']
# Call the function
print("lambda argument: expression = ", first_item(pet))