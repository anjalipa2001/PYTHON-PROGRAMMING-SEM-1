#store a list of first names count the occurences of 'a' within the list
names=["anjali","amrutha","Reshma","Sam"]
count=0
for name in names:
    count=count+name.count('a')
print("Occurence of 'a' in the name list is :",count)
