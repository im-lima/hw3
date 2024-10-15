class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("сколько денег вы хотите добавить на счет? "))
        self._balance += amount
        print(f"на вашем счету теперь: {self._balance}")

    def _kill(self):
        self._balance = 0
        print("ваш баланс обнулен.")

    def __jackpot(self):
        self._balance *= 10
        print("поздравляем! вы выиграли джекпот! ваш баланс: ", self._balance)

    def _combine_balance(self, other):
        if isinstance(other, Bank):
            self._balance += other._balance
            print(f"объединенный баланс: {self._balance}")
        else:
            print("ошибка: можно объединять балансы только объектов Bank.")