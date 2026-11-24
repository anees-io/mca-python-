class Bank:
    def __init__(self, accno, name, acc_type, balance):
        self.accno = accno
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Number:", self.accno)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)


# User input
accno = input("Enter account number: ")
name = input("Enter name: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

# Creating object
b = Bank(accno, name, acc_type, balance)

b.display()

amount = float(input("Enter amount to deposit: "))
b.deposit(amount)
print("Balance:", b.balance)

amount = float(input("Enter amount to withdraw: "))
b.withdraw(amount)

b.display()
