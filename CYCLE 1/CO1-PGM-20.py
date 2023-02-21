#From a list of integers, create a list removing even numbers
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    if i%2==0:
        list.remove(i)
print("The new list after Removing the Even numbers :",list)