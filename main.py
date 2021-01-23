from calculadora import Calculadora
from comodo import Comodo
from lata_tinta import Tinta

def main():
    # Dados sobre o cômodo
    Largura = float(input('Digite a largura do cômodo: '))
    Comprimento = float(input('Digite o comprimento do cômodo: '))
    Altura = float(input('Digite a altura do cômodo: '))

    # Dados sobre a tinta
    Quantidade_litros_lata = float(input('Digite a quantidade de litros em apenas UMA lata: '))
    Rendimento = float(input('Digite quantos metros quadrados rende a lata: '))
    Demaos = int(input('Digite quantas demãos serão necessárias: '))

    comodo = Comodo(Comprimento, Largura, Altura)
    tinta = Tinta(Quantidade_litros_lata, Rendimento, Demaos)
    formato = comodo.return_format()
    resultado = Calculadora(comodo, tinta)

    print('Considerando uma lata de {0:.1f}L com rendimento de {1:.1f}m²,'
          ' e {2} demãos:\n'
          'Serão necessários {3:.1f}L de tinta para pintar as '
          'paredes do cômodo {4},\ne mais {5:.1f}L para o teto. '
          'Totalizando assim {6:.1f}L ao todo.\nPortanto compre'
          'compre {7} latas dessa!'.format(tinta.quantidade_litros_lata,
                                                   tinta.rendimento,
                                                   tinta.demaos,
                                                   resultado.calcular_litros_paredes(),
                                                   comodo.return_format(),
                                                   resultado.calcular_litros_teto(),
                                                   resultado.calcular_litros_total(),
                                                   resultado.calcular_quantidade_latas()))

while True:
    print('===============================\n'
          '===============================\n'
          '====BEM VINDO À CALCULADORA====\n'
          '=======PARA A PINTURA DE=======\n'
          '============CÔMODOS============\n'
          '===============================\n'
          '===============================\n'
          '* Por Favor, utilize o SI(Sistema Internacional '
          'de medidas!(Metros e Litros)')

    main()

    if not 'S' in str(input('Deseja recalcular? (S/N)\n')):
        break
