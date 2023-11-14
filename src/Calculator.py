class Calculator:
    def __init__(self, num1:float, num2:float) :
        self.num1 = num1
        self.num2 = num2
        self.res = 0

    def get_result(self):
        return self.res
    def add(self):
        self.res = self.num1 + self.num2
    def sub(self):
        self.res = self.num1 - self.num2
    def mul(self):
        self.res = self.num1 * self.num2
    def div(self):
        self.res = self.num1 / self.num2
