class Calculadora:

    def __init__(self, Comodo):
        self.Comodo = Comodo

    def calcular_area_comprimento(self):
        return (self.Comodo.Comprimento * self.Comodo.Altura) * 2
