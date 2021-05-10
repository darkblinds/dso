from model.usuario import User
from view.general_view import GeneralView
from view.usuario_view import UserView


class UserController:
    def __init__(self, usuarios):
        self.__usuarios = usuarios

    def iniciar(self):
        opts = [self.cadastrar, self.verUsuarios]
        optsString = ['Cadastrar usuário', 'Ver usuários']
        while True:
            opt = GeneralView.menu(optsString)

            if opt is None or opt >= len(opts):
                break
            else:
                opts[opt]()

    def cadastrar(self):
        try:
            data = UserView.register_user()
            if data is None:
                return
            nome, idade, telefone = data
            id = len(self.__usuarios)
            user = User(id, nome, idade, telefone)
            self.__usuarios.append(user)
        except:
            GeneralView.message('Não foi possível cadastrar o usuário, tente novamente!')

    def verUsuarios(self):
        try:
            data = UserView.show_users(self.__usuarios)
        except Exception as e:
            print(e)
            GeneralView.message('Não foi possível ver os usuários')
            return
        if data is None:
            return
        try:
            botao, index, usuario = data
            if botao == 'Editar':
                self.editarUsuario(index, usuario)
            elif botao == 'Deletar':
                self.deletarUsuario(index)
        except:
            GeneralView.message('Não foi possível realizar a sua ação')

    def editarUsuario(self, index, user):
        data = UserView.register_user(defaults=[user.nome, user.idade, user.telefone])
        if not data:
            return
        nome, idade, telefone = data
        user.nome = nome
        user.idade = idade
        user.telefone = telefone

    def deletarUsuario(self, index):
        del self.__usuarios[index]
