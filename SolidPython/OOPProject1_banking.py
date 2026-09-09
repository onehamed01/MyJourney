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
        return True
    
    @property
    def is_empty(self):
        return self._balance == 0



class SavingAccount(BankAccount):
    def __init__(self, owner, balance, minimum_balance):
        super().__init__(owner, balance)
        self._minimum_balance = minimum_balance

    @property
    def minimum_balance(self):
        return self._minimum_balance

    def withdraw(self, amount):
        if self._minimum_balance > self._balance - amount:
            return False
        return super().withdraw(amount)

class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.collection_bank_account: list[BankAccount] = []

    def add_account(self, account: BankAccount):
        self.collection_bank_account.append(account)

    def total_balance(self):
        total_balance = 0
        for obj in self.collection_bank_account:
            total_balance += obj.balance
        return total_balance

    
    def withdraw_from_all(self, amount):
        all_accounts = self.collection_bank_account
        
        count_accounts = 0

        for obj in all_accounts:
            if obj.withdraw(amount):
                count_accounts += 1
        return count_accounts




hami = Customer('Hami')
hami_1_bank_account = BankAccount('Hami', 6000)
hami_1_saving_account = SavingAccount('Hami', 5100, 500)
hami_2_bank_account = BankAccount('Hami', 5500)

hami.add_account(hami_1_bank_account)
hami.add_account(hami_1_saving_account)
hami.add_account(hami_2_bank_account)
print(hami.withdraw_from_all(5000))