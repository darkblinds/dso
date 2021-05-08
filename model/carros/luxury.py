from model.carros.car import Car


class Luxury_car(Car):
    def __init__(self, modelo, ano, placa):
        super().__init__('Luxuoso', modelo, ano, placa)
