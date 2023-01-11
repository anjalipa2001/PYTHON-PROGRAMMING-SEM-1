# Python program to copy odd lines of one file to other 
f=open("text1.txt","r")
f1=open("text2.txt","w")
lines=f.readlines()
for i in range(0,len(lines)):
    if i%2!=0:
        l=f1.write(lines[i])
f.close()
f1=open("text2.txt","r")
cont=f1.read()
print(cont)
f1.close()