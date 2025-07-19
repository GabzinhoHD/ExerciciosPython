# Quebrando um numero
from math import trunc
print('\033[1;33;40mPARTE INTEIRA DE UM VALOR REAL:\033[m\n')

num = float(input('Digite um numero decimal: '))

print('\nResultado:')
print(f'A parte inteira de {num} é: {trunc(num)}')
