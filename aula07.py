

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def divisao(self):
        return self.a / self.b

    def multiplicacao(self):
        return self.a * self.b


calc = Calculadora(10,2)

print(calc.soma())
print(calc.subtracao())
print(calc.divisao())
print(calc.multiplicacao())



#--------------------------------------

#
# def soma(a, b):
#     return a + b
#
# def subtracao(a, b):
#     return a - b
#
# def divisao(a, b):
#     return a / b
#
# def multiplicacao(a, b):
#     return a * b

# print(soma(1,2))
# print(soma(3,4))
# print(subtracao(3,4))
# print(divisao(3,4))
# print(multiplicacao(3,4))