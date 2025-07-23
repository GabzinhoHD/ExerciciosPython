# Jogo de Adivinhação v2
from random import randint
print('ACERTE O NUMERO:\n')

maquina = randint(0, 10)
continua = ''

while continua != 'N':
    escolha = int(input('Digite um numero: '))

    if escolha != maquina:
        print('\nVocẽ errou!!, Tente de novo...')
    
    if escolha == maquina:
        print('\nParabens vocẽ acertou!!')
        continua = input('Deseja continuar?(S/N): ').upper()
        maquina = randint(0, 10)
