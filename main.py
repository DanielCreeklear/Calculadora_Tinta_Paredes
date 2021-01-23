from calculadora import Calculadora
from comodo import Comodo

def main():
    Largura = float(input('Digite a largura do cômodo: '))
    Comprimento = float(input('Digite o comprimento do cômodo: '))
    Altura = float(input('Digite a altura do cômodo: '))

    comodo = Comodo(Comprimento, Largura, Altura)
    formato = comodo.return_format()

    resultado = Calculadora(comodo)

    print('Serão necessários {0:.2f} L de tinta para pintar as paredes'
          'e o teto'.format(resultado.calcular_area_comprimento()))
while True:
    main()
    if 'S' in str(input('Deseja recalcular? (S/N)\n')):
        pass
    else:
        break