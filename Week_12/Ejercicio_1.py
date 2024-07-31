class BankAccount:
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        self.balance += amount
        print(f"Transacción satisfactoria, el saldo actual de su cuenta es {self.balance}")

    def subtract_money(self, amount):
        if amount > self.balance:
            print(f"Fondos insuficientes, usted dispone de {self.balance}")
        else:
            self.balance -= amount

class SavingsAccount(BankAccount):

    def __init__(self, min_balance=8000):
        super().__init__()
        self.min_balance = min_balance

    def subtract_money(self, amount):
        real_balance = self.balance - amount

        if real_balance < self.min_balance:
            print(f"ALERTA !!!, su operacion no es permitida ya que debe mantener un mínimo de {self.min_balance} en su cuenta")
        else:
            super().subtract_money(amount)
            print(f"Transacción exitosa, su saldo actual es {self.balance}")

my_account = SavingsAccount(min_balance=8000)
my_account.add_money(10000)
my_account.subtract_money(amount=int(input("Ingrese la cantidad a retirar: ")))
