class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value != 0:
            return self.value / other.value
        else:
            return "Ошибка: деление на ноль невозможно."

num1 = Calculator(10)
num2 = Calculator(5)
print("Сложение:", num1 + num2)
print("Вычитание:", num1 - num2)
print("Умножение:", num1 * num2)
print("Деление:", num1 / num2)