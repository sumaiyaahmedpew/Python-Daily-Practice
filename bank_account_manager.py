# problem_26 Bank Account Manager

balance = 1000 

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited {amount}, New Balance = {balance}")

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print(f"Withdrew {amount}, New Balance = {balance}")
    else:
        print("Insufficient funds!")

def check_balance():
    print(f"Current Balance = {balance}")

def fake_withdraw(amount): 
    balance = 0  
    balance -= amount
    print("Local balance inside fake_withdraw:", balance)

check_balance()
deposit(500)
withdraw(300)
fake_withdraw(100)
check_balance()
