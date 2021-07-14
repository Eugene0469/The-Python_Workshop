"""
The program calculates the total amount in USD
"""
'''
@brief: The function accepts amounts in GBP and AUD currencies and calculates the total in USD currency.
@param: amount_in_aud: the amount in AUD currency
@param: amount_in_gbp: the amount in GBP currency
@retVal: total: total amount in USD currency
'''
def computeUSDTtl(amount_in_aud = 0, amount_in_gbp = 0):
    total = 0
    total += convertCurrency(amount_in_aud, 0.78)
    total += convertCurrency(amount_in_gbp, 1.29, 0.01)
    return total

'''
@brief: Function converts values from one currency to another
@param: amount: Value to be converted
@param: rate: Rate to be used to convert the amount value
@param: margin
'''
def convertCurrency(amount, rate, margin = 0):
    return amount * rate * (1 + margin)

print(computeUSDTtl(amount_in_gbp = 10))
