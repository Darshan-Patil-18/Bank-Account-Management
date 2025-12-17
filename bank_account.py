class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self,amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        self.balance += amount
        print(f"{amount} has been deposited in your account")
        self.history.append(f"+{amount} has been deposited")

    def withdraw(self,amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        elif amount>self.balance:
            print("Sorry!!!! Insufficient Balance")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from your account")
            self.history.append(f"-{amount} has been withdrawn")

    def transaction_history(self):
        print("\n TRANSACTION HISTORY ")
        print(f"ACCOUNT HOLDER : {self.name}")
        print(f"CURRENT BALANCE : {self.balance}")
        if not self.history:
            print("No Transaction Done Yet....")
        else:
            for transaction in self.history:
                print(f"{transaction}")


name = input("Enter Your name : ")
balance = 0
account1 = Account(name,balance)
while True:
    print(f"\nHello {name}!!!")
    print("Welcome to our bank")

    print("\n Select your choice")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transaction History ")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if choice == 1:
        num = float(input("Enter Deposit amount : "))
        account1.deposit(num)

    elif choice == 2:
        num = float(input("Enter Withdraw amount : "))
        account1.withdraw(num)

    elif choice == 3:
        account1.transaction_history()

    elif choice == 4:
        print("Thanks for Trusting Our Bank")
        break

    else:
        print("ADD correct number 1 or 2 or 3 or 4 !!!!")

