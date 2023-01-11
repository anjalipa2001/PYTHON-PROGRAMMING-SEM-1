#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’
strg=input("Enter the string ")
if strg.endswith('ing'):
    strg+='ly'
elif len(strg)>=3:
    strg+='ing'
print(strg)