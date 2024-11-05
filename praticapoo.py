"""Aa"""

class Funcionario():
    """A"""
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    def __versal__(self):
        print(f"Salário de {self.nome}, cargo {self.cargo} é R${self.__salario:.2f}")

    def __aumentarsal__(self, bonus):
        if bonus > 0 :
            self.__salario = self.__salario + bonus

class Gerente(Funcionario):
    """A"""
    def __init__(self, nome, cargo, salario):
        super().__init__(nome, cargo, salario)
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario + 1000

    def __versal__(self):
        print(f"Salário de {self.nome}, cargo {self.cargo} é R${self.__salario:.2f}")

    def __aumentarsal__(self, bonus):
        if bonus > 0:
            self.__salario = self.__salario + bonus

eu = Funcionario("EU", "Entregador", 2130)
eu.__versal__()
eu.__aumentarsal__(500)
eu.__versal__()

ele = Gerente("ELE", "Gerente", 2130)
ele.__versal__()
ele.__aumentarsal__(500)
ele.__versal__()
