#Print out all colors from color-list1 not contained in color-list2.
color_list1=["red","green","black","blue","pink","navyblue"]
color_list2=["violet","black","red","blue"]
diff = [x for x in color_list1 if x not in color_list2]
print("All colors from color-list1 not contained in color-list2 : ",diff)