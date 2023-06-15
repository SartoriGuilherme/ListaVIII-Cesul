from funcoes_ex8 import *


def obter_opcao() -> int:
    print("Olá, escolha uma das opções:\n"
          "1- Calcular combinação\n"
          "2- Calcular arranjo\n"
          "3- Sair")

    return int(input('==> '))


def tratar_combinacoes():
    n = int(input('Informe o número de elementos (n): '))
    p = int(input('Informe o número de agrupamentos (p) '))

    result = calcular_combinacoes(n, p)
    print(f'O total de combinações é {result:.1f}')


def tratar_arranjos():
    n = int(input('Informe o número de elementos (n): '))
    p = int(input('Informe o número de agrupamentos (p) '))

    result = calcular_arranjos(n, p)
    print(f'O total de arranjos é {result:.1f}')
