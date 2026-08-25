#Program which will accept numerical integer val or float value and decide whether it is even or odd
#Even-Odd.py
n=int(input('Enter a Number: '))

#Logic for finding odd or even number
res= 'Even' if n%2==0 else 'Odd'

#Displaying the result
print('*'*50)
print('{} is {}'.format(n,res))
print('*'*50)