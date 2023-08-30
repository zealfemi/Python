from colorama import init
init()
from colorama import Fore

class Account:
    
    def __init__(self, owner="ACC NAME", balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: ${self.balance}"
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Deposit of ${amount} Accepted \nNew Balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
          self.balance = self.balance - amount
          return f"Withdrawal of ${amount} Accepted \nNew Balance: ${self.balance}"
        return f"Funds Unavailable! Balance: ${self.balance}"

acct1 = Account('Mackie', 100)

print(acct1.owner)
print(acct1.balance)

print(acct1.deposit(50))

print(acct1.withdraw(100))

print(Fore.RED + acct1.withdraw(500))
