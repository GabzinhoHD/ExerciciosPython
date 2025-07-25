# Maior e menor na lista
print('MAIOR, MENOR EM LISTA:\n')

valores = []

for i in range(0, 5):
    valores.append(int(input(f'Digite o {i + 1}º numero: ')))
    if i == 0:
        maior = valores[0]
        menor = valores[0]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]


print('\nResultado:')
print(f'O maior valor foi: {maior},', end= ' nas posições: ')
for p, v in enumerate(valores):
    if v == maior:
        print(p + 1, end = ' ')

print(f'\nO menor valor foi: {menor},', end = ' nas posições: ')
for p, v in enumerate(valores):
    if v == menor:
        print(p + 1, end = ' ')