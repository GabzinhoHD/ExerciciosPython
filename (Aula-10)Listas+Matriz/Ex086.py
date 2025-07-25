# Matriz v1
print('MATRIZ:\n')

matriz = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite o valor([{l}], [{c}]): '))
        matriz[l].append(num)

print('\nResultado:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end = ' ')
    print('\n')