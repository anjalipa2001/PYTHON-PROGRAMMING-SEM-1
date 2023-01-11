l=[1,2,3,4,5,6,7]
print("The orginal list is :",l)
for i in l:
    if(i%2==0):
        l.remove(i)
print("The list after removing the even numbers is :",l)