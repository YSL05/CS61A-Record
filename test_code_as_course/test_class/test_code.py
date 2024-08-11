class Account:

    def __init__(self, account_holder):
        self.balance = 0
        self.holder  = account_holder
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if (self.balance < amount):
            print("account is not enough")
        else:
            self.balance = self.balance - amount
            return self.balance
class CheckingAccount(Account):
    """A bank account that charges for withdrawals"""

    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)