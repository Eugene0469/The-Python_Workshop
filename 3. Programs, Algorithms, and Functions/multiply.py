"""
Functions
"""
'''
@brief: Multiplies the numbres in a list with each other
@param: myList: a list of hte numbers to be multiplied
@retVal: result: final multiplication value
'''
def listProduct(myList):
    result = 1
    for number in myList:
        result = result * number
    return result

if __name__ == '__main__':
    print('List product',[2,3],'=',listProduct([2,3]))
    print('List product',[2,10,15],'=',listProduct([2,10,15]))