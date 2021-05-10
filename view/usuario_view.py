import PySimpleGUI as sg

from view.general_view import GeneralView


class UserView:

    @staticmethod
    def register_user(defaults=None):
        layout = [
            [sg.T("Nome", size=(6, 0)), sg.Input(default_text=defaults[0] if defaults else '', size=(10, 0))],
            [sg.T("Idade", size=(6, 0)), sg.Input(default_text=defaults[1] if defaults else '', size=(10, 0))],
            [sg.T("Telefone", size=(6, 0)), sg.Input(default_text=defaults[2] if defaults else '', size=(10, 0))],
            [sg.Submit("Enviar", key=1), sg.B("Voltar", key=2)]
        ]
        window = sg.Window('Registrar', layout)
        answer = window.read(close=True)[1]
        nome = answer[0]
        idade = answer[1]
        telefone = answer[2]
        if not idade.isnumeric():
            GeneralView.message("Idade inválida")
            return

        return nome, idade, telefone

    @staticmethod
    def show_users(users):
        if len(users) == 0:
            GeneralView.message('Não tem usuários para mostrar')
        else:
            layout = [[sg.Radio(f"ID: {user.id}, Nome: {user.nome}, Idade: {user.idade}, Telefone: {user.telefone}", 'users')]
                         for index, user in enumerate(users)] + [
                         [sg.B("Voltar"), sg.Submit("Editar"), sg.Submit("Deletar")]]
            window = sg.Window("Painel usuário", layout)
            data = window.read(close=True)
            if not data:
                return
            botao = data[0]
            try:
                userIndex = [key for key, value in data[1].items() if value][0]
            except IndexError:
                return
            return botao, userIndex, users[userIndex]
