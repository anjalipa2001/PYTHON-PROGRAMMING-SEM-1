#Count the number of characters (character frequency) in a string.
strg=input("Enter the word ")
c=0
for i in strg:
    if i==" ":
        continue
    else:
        c+=1
print(c,"the characters in "+strg)
            