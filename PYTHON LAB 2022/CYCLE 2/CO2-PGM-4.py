from math import sqrt
x=int(input("Enter the limit :"))
y=int(input("Enter the limit :"))
for i in range(x,y):
    if sqrt(i)==int(sqrt(i)) and i%2==0:
        print(i)
