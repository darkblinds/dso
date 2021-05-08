from model.carros.car import Car


class Suv_car(Car):
    def __init__(self, modelo, ano, placa):
        super().__init__('SUV', modelo, ano, placa)
