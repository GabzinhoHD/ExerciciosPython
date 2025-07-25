# Lista composta par e impar
print('LISTA PAR E IMPAR:\n')
numeros = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i+1}º numero: '))
    if (num % 2) == 0:
        numeros[0].append(num, )
        numeros[0].sort()
    else:
        numeros[1].append(num, )
        numeros[1].sort()

print('\nResultado:')
print(f'Numeros pares: ', end =' ')
for p in numeros[0]:
    print(f'[{p}]', end = ' ')

print('\nNumeros impares:', end = ' ')
for i in numeros[1]:
    print(f'[{i}]', end = ' ')