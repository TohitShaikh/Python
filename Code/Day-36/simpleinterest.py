#Program for calculation of Simple Interest and Total Amount ot pay
#simpleinterest.py
principle=float(input('Enter the principle amount: '))
time=float(input('Enter the time:'))
rate_of_interest=float(input('Enter the rate of interest:'))
#Calculation of Simple Amount and Total amount to pay
simple_interest=(principle*time*rate_of_interest)/100
total_amount=principle+simple_interest
print('*'*50)
print('\t\tResult of simple interest')
print('*'*50)
print('\t\tPrinciple Amount is {}'.format(principle))
print('\t\tTime is {}' .format(time))
print('\t\tRate of Interest is {}' .format(rate_of_interest))
print('\t\tSimple interest is {}'.format(simple_interest))
print('\t\tTotal amount to pay {}'.format(total_amount))
print('*'*50)