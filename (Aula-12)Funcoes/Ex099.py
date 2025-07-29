# Maior numero
print('MAIOR NUMERO:')
numeros = []
maior = 0

def maior(numeros):
    for i, n in enumerate(numeros):
        if i == 0:
            maior = n
        else:
            if n > maior:
                maior = n

    print(f'Foram analisados {len(numeros)} numeros!')
    print(numeros)
    print(f'O maior valor entre eles é: {maior}!')


while True:
    numeros.append(int(input('\nDigite um numero: ')))
    continua = input('Continua?(S/N): ')
    if continua in 'Nn':
        break

print('\nResultado:')
maior(numeros)