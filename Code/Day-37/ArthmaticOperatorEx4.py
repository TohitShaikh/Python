#program which will evaluate (a+b)2
a=float(input("Enter the Value of a: "))
b=float(input("Enter the Vallue of b: "))

#Applying the formula with various logic
logic1=(a+b)**2
logic2=(a+b)*(a+b)
logic3=a**2+2*a*b+b**2


#Displaying the result
print('*'*50)
print('Answer with logic 1 is {}'.format(logic1))
print('Answer with logic 2 is {}'.format(logic2))
print('Answer with Logic 3 is {}'.format(logic3))
print('*'*50)