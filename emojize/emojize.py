import emoji

em = input('Input: ')

str = emoji.emojize(f'Python is {em}')

print(f'Output: {str[10:]}')