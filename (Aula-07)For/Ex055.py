# Maior, Menor em uma sequencia
print('MAIOR E MENOR PESO:\n')

for pessoa in range(0, 5):
    peso = float(input(f'Digite seu peso em Kg({pessoa+1}ª pessoa): '))
    if pessoa == 0:
        maior = peso
        menor = peso
    else: 
        # Determinção do maior peso
        if peso > maior:
            maior = peso
        # Determinação do menor peso
        elif peso < menor:
            menor = peso

print('\nResultado:')
print(f'O maior peso foi: {maior} kg')
print(f'O menor peso foi: {menor} kg')
