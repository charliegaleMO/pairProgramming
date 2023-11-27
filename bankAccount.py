class BankAccount:
    account_number_generator = 100000
    def init(self, customer_name, balance=0.0):
        self.customer_name = customer_name
        self.account_number = BankAccount.account_number_generator
        BankAccount.account_number_generator += 1
        self.balance = balance
    
    def account_number(self):
        return self._account_number
    
    def balance(self):
        return self._balance
    
    def balance(self, value):
        self._balance = round(value, 2)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("You successfully deposited "+ amount +", your new balance is "+ self.balance )
        else:
            print("Error deposit too small (this isnt actually an error)")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("You successfully withdrew " + amount + ", your new balance ")
