from math import ceil

class Calculadora:

    def __init__(self, Comodo, Tinta):
        self.Comodo = Comodo
        self.Tinta = Tinta
    def calcular_area_total_paredes(self):
        return 2 * self.Comodo.Altura * (self.Comodo.Comprimento + self.Comodo.Largura)

    def calcular_area_teto(self):
        return self.Comodo.Comprimento * self.Comodo.Largura

    def calcular_area_total_comodo(self):
        return self.calcular_area_total_paredes() + self.calcular_area_teto()

    def calcular_litros_area(self, area):
        return area * self.Tinta.return_constanteTinta()

    def calcular_litros_paredes(self):
        return self.calcular_litros_area(self.calcular_area_total_paredes())

    def calcular_litros_teto(self):
        return self.calcular_litros_area(self.calcular_area_teto())

    def calcular_litros_total(self):
        return (self.calcular_litros_paredes() + self.calcular_litros_teto()) * self.Tinta.demaos

    def calcular_quantidade_latas(self):
        return ceil(self.calcular_litros_total() / self.Tinta.quantidade_litros_lata)