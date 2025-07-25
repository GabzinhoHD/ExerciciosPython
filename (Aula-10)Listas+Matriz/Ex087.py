# Matriz v2
print('ANALISE DE DADOS DA MATRIZ:\n')
matriz = [[], [], []]
soma_pares = 0
soma_col_tres = 0

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite o valor([{l}], [{c}]): '))
        if (num % 2) == 0:
            soma_pares += num

        if c == 2:
            soma_col_tres += num

        if l == 1:
            if c == 0:
                maior = num
                
            else:
                if num > maior:
                    maior = num

        matriz[l].append(num)

print('\nResultado:')
print('Matriz:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end = ' ')
    print('\n')

print(f'Soma dos pares: {soma_pares}')
print(f'Soma da terceira coluna: {soma_col_tres}')
print(f'O maior valor da segunda linha: {maior}')