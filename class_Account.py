class Account:

    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,plus_amo):
        self.balance+=plus_amo
        print(f"Added {plus_amo} to the balance")

    def withdraw(self,minus_amo):
        if self.balance>=minus_amo:
            self.balance -= minus_amo # self.balance = self.balance - minus_amo
            print("Withdrawal accepted")
        else:
            print("Sorry non enough funds!")
    # i wannt to print my account Obj:
    def __str__(self):
        return f"Owner: {self.owner} \nBalance:{self.balance}"



#  Instantiate the class = create obj
acct1 = Account('Nasimi',5000)

print(acct1)
#Show the account balance attribute
print(acct1.balance)
#Show the account owner attribute
print(acct1.owner)

# Make a series of deposits and withdrawals
acct1.deposit(500)
print(acct1.balance)
acct1.withdraw(100)
print(acct1.balance)
# Make a withdrawal that exceeds the available balance
#acct1.withdraw(6000)
acct1.withdraw(1000)
print(acct1.balance)
print(acct1)
