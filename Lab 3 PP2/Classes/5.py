class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Добавлено: {amount}. Текущий баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств.")
        else:
            self.balance -= amount
            print(f"Снято: {amount}. Текущий баланс: {self.balance}")

# Пример использования
acc = Account("Иван", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150)
"""
Объяснение:
Класс Account управляет балансом счёта с методами для внесения депозита и снятия средств с проверкой на недостаток средств.
"""