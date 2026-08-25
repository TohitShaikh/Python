#program for swapping two integer Values
#AssignmentOperatorEx3.py
a,b=int(input('Enter The Value of a: ')),int(input('Enter the Value of b: '))

#Displaying the Original Result
print('*'*50)
print('Original Value of a is {}'.format(a))
print('Original Value of b is {}'.format(b))
print('*'*50)

#Swapping Logic -4
a=a+b
b=a-b
a=a-b

#Displaying Swapped Result
print('*'*50)
print('Swapped Value of a is {}'.format(a))
print('Swapped Value of b is {}'.format(b))
print('*'*50)
