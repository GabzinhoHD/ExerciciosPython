# Menu de operações
from time import sleep
print('OPERAÇÕES:\n')

opcao = 0
num1 = float(input('Digite o 1º valor: '))
num2 = float(input('Digite o 2º valor: '))

while opcao != 5:
    print('\nMenu: ')
    print('| [1] Somar')
    print('| [2] Multiplicar')
    print('| [3] Maior numero')
    print('| [4] Novos numeros')
    print('| [5] Sair')

    opcao = int(input('Digite uma opção: '))

    print('\nResultado:')
    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')    

    elif opcao == 2:
        print(f'{num1} X {num2} = {num1 * num2}')
    
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é o maior valor!')

        else:
            print(f'{num2} é o maior valor!')
        
    elif opcao == 4:
        num1 = float(input('Digite o 1º valor: '))
        num2 = float(input('Digite o 2º valor: '))

    else:
        print('Saindo...')

    sleep(1)