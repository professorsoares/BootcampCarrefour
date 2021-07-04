class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


# verifica se o arquivo que está chamando o código abaixo é o próprio arquivo.
# Muito utilizado para a  definição de testes. De forma a não impactar o uso da classe por outros módulos.

# if __name__ != "__main__":
#     pass
# else:
#           ou
if __name__ == "__main__":
    tv = Televisao()
    print(tv.ligada)

    tv.power()
    print(tv.ligada)

    tv.power()
    print(tv.ligada)
