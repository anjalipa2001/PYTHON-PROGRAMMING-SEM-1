#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
n=int(input("Enter the number of elements : "))
list2=[]
for number in range(n):
    number=int(input("Enter the number :"))
    if number>100:
        list2.append('over')
    else:
            list2.append(number)
print("The output is ",list2)