class Bank_acct:
    def __init__(self, interest =5, account_balance =100):
        self.account_balance = 100
        self.interest = 5


    def deposit(self, amount):
        self.account_balance += amount
        print(f"Your balance is now {self.account_balance}")
        return self

    def withdraw(self, amount):
        if Bank_acct.can_withdraw(self.account_balance,amount):
            self.account_balance -= amount
            print(f"Your balance is now {self.account_balance}")
        else:
            print("Insufficient Funds")
            self.account_balance -= 5
        return self
    @staticmethod
    def can_withdraw(account_balance,amount):
        if (account_balance - amount) < 0:
            return False
        else:
            return True
    def yield_interest(self):
        self.account_balance += (self.interest*self.account_balance /100)
        print (f"You got interest! You now have {self.account_balance}")
        return self
    def display_account_info(self):
        print(f"You currently have {self.account_balance} and your interest rate is {self.interest}")
        return self

class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account = Bank_acct(interest =5, account_balance=100)
        User.totalUsers =+ 1



Brian = User("Brian", "brian@predatoryloans.com")
Sariah = User("Sariah", "sariah@fairbanking.com")

Brian.account.deposit (5).deposit (300).deposit (25000).withdraw (500).yield_interest()
Sariah.account.deposit (200).deposit(400).withdraw(50).withdraw(75).withdraw(50).withdraw(100).yield_interest().display_account_info()





"""



    @classmethod
    def userCount(cls):
        print (f"There are {User.totalUsers} banking here")
"""