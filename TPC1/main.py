from Model import Model
import matplotlib.pyplot as plt



    



# UI

dados = Model()
dados.readFile('myheart.csv')
option = 0
while option != 5:
    print('Qual a opção?')
    print('1 - Tabela dados')
    print('2 - Distribuição por sexo')
    print('3 - Distribuição por escalões etários')
    print('4 - Distribuição por níveis de colestrol')
    print('5 - Sair')
    op = input()
    if op.isdigit():
        option = int(op)
        if option > 0 and option < 6:
            if option == 1: print(dados)
            elif option == 2: dist_sexo(dados)
            elif option == 3: dist_escaloes(dados)
            elif option == 4: dist_colesterol(dados)
        else:
            print('Opção Inválida')
    else:
        print('Input Inválido')
            