#Program for Multiplying Two Numerical Values
#DataRead3.py
a=input('Enter First Value:')
b=input('Enter Second Value:')
#Here a,b are of type str so we need to convert it into float type.
x=float(a)
y=float(b)
#Multiply
z=x*y
print('Multiplication({},{}) is {}'.format(x,y,z))