# Lista composta + analise de dados
print('ANALISE DE PESOS:\n')

grupo = []
pessoa = []

continua = ''
while continua != 'N':
    pessoa.append(input('Digite o nome: '))
    pessoa.append(input('Digite o peso(kg): '))

    if len(grupo) == 0:
        maior =  pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]

        elif pessoa[1] < menor:
            menor = pessoa[1]


    grupo.append(pessoa[:])
    pessoa.clear() # Reseta a lista pessoa

    continua = ''
    while continua != 'S' and continua != 'N':
        continua = input('Continua?(S/N): ').strip().upper()
        if continua != 'S' and continua != 'N':
            print('Entrada Invalida!!')

print('\nResultado:')
print(f'Ao todo foram cadastrados {len(grupo)} pessoas')

print(f'O maior peso foi: {maior}kg, de: ', end = '')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]}', end =', ')

print(f'\nO menor peso foi: {menor}kg')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]}', end =', ')