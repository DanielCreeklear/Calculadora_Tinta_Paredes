class Comodo:

    def __init__(self, Comprimento, Largura, Altura):
        self.Comprimento = Comprimento
        self.Largura = Largura
        self.Altura = Altura

    def return_format(self):
        if self.Comprimento == self.Largura:
            return 'quadrático'
        else:
            return 'retangular'