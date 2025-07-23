# Fatorial
from math import factorial
print('CALCULO FATORIAL:\n')

num = int(input('Digite um numero: '))
fat = factorial(num)

print('\nResultado:')
print(f'{num}! = ', end = '')
while num != 0:
    print(num, end = '')

    if num != 1:
        print(' x ', end = '')
    else:
        print(' = ', end = '')
    num -= 1

print(fat)
