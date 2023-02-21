#Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums to same value (c) whether any value occur in both 
list1=[2,3,4,5]
list2=[6,7,8,9,4]
print("List 1 =",list1)
print("List 2 =",list2)
if len(list1)==len(list2):
    print("Both lists have same Length")
else:
    print("Both lists have different Length")
if sum(list1)==sum(list2):
    print("Both lists have same sum")
else:
    print("Both lists have different sum")
    for item in list1:
        if item in list2:
            print("Both lists have the same item : ",item)
       