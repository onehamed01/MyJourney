class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, balance: float, owner: str):
        self._balance = balance
        self.owner = owner
    
    def change_bank_name(self, bankname: str) -> None:
        self.bank_name = bankname

    @property
    def balance(self) -> float:
        return self._balance
    
    def deposit(self, amount:float) -> str:
        if amount <= 0:
            return "Please insert a valid amount!"
        
        self._balance += amount
        return f"£{amount} has been deposit"
    
    def withdraw(self, amount: float) -> str:
        if self._balance < amount:
            return "The amount is more than your balance!"
        elif amount <= 0 :
            return "Please insert a valid amount!"

        self._balance -= amount
        return f"£{amount} has deduce from your account"
        
hami = BankAccount(27000.00, 'Hami')
hami.withdraw(500)
print(hami.balance)
hami.withdraw(2000)
print(hami.balance)
hami.change_bank_name('LLOYDS')