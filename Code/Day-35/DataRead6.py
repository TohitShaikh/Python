#Program for Multiplying Two Numerical Values
#DataRead6.
print('Enter Two Values')
x=float(input())
y=float(input())
print('Multiplication ({},{}) is {}'.format(x,y,x*y))
print('----------------------------------------------------------------------')
print('Multiplication (%0.2f,%0.2f) is %0.2f '%(x,y,x*y))
print('----------------------------------------------------------------------')
print('Multiplication (%0.2f,%0.2f) is %0.2f '%(x,y,round(x*y,2)))