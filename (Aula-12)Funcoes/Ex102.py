# Fatorial
from math import factorial
print('FATORIAL:\n')

def fatorial(num, show):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f

num = int(input('Digite um numero: '))
show = input('Mostrar Calculo?(S/N): ')

if show in 'Ss':
    show = True

else: 
    show = False

print('\nResultado:')
print(fatorial(num, show))
