# Extraido dados da lista
print('ANALISE DA LISTA:\n')
numeros = []
cont = 0

continua = ''
while continua != 'N':
    numeros.append(int(input('\nDigite um numero: ')))
    cont += 1
    continua = ''

    while continua != 'S' and continua != 'N':
        continua = input('Continua?(S/N): ').strip().upper()
        if continua != 'S' and continua != 'N':
            print('Entrada Invalida!!')


numeros.sort(reverse = True)

if 5 in numeros:
    status = 'está na lista!'

else:
    status  ='não está na lista!'

print('\nResultado:')
print(f'Você digitou {cont} numeros!!')
print(f'A lista em ordem decrescente é: ')
for num in numeros:
    print(f'[{num}]', end = ' ')

print(f'\nO numero cinco[5] {status}')
    