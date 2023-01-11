#Create a string from given string where first and last characters exchanged.
text = input('Enter a string: ')
newtext = text[-1]+text[1:-1]+text[0]
print('New string after the first and last characters exchanged :', newtext)
