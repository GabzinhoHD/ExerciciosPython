# Par ou Impar (jogo)
from random import randint
print('PAR OU IMPAR:\n')

maquina = randint(0, 10)
num = int(input('Digite seu numero: '))
escolha = ''
qtd = 0
soma = 0

while True:
    soma = num + maquina

    while escolha != 'P' and escolha != 'I':
        escolha = input('Par ou Impar (P/I) ').upper()

    if escolha == 'P' and (soma % 2) == 0:
        print('\nParabens!!')
        print(f'A maquina mostrou: {maquina}')
        print(f'{num} + {maquina} é PAR!!\n')
        qtd += 1
        escolha = ''
        # Nova Entrada
        maquina = randint(0, 10)
        num = int(input('Digite seu numero: '))
        while escolha != 'P' and escolha != 'I':
            escolha = input('Par ou Impar (P/I) ').upper()
    
    elif escolha == 'I' and (soma % 2) == 1:
        print('\nParebens!!')
        print(f'A maquina mostrou: {maquina}')
        print(f'{num} + {maquina} é IMPAR!!\n')
        qtd += 1
        escolha = ''

        #Nova Entrada
        maquina = randint(0, 10)
        num = int(input('Digite seu numero: '))
        while escolha != 'P' and escolha != 'I':
            escolha = input('Par ou Impar (P/I) ').upper()
        
    else:
        print('\nDERROTA!!')
        print(f'A maquina mostrou: {maquina}')
        break

print('\nResultado:')
print(f'Você ganhou {qtd} partidas!')