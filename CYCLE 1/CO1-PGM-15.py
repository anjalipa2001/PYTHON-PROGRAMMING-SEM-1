#Print out all colors from color-list1 not contained in color-list2.
color_list1=set(["green","red","pink","black","blue","white"])
color_list2=set(["pink","yellow","blue","black"])
s=color_list1.difference(color_list2)
print("All colors from color-list1 not contained in color-list2 : ",s)