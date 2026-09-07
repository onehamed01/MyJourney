class BankAccount:
    bank_name = "LLOYDS"

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @classmethod
    def change_bank_name(cls, new_name):
        cls.BANK_NAME = new_name

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            return False
        self._balance += amount
        return True

    def withdraw(self, amount):
        if amount > self._balance or amount <= 0:
            return False
        self._balance -= amount
    
    @property
    def is_empty(self):
        return self._balance == 0



