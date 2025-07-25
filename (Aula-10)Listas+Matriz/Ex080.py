# Lista Ordenada sem sort()
print('LISTA ORDENADA:')
numeros = []

for i in range(0, 5):
    num = int(input(f'\nDigite o {i+1}º numero: '))

    if i == 0:
        numeros.append(num)
        print('Numero adicionado ao final da lista...')

    elif num > numeros[-1]:
        numeros.append(num)
        print('Numero adicionado no final da lista...')

    else:
        p = 0
        while p < len(numeros):
            if num <= numeros[p]:
                numeros.insert(p, num)
                print(f'Numero adicionado na posição: {p+1}...')
                break
            p += 1

print('\nResultado:')
print(f'Sua Lista:', end = ' ')
for n in numeros:
    print(f'[{n}]', end = ' ')
