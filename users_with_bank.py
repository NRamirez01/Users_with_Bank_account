class BankAccount:
    accounts = {}
    def __init__(self, account_type, balance=0):
        self.account_type = account_type
        for name in BankAccount.accounts:
            self.name = name
        self.balance= balance
        self.accounts = BankAccount.accounts[self.name]
    def deposit(self, account_type, amount):
        i = 0
        while i < len(self.accounts):
            for key in self.accounts[i]:
                if key == account_type:
                    self.accounts[i][account_type] += amount
                    return self
                else: 
                    i += 1
    def withdrawal(self, account_type, amount): #forgot to add this until looking at solution
        i = 0
        while i < len(self.accounts):
            for key in self.accounts[i]:
                if key == account_type:
                    if self.accounts[i][account_type]-amount >= 0:
                        self.accounts[i][account_type] -= amount
                        return self
                    else: 
                        print("Insufficient Funds: Charging $5 Overdraft Fee")
                        return self
                else: 
                    i += 1
    def display_account_info(self, account_type):
        i = 0
        while i < len(self.accounts):
            for key in self.accounts[i]:
                if key == account_type:
                    print(f"{self.name}'s {account_type} account balance is {self.accounts[i][account_type]}")
                    return self
                else: 
                    i += 1
class User:
    accounts = []
    def __init__(self, name, account_type, balance):       
        self.name = name
        self.balance = balance
        self.account_type = account_type
        if f'{name}' in BankAccount.accounts:
            BankAccount.accounts[name]= User.accounts
            User.accounts.append({account_type : balance})
        else:
            BankAccount.accounts[name] = [{account_type: balance}]
            User.accounts.append({account_type : balance})
        self.bank = BankAccount(account_type, balance)
    def make_deposit(self, account_type, amount):
        self.bank.deposit(account_type, amount)
        return self
    def make_withdrawal(self, account_type, amount):
        self.bank.withdrawal(account_type, amount)
        return self
    def display_user_balance(self, account_type):
        self.bank.display_account_info(account_type)
        return self
nate = User("Nate", "Checking", 6000)
nate = User("Nate", "Savings", 10000)
nate = User("Nate", "Piggybank", 4000)
sally = User("Sally", "Checking", 420)
nate.make_withdrawal("Savings", 1000).make_withdrawal("Savings", 1000).make_withdrawal("Savings", 1000).make_withdrawal("Savings", 1000).display_user_balance("Savings")
nate.make_deposit("Checking", 1000).make_withdrawal("Checking", 7000).display_user_balance("Checking")
nate.make_deposit("Piggybank", 1000).display_user_balance("Piggybank")
sally.display_user_balance("Checking")

# Original attempt to iterate through balances included the following:
#   account_index = len(BankAccount.accounts[name])-1
#     if account_index < 1:
#         BankAccount.accounts[name][account_type] = balance
#         self.balance = balance 
#         print(self.balance)
#     if account_index >= 1:
#         BankAccount.accounts[name][account_index][account_type] = balance
#         self.balance = balance 