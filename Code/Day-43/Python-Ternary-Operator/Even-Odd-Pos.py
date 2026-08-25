#Program which will accept numerical integer val or float value and decide whether it is even or odd with Positive Number
#If User enter Negative Number then display Invalid Input
#Even-Odd-Pos.py
n=int(input('Enter a Number: '))

#Logic for finding odd or even number positive number
res= 'Invalid Input' if (n<0) else 'Even' if n%2==0 else 'Odd'

#Displaying the result
print('*'*50)
print('{} is {}'.format(n,res))
print('*'*50)