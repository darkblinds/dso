from model.aluguel import Aluguel
from view.aluguel_view import AluguelView
from view.general_view import GeneralView


class AluguelController:
    def __init__(self, usuarios, carros, alugueis):
        self.__usuarios = usuarios
        self.__carros = carros
        self.__alugueis = alugueis

    def iniciar(self):
        opts = [self.alugarCarro, self.verAlugueis]
        optsString = ['Alugar carro', 'Ver alguéis']
        while True:
            opt = GeneralView.menu(optsString)

            if opt is None or opt >= len(opts):
                break
            else:
                opts[opt]()

    def alugarCarro(self):
        listaUsuarios = [user for user in self.__usuarios if
                         user not in map(lambda aluguel: aluguel.locatario, self.__alugueis)]
        listaCarros = [carro for carro in self.__carros if
                       carro not in map(lambda aluguel: aluguel.carro, self.__alugueis)]
        if len(listaUsuarios) == 0:
            GeneralView.message('Todos os usuários já alugaram um carro')
            return
        if len(listaCarros) == 0:
            GeneralView.message('Todos os carros já foram alugados')
            return
        try:
            data = AluguelView.getUser(listaUsuarios)
            if data is None:
                return
            botao, user = data
            if botao == 'Cancelar':
                return
            data = AluguelView.getCarro(listaCarros)
            if data is None:
                return
            botao, carro = data
            if botao == 'Cancelar':
                return
            data = AluguelView.duracao()
            if data is None:
                return
            duracao = data
            aluguel = Aluguel(user, carro, duracao=duracao)
            self.__alugueis.append(aluguel)
        except Exception as e:
            print(e)
            GeneralView.message('Não foi possível alugar o carro, tente novamente!')

    def verAlugueis(self):
        if len(self.__alugueis) == 0:
            GeneralView.message('Nenhum carro alugado')
            return
        try:
            data = AluguelView.show_alugueis(self.__alugueis)
        except Exception as e:
            print(e)
            GeneralView.message('Não foi possível ver os alugueis')
            return
        if data is None:
            return
        try:
            botao, index, aluguel = data
            if botao == 'Prolongar aluguel':
                self.prolongarAluguel(aluguel)
            elif botao == 'Devolver carro':
                self.devolverCarro(index)
        except:
            GeneralView.message('Não foi possível realizar a sua ação')

    def prolongarAluguel(self, aluguel):
        data = AluguelView.prolongar()
        if data is None:
            return
        aluguel.aumentarAlguel(data)

    def devolverCarro(self, index):
        del self.__alugueis[index]
