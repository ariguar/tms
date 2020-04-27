print('Enter your phrase or number: ')
phrase = input()
reverse_phrase = phrase[::-1]
print('Is it palindrome?')
if phrase == reverse_phrase:
    print('YES!')
else:
    print('NO')