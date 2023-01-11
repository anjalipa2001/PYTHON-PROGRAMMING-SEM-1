import calculator
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Choose \n 1.Addition \n 2.Substraction\n 3.Multiplication \n 4.Division"))
if c==1:
    print(a,"+",b,"=",calculator.summ(a,b))
elif c==2:
    print(a,"-",b,"=",calculator.sub(a,b))
elif c==3:
    print(a,"*",b,"=",calculator.mul(a,b))
elif c==4:
    print(a,"/",b,"=",calculator.div(a,b))