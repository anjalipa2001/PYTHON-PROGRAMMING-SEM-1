#Create a single string separated with space from two strings by swapping the character at position 1.
str1=input("Enter the first string : ")
str2=input("Enter the second string : ")
x=str1[0:1]
str1=str1.replace(str1[0:1],str2[0:1])
str2=str2.replace(str2[0:1],x)
print("New string after swapping : ",str1,str2)