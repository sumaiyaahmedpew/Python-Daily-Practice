#Banking System

class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance = {self.balance}")
        else:
            print("Insufficient funds!")

class SavingsAccount(Account):
    def __init__(self, acc_no, balance, interest_rate):
        super().__init__(acc_no, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added {interest}, New Balance = {self.balance}")

class CurrentAccount(Account):
    def __init__(self, acc_no, balance, overdraft_limit):
        super().__init__(acc_no, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance = {self.balance}")
        else:
            print("Overdraft limit exceeded!")


if __name__ == "__main__":
    s = SavingsAccount(101, 1000, 0.05)
    s.deposit(500)
    s.add_interest()
    s.withdraw(2000)

    c = CurrentAccount(102, 500, 1000)
    c.withdraw(1200)
    c.withdraw(2000)
