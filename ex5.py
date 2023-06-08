from ex5_ui import *
# OUTRA MANEIRA DE IMPORTAR: from ex5_ui import as ui (RENOMEAR A FUNÇÃO)

opcao = obter_opcao()

if opcao == 1:
    area = tratar_quadrado()
elif opcao == 2:
    area = tratar_circulo()
elif opcao == 3:
    area = tratar_triangulo()
else:
    print("Escolha invalída, selecione uma das opções do Menu")

print(f'A área é {area:.2f}')
