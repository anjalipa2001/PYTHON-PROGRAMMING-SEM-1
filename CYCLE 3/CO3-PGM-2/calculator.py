import calculatormain
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
ch=int(input("Enter your choice :\n 1.add \n 2.substract \n 3.Multiply \n 4.Division \n"))
if ch==1:
    print("Sum is ",calculatormain.add(a,b))
elif ch==2:
    print("Substraction is ",calculatormain.sub(a,b))
elif ch==3:
    print("Multiplication is ",calculatormain.mul(a,b))
elif ch==4:
    print("Division is ",calculatormain.div(a,b))
else:
    print("Incorrect option")


