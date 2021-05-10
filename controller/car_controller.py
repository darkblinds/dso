from model.carros.luxury import Luxury_car
from model.carros.popular import Popular_car
from model.carros.suv import Suv_car
from view.car_view import CarView
from view.general_view import GeneralView


class CarController:

    def __init__(self, carros):
        self.__carros = carros

    def iniciar(self):
        opts = [self.cadastrar, self.verCarros]
        optsString = ['Cadastrar carro', 'Ver carros']
        while True:
            opt = GeneralView.menu(optsString)
            if opt is None or opt >= len(opts):
                break
            else:
                opts[opt]()

    def cadastrar(self):
        try:
            data = CarView.register_car()
            if data is None:
                return
            tipo, modelo, ano, placa = data
            if placa in list(map(lambda carro: carro.license_plate, self.__carros)):
                GeneralView.message('Carro com license_plate já cadastrada')
            else:
                if tipo == 'Luxo':
                    car = Luxury_car(modelo, ano, placa)
                elif tipo == 'Popular':
                    car = Popular_car(modelo, ano, placa)
                elif tipo == 'SUV':
                    car = Suv_car(modelo, ano, placa)
                else:
                    GeneralView.message('Tipo do carro desconhecido')
                    return
                self.__carros.append(car)
        except:
            GeneralView.message('Não foi possível cadastrar o carro, tente novamente!')

    def verCarros(self):
        try:
            data = CarView.show_cars(self.__carros)
        except:
            GeneralView.message('Não foi possível ver os carros')
            return
        if data is None:
            return
        try:
            botao, index, carro = data
            if botao == 'Editar':
                self.editarCarro(index, carro)
            elif botao == 'Deletar':
                self.deletarCarro(index)
        except:
            GeneralView.message(f'Não foi possível realizar a sua ação')

    def editarCarro(self, index, car):
        data = CarView.register_car(defaults=[car.modelo, car.ano, car.placa])
        if not data:
            return
        type, model, age, license_plate = data
        if license_plate != car.placa and license_plate in list(
                map(lambda carro: carro.placa, self.__carros)):
            GeneralView.message('Carro com placa já cadastrada')
        else:
            if type == 'Luxo':
                car = Luxury_car(model, age, license_plate)
            elif type == 'Popular':
                car = Popular_car(model, age, license_plate)
            elif type == 'SUV':
                car = Suv_car(model, age, license_plate)
            else:
                GeneralView.message('Tipo do carro desconhecido')
                return
            self.__carros[index] = car

    def deletarCarro(self, index):
        del self.__carros[index]
