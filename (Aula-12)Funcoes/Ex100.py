# Somando pares sorteados
from random import randint
from time import sleep
print('SOMANDO PARES:\n')
numeros = []

def sorteio():
    for i in range(0, 5):
        numeros.append(randint(0, 10))

    print('Sorteando numeros: ', end = '')
    for n in numeros:
        sleep(1)
        print(f'[{n}]', end = ' ', flush = 'False')
    print('FIM')

def soma(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos pares dos numeros sorteados é: {soma}')

sorteio()
print('-+' * 30)
print('Resultado:')
soma(numeros)