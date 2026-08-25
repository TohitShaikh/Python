#Program which will accept numerical integer value and decide whether it Positive Negative or Zero
#Pos-Neg-Zero.py
n=int(input('Enter a Number: '))

#Logic
res='Zero' if (n==0) else 'Positive Number' if n>0 else 'Negative Number'

#Displaying the result
print('*'*50)
print('{} is {}'.format(n,res))
print('*'*50)