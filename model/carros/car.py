class Car:
    def __init__(self, tipo, modelo, ano, placa):
        self.__tipo = tipo
        self.__modelo = modelo
        self.__ano = ano
        self.__placa = placa

    @property
    def tipo(self):
        return self.__tipo

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def placa(self):
        return self.__placa

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @placa.setter
    def placa(self, placa):
        self.__placa = placa
