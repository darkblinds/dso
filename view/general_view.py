import PySimpleGUI as sg

class GeneralView:

    @staticmethod
    def message(text):
        layout = [[sg.T(text)], [sg.B("OK")]]
        window = sg.Window("", layout)
        data = window.read(close=True)

    @staticmethod
    def menu(opts, voltar='Voltar'):
        layout = [
            [sg.B(element)] for index, element in enumerate(opts)
        ] + [[sg.B(voltar)]]
        window = sg.Window("Painel Geral", layout)
        data = window.read(close=True)[0]
        if data is None or data == voltar:
            return None
        else:
            return opts.index(data)
