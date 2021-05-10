import PySimpleGUI as sg

import excessao_inteiro
from view.general_view import GeneralView


class CarView:

    @staticmethod
    def register_car(defaults=None):
        layout = [
            [sg.Radio("Popular", 'type', key='Popular')], [sg.Radio('Luxo', "type", key='Luxo')],
            [sg.Radio('SUV', "type", key='SUV')],
            [sg.T("Modelo", size=(6, 0)), sg.Input(default_text=defaults[0] if defaults else '', size=(10, 0))],
            [sg.T("Ano", size=(6, 0)), sg.Input(default_text=defaults[1] if defaults else '', size=(10, 0))],
            [sg.T("Placa", size=(6, 0)), sg.Input(default_text=defaults[2] if defaults else '', size=(10, 0))],
            [sg.Submit("Enviar", key=1), sg.B("Voltar", key=2)]
        ]
        window = sg.Window('Registrar', layout)
        answer = window.read(close=True)[1]
        type = 'Popular' if answer['Popular'] else 'Luxo' if answer['Luxo'] else 'SUV' if answer['SUV'] else None
        model = answer[0]
        age = answer[1]
        if age is None:
            return
        elif not age.isnumeric():
            raise excessao_inteiro
            return
        license_plate = answer[2]

        return type, model, age, license_plate

    @staticmethod
    def show_cars(cars):
        if len(cars) == 0:
            GeneralView.message('Não tem carros para mostrar')
        else:
            layout = [[sg.Radio(
                """{} - Tipo: {}, Modelo: {}, Ano: {}, Placa: {}""".format(index, car.tipo, car.modelo,
                                                                           car.ano, car.placa), 'car')]
                         for index, car in enumerate(cars)] + [
                         [sg.B("Voltar"), sg.Submit("Editar"), sg.Submit("Deletar")]]
            window = sg.Window("Painel carro", layout)
            data = window.read(close=True)
            if not data:
                return
            botao = data[0]
            try:
                carIndex = [key for key, value in data[1].items() if value][0]
            except IndexError:
                return
            return botao, carIndex, cars[carIndex]


