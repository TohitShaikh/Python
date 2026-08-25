#Program for finding biggest of two number by using ternary operator
#BigTwoEx1.py
a=int(input('Enter First Value: '))
b=int(input('Enter Second Value: '))
#Logic for big
big_value= a if a>b else b
#Displaying the result
print('*'*50)
print('Biggest Value between {} & {} is {}'.format(a,b,big_value))
print('*'*50)