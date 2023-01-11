list1=[10,2,5,4,1]
list2=[2,4,6,10]
x=len(list1)
y=len(list2)
u=sum(list1)
v=sum(list2)
common= any(check in list1 for check in list2)
print("list1 =",list1)
print("list2 =",list2)
if x==y:
    print("\n whether the two lists are of same Length : Yes")
else:
    print("\n whether the two lists are of same Length : No")
if u==v:
    print("\n whether the sum of first list is equal to the sum of seconnd list : Yes")
else:
    print("\n whether the sum of first list is equal to the sum of seconnd list : No")
if common:
    print("\n Whether the two lists have Same Elements are in common : Yes")
else :
    print("\n Whether the two lists have Same Elements are in common : No")
