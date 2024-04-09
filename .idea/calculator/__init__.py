class Calculator:
    def __init__(self, number):
        self.number = number

    def add(self, num):
        self.number += num

    def subtract(self, num):
        self.number -= num

    def multiply(self, num):
        self.number *= num

    def divide(self, num):
        if self.num2 == 0:
            return "Cannot divide by zero"
        self.number /= num

    def result(self):
        return self.number

calculator = Calculator(5)
calculator.add(3)
calculator.multiply(2)
print(calculator.result())