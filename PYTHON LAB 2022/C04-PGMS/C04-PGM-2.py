class Bank:
    def __init__(self):
        self.account=input("\n Enter the account number : ")
        self.name=input("\n Enter the name : ")
        self.types=input("\n Enter the type of account : ")
        self.balance=0
 
    def deposit(self):
        amount=int(input("\nEnter amount to be Deposited: "))
        self.balance += amount

 
    def withdraw(self):
        amount = int(input("\n Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        print("\n Net availabe balance",self.balance)
   
    
s = Bank()
while(True):
    print("\n 1.Deposit \n 2.withdraw \n 3.Exit")
    ch=int(input("\n Enter your choice : "))
    if(ch==1):
        s.deposit()
        s.display()
    elif(ch==2):
        s.withdraw()
        s.display()
    else:
        exit(0)

 