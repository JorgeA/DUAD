class BankAccount:
    balance = 0

    def add_money(self, amount):
        balance += amount
        print(f"Transaccion satisfactoria, el saldo actual de su cuenta es {self.balance}")

    def subtract_money(self, amount):
        if amount > balance:
            print(f"Fondos insuficientes, usted dispone de {self.balance}")
        else:
            balance -= amount
            print(f"Transaccion satisfactoria, el saldo actual de su cuenta es {self.balance}")

class SavingsAccount(BankAccount):
    min_balance = 8000

    def subtract_money(self, amount):
        if amount > self.min_balance:
            print(f"La transaccion no puede ser realizada debido al requerimiento minimo de {self.min_balance}")
        else:
            balance -= amount
            print(f"Transaccion satisfactoria, el saldo actual de su cuenta es {self.balance}")

my_account = SavingsAccount()
my_account.subtract_money(500)