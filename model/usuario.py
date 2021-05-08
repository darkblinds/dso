class User:

    def __init__(self, id, nome, idade, telefone):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__telefone = telefone

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def telefone(self):
        return self.__telefone

    @id.setter
    def id(self, id):
        self.__id = id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
