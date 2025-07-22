# Soma multiplos de trẽs
print('SOMA DOS MULTIPLOS IMPARES DE 3 (1 a 500):\n')
soma = 0

for num in range(1, 501):
    if (num % 2) == 1 and (num % 3) == 0:
        soma = soma + num

print('\nResultado')
print(soma)