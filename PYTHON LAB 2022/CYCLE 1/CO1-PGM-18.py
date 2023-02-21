#Merge two dictionaries.
dic1={"Name:Anakha","Age:21"}
dic2={"DOB:03-08-2001","Gender:Female"}
print("Dictionary 1 : ",dic1)
print("Dictionary 2 : ",dic2)
d=dic1.copy()
d.update(dic2)
print("After Merging :",d)