# Soma dos pares
print('SOMADOR DE PARES:\n')
soma = 0
for i in range(0, 6):
    num = int(input(f'Digite o {i+1}ª valor: '))
    if (num % 2) == 0:
        soma += num

print('\nResultado:')
print(soma)