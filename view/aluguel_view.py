import PySimpleGUI as sg

from view.general_view import GeneralView


class AluguelView:

    @staticmethod
    def getUser(listaUsuarios):
        if len(listaUsuarios) == 0:
            GeneralView.message('Não tem carros para mostrar')
        else:
            layout = [[sg.Radio(f"ID: {user.id}, Nome: {user.nome}, Idade: {user.idade}, Telefone: {user.telefone}",
                                'users')]
                      for index, user in enumerate(listaUsuarios)] + [[sg.B('Cancelar')], [sg.Submit("Enviar")]]
            window = sg.Window("Escolha o Cliente", layout)
            data = window.read(close=True)
            botao = data[0]
            if not data:
                return
            try:
                index = [key for key, value in data[1].items() if value][0]
            except IndexError:
                return
            usuarios = listaUsuarios[index]
            return botao, usuarios

    @staticmethod
    def getCarro(listaCarros):
        if len(listaCarros) == 0:
            GeneralView.message('Não tem usuários para mostrar')
        else:
            layout = [[sg.Radio(
                f"Tipo: {listaCarro.tipo}, Modelo: {listaCarro.modelo}, Ano: {listaCarro.ano}, Placa: {listaCarro.placa}",
                'carros')]
                         for index, listaCarro in enumerate(listaCarros)] + [[sg.B("Cancelar"), sg.Submit("Confirmar")]]
            window = sg.Window("Escolha o Carro", layout)
            data = window.read(close=True)
            botao = data[0]
            if not data:
                return
            try:
                index = [key for key, value in data[1].items() if value][0]
            except IndexError:
                return
            carros = listaCarros[index]
            return botao, carros

    @staticmethod
    def duracao():
        layout = [
            [sg.Radio("7 Dias", 'tipo', key='7')], [sg.Radio('15 Dias', "tipo", key='15')],
            [sg.Radio('30 Dias', "tipo", key='30')],
            [sg.B('Alugar')], [sg.B('Cancelar')]
        ]
        window = sg.Window("Duração do aluguel", layout)
        resposta = window.read(close=True)
        if resposta is None or resposta[0] == 'Cancelar':
            return None
        resposta = resposta[1]
        tipo = 7 if resposta['7'] else 15 if resposta['15'] else 30 if resposta['30'] else None
        return tipo

    @staticmethod
    def show_alugueis(alugueis):
        layout = [[sg.Radio(
            f" Modelo: {aluguel.carro.modelo}, Ano: {aluguel.carro.ano}, Cliente: {aluguel.locatario.nome}, Devolução : {aluguel.devolucao.strftime('%d/%m/%Y')}",
            'aluguel')] for aluguel in alugueis] + [[sg.B("Voltar"), sg.B("Prolongar aluguel"), sg.B("Devolver carro")]]
        window = sg.Window("Mostrar carros alugados", layout)
        data = window.read(close=True)
        if data is None:
            return
        botao = data[0]
        try:
            aluguelIndex = [key for key, value in data[1].items() if value][0]
        except IndexError:
            return
        return botao, aluguelIndex, alugueis[aluguelIndex]

    @staticmethod
    def prolongar():
        layout = [
            [sg.T("Dias"), sg.Input()],
            [sg.B("Confirmar"), sg.B("Cancelar")]
        ]
        window = sg.Window('Prolongar', layout)
        data = window.read(close=True)
        if not data or data[0] == 'Cancelar':
            return
        value = data[1][0]
        return int(value)
