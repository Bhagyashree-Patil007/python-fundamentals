#create account class with 2 attributes -balance & account no. create methods for debit,credit, & printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount
        print("rs",amount, "was debited")
        print("the total amount is: ",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("rs",amount, "was credited")
        print("the total amount is: ",self.get_balance())


    def get_balance(self):
        return self.balance
    
acc1=Account(1000,1234)
acc1.debit(150)
acc1.credit(123)
acc1.credit(1200)
    
    