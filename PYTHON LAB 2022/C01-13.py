#Create a list of colors from comma-separated color names entered by user. Display first and lastcolors.
list=[]
input_string=input("Enter the colors :")
l=input_string.split()
print("The list is:",l)
print("The first and last color :",(l[0],l[-1]))