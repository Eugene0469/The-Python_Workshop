'''
Imports
Python files typically import classes, modules and functions from other Libraries

# One can import an entire module and get access to all the functions in that module
import math
# exp returns e raised to the passed parameter value
math.exp(2)

# One can also import the function itself from the module
from math import exp
exp(2)

# One can also decide to import everything in a module. This method is not desirable
from math import *
exp(2)

# One can also rename modules or imported objects in the import statement itself
from math import exp as exponential
exponential(2)
'''
'''
This script prints the current system date
'''
# Import the datetime module
import datetime

# Print out the current date using today() property of datetime.date
print(datetime.date.today())
