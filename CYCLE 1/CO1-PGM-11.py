#Find the biggest of three numbers
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
if a>b and a>c:
    print("The biggest number is ",a)
if b>c and b>a:
    print("The biggest number is ",b)
if c>a and c>b:
    print("The biggest number is ",c)