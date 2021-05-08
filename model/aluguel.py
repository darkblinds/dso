from datetime import datetime, timedelta


class Aluguel:
    def __init__(self, locatario, carro, alugado=datetime.now(), duracao=7):
        self.__locatario = locatario
        self.__carro = carro
        self.__alugado = alugado
        self.__duracao = duracao

    def aumentarAlguel(self, dias):
        self.__duracao += dias

    @property
    def devolucao(self):
        return self.__alugado + timedelta(days=self.__duracao)

    @property
    def locatario(self):
        return self.__locatario

    @property
    def carro(self):
        return self.__carro

    @property
    def alugado(self):
        return self.__alugado

    @property
    def duracao(self):
        return self.__duracao

    @locatario.setter
    def locatario(self, locatario):
        self.__locatario = locatario

    @carro.setter
    def carro(self, carro):
        self.__carro = carro

    @alugado.setter
    def alugado(self, alugado):
        self.__alugado = alugado

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao
