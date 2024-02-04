class Account:
    def __init__(self,owner,balance = 0):
        self.owner,self.balance = owner,balance
    def deposit(self,n):
        self.balance+=n 
    def withdraw(self,n):
        if self.balance < n:
            print("Operation is not available")
            return
        self.balance-=n 
    def Print(self):
        print(self.balance)
a = Account("Abilmansur",100)
a.Print()
a.withdraw(101)
a.Print()
a.deposit(100)
a.Print()
a.withdraw(101)
a.Print()