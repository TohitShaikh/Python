#Program for finding biggest of two number and check for equality by using ternary operator
#BigTwoEx2.py
a=int(input('Enter First Value: '))
b=int(input('Enter Second Value: '))
#Logic for finding bigger and equal value
res=a if a>b else b if b>a else 'Both the values are same'
#Displaying the result
print('*'*50)
print('Biggest Value between ({},{}) is {}'.format(a,b,res))
print('*'*50)