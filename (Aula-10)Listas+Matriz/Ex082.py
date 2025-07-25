# Pares e Impares
print('NUMEROS PARES E IMPARES:\n')

numeros = []
pares = []
impares = []


continua = ''
while continua != 'N':
    num = int(input('\nDigite um numero: '))
    numeros.append(num)
    
    if (num % 2) == 0:
        pares.append(num)

    else:
        impares.append(num)

    continua = ''
    while continua != 'S' and continua != 'N':
        continua = input('Continua?(S/N): ').strip().upper()
        if continua != 'S' and continua != 'N':
            print('Entrada Invalida!!')

print('\nResultado:')

print('Lista inteira:', end = ' ')
for n in numeros:
    print(f'[{n}]', end = ' ')

print('\nLista dos pares:', end = ' ')
for p in pares:
    print(f'[{p}]', end = ' ')

print('\nLista dos impares:', end = ' ')
for i in impares:
    print(f'[{i}]', end = ' ')