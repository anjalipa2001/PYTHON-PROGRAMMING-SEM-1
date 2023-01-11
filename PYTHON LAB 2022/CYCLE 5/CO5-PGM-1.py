f=open("text1.txt","r")
'''lines=f.readlines()
l1=[line.strip() for line in lines]
print(l1)'''
f1=f.readlines()
for x in range(0,len(f1)):
    print(f1[x])
f.close()
#print([line.strip() for line in open("text1.txt","r")])