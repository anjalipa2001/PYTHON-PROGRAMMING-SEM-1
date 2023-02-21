#Create a string from given string where first and last characters exchanged
string=input("Enter the string :")
newstring=string[-1]+string[1:-1]+string[0]
print("New String after exchanging the first and last characters : ",newstring)