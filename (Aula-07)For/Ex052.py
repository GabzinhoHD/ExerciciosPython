# Numeros Primos
print('É PRIMO?:\n')

num = int(input('Digite um numero: '))

status = 'é primo'

for i in range (2, num):
    if (num % i) == 0:
        status = 'não é primo'

print('\nResultado:')
print(f'{num} {status}')