from colorama import Fore
class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.name} \nBalance: ${self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit: ${amount} \nBalance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal: ${amount} \nBalance: ${self.balance}"
        return f"Insufficient funds \nBalance: ${self.balance}"
    
account = Account("Mackie", 500)
print(account)
print(account.deposit(300))
print(account.withdraw(800))
print(account.withdraw(2))
