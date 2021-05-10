from controller.aluguel_controller import AluguelController
from controller.car_controller import CarController
from controller.user_controller import UserController
from dao import get
from model.usuario import User
from view.general_view import GeneralView


class MainController:

    def __init__(self):
        self.__usuarios = [User.fromJson(usuario) for usuario in get('usuarios')]
        self.__carros = []
        self.__alugueis = []

    def iniciar(self):
        opts = [self.carController, self.userController, self.aluguelController]
        optsString = ['Carros', 'Usuários', 'Aluguéis']
        while True:
            opt = GeneralView.menu(optsString, voltar='Sair')

            if opt is None or opt >= len(opts):
                GeneralView.message('Adeus')
                break
            else:
                opts[opt]()

    def carController(self):
        CarController(self.__carros).iniciar()

    def userController(self):
        UserController(self.__usuarios).iniciar()

    def aluguelController(self):
        AluguelController(self.__usuarios, self.__carros, self.__alugueis).iniciar()
