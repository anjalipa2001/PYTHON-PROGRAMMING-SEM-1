
class Bank_Account:
    def __init__(self):
        self.balance=0
          
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance = self.balance + amount
        print("\n Amount Deposited:",amount)
  
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance = self.balance-amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
  
    def display(self):
        print("\n Net Available Balance=",self.balance)
  
b= Bank_Account()
while(True):
    print("\n 1:Deposit Money \n 2:Withdraw Money \n 3:Exit")
    ch=int(input("Enter the choice: "))
    if(ch==1):
        b.deposit()
        b.display()
    elif(ch==2):
        b.withdraw()
        b.display()
    else:
        exit(0)
b.display()

