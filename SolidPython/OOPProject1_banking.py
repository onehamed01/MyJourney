class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, balance: float, owner: str):
        self._balance = balance
        self.owner = owner
    
    @classmethod
    def change_bank_name(cls, bankname: str) -> None:
        cls.bank_name = bankname

    @property
    def balance(self) -> float:
        return self._balance
    
    def deposit(self, amount:float) -> bool:
        if amount <= 0:
            return False
        
        self._balance += amount
        return True
    
    def withdraw(self, amount: float) -> bool:
        if self._balance < amount or amount <= 0:
            return False

        self._balance -= amount
        return True

    @property
    def is_empty(self) -> bool:
        return self._balance == 0
        
hami = BankAccount(27000.00, 'Hami')
hami.deposit(2000)
print(hami.balance)
print(hami.is_empty)
hami.withdraw(9800000)
print(hami.is_empty)
BankAccount.change_bank_name("LLOYDS")
print(BankAccount.bank_name)