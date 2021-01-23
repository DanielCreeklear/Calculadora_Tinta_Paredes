class Tinta:

    def __init__(self, quantidade_litros_lata, rendimento, demaos):
        self.quantidade_litros_lata = quantidade_litros_lata
        self.rendimento = rendimento
        self.demaos = demaos

    def return_constanteTinta(self):
        return self.quantidade_litros_lata / self.rendimento