
class User():
# Update the User class __init__ method
    def __init__(self, name="Unknown", balance=0, int_rate=.02):
        self.name = name
        self.account = BankAccount(balance,int_rate)
        # super().__init__=(balance,int_rate)
# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
# Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

# Constructor/ Blue print --------------------------
class BankAccount:

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.in_rate= int_rate
        self.balance= balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
# Instances -------------------------------------------------------------------------------------
# deposit(self, amount) - increases the account balance by the given amount
# Create code that increase BALANCE by amount deposit  so use +=
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here

# withdraw(self, amount) - decreases the account balance by the given amount if there are 
# sufficient funds; if there is not enough money, print a message "Insufficient funds:
# Charging a $5 fee" and deduct $5
# Create Code that decreases (subtract) BALANCE by amout withdraw! Use -= THEN!
# Creat a if/else function that prints "Insufficient funds" in not enough money use >= 0 take $5 out of balance
    def withdraw(self, amount):
        if (self.balance - amount) >=0:
            self.balance -= amount
        else: 
            print('No Money: Charging a $5.00 fee')
            self.balance-=5
            return self
        # your code here

# display_account_info(self) - print to the console: eg. "Balance: $100"
# Create Code that prints just the Balance: #### (simple print statement)
    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self
        # your code here


# User test
randy = User("Randy")
randy.display_user_balance().make_deposit(3000).display_user_balance()
randy.make_withdrawal(42).display_user_balance()

randi = User(name="Randi",)
randi.display_user_balance().make_deposit(800)
randi.make_withdrawal(7000).display_user_balance()




