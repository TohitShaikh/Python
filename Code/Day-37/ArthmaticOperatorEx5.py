#Program for implementing the formula A to power m / A to the power n
#ArthmaticOperatorEx5.py
a=float(input("Enter the Value of a: "))
m=float(input("Enter the value of m: "))
n=float(input("Enter the Value of n: "))

#Applying the formula
logic1=(a**m)/(a**n)
logic2=a**(m-n)

#Displaying the result
print('*'*50)
print('The value of logic1 is {}'.format(logic1))
print('The value of logic2 is {}'.format(logic2))
print('*'*50)