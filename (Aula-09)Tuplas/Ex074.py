# Maior e menor em tuplas
from random import randint
print('MAIOR, MENOR DA TUPLA:\n')

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))


print(f'Numeros gerados:', end = '')
for num in numeros:
    print(f' [{num}] ', end = '')

print('\n\nResultado:')
print(f'{max(numeros)} foi o maior numero gerado') # Metodos proprio das tuplas para maior e menor valor
print(f'{min(numeros)} foi o menor numero gerado')