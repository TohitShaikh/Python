#Program for Swapping two Values
#SwapLogic.py
a=input('Enter the Value of a:')
b=input('Enter the Value of b:')
print('*'*50)
print('Original Value of a {}'.format(a))
print('Original Value of b {}'.format(b))
print('-'*50)
#Swapping Logic
k=a #Here k is temporary Variable
a=b
b=k
print('Swapped Value of a is {}'.format(a))
print('Swapped Value of b is {}'.format(b))
print('*'*50)