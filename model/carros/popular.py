from model.carros.car import Car


class Popular_car(Car):
    def __init__(self, modelo, ano, placa):
        super().__init__('Popular', modelo, ano, placa)
