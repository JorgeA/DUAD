class BankAccount:
    balance = 0

    def add_money(self, amount):
        self.balance += amount
        print(f"Transaccion satisfactoria, el saldo actual de su cuenta es {self.balance}")

    def subtract_money(self, amount):
        if amount > self.balance:
            print(f"Fondos insuficientes, usted dispone de {self.balance}")
        else:
            self.balance -= amount

class SavingsAccount(BankAccount):
    min_balance = 8000

    def check_balance(account):
        amount = int(input("Ingrese la cantidad a retirar: "))
        real_balance = account.balance - amount

        if real_balance < account.min_balance:
            print(f"ALERTA !!!, su no es operacion permitida ya que debe mantener un minimo de {account.min_balance} en su cuenta")
        else:
            account.subtract_money(amount)
            print(f"Transaccion exitosa, su saldo actual es {account.balance}")

my_account = SavingsAccount()
my_account.add_money(10000)
SavingsAccount.check_balance(my_account)
