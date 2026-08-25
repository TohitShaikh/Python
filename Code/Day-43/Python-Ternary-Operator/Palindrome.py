#program accepting a word or balue and decinding whether a word is palindrome or not
#Palindrome.py
value=input('Enter a Value: ')

#Logic for checking palindrome
res= 'Palindrome' if value==value[::-1] else 'Not Palindrome'

#Displaying the Result
print('*'*50)
print('{} is {} ' .format(value,res))
print('*'*50)