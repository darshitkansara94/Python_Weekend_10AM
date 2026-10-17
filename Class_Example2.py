class calculator():
    def __init__(self):
        self.a = 10
        self.b = 10

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

calc = calculator()
add = calc.addition()
print(add)
mul = calc.multiplication()
print(mul)
div = calc.division()
print(div)