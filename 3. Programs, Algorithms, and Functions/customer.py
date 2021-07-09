"""
The program displays a user's record
"""
'''
@brief: The function displays a user's record
@param: firstName: first name of the customer
@param: lastName: last name of the customer
@param: location(optional): location of the customer
'''
def formatCustomer(firstName, lastName, location = 'null'):
    fullName = '{} {}'.format(firstName, lastName)
    if location == 'null':
        return fullName
    else:
        return '{} ({})'.format(fullName, location)