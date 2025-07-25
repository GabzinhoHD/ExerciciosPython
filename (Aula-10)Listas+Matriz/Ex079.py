# Valores unicos
print('LISTA NUMERICA:')

numeros = []

continua = ''
while continua != 'N':
    num  = int(input('\nDigite um numero: '))
    
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado!')

    else:
        print('Valor Duplicado! Não será adicionado!')

    continua = ''

    while continua != 'S' and continua != 'N':
        continua = input('Continua?(S/N): ').strip().upper()
        if continua != 'S' and continua != 'N':
            print('Entrada Invalida!!')
    
numeros.sort()

print('\nResultado:')
print(f'Sua lista:', end = ' ')
for n in numeros:
    print(f'[{n}]', end = ' ')
