class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance

    def Deposite(self,d):
        self.balance=self.balance + d 

    def Withdrawal(self,w):
        if w<self.balance :
            self.balance=self.balance-w
        else:
            print("Sorry")

    def bankFees(self):
        self.balance= (95/100)*self.balance

    def display(self):
        print(f"Account number:{self.accountNumber} \nName:{self.name} \nBalance:{self.balance}")    

Account=BankAccount(12345678909,"labdhi",345678)
Account.Deposite(2)
Account.Withdrawal(680)
Account.Withdrawal(456789)
Account.bankFees()
Account.display()
