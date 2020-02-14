class Account:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,value):
        self.value=self.balance+value

    def withdraw(self,debt):
        self.debt=self.value-debt

#  Instantiate the class = create obj
acct1 = Account('Nasimi',5000)

print(acct1)
#Show the account balance attribute
print(acct1.balance)
#Show the account owner attribute
print(acct1.owner)

# Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)
# Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
print(acct1.withdraw(100))

