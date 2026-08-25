#Program for deciding the word is vowel or not
#VowelorNot.py
word=input('Enter a Word: ')

#Logic
res='Vowel Word' if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word or 'A' in word or 'E' in word or 'I' in word  or 'O' in word or 'U' in word  else 'Not a Vowel Word'

#Displaying the result
print('*'*50)
print('{} is {} ' .format(word,res))
print('*'*50)