class Bankaccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Not enough balance!")
    def show(self,balance):
        print(self.owner,"'s balance:",self.balance)
choose = 0
owner = input("Owner: ")
balance = int(input("Starting balance: "))
account = Bankaccount(owner,balance)
while choose != 4:
    choose = int(input("===== Bank =====\n\n"
                       "1. Deposit\n"
                       "2. Withdraw\n"
                       "3. Show Balance\n"
                       "4. Exit\n"
                       "Choose: "))
    if choose == 1:
        amount = int(input("Amount: "))
        account.deposit(amount)
    if choose == 2:
        amount = int(input("Amount: "))
        account.withdraw(amount)
    if choose == 3:
        account.show(balance)
print ("Program Closed")