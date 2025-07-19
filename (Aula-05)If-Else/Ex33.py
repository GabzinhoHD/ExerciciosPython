# Maior e menor valor
print('QUAL E O MAIOR E MENOR VALOR:\n')

num1 = float(input('Digite o 1º numero: '))
num2 = float(input('Digite o 2º numero: '))
num3 = float(input('Digite o 3º numero: '))
maior = num1
menor = num1

# Validação do maior
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Validação do menor
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print('\nResultado:')
print(f'O menor valor é: {menor:.2f}')
print(f'O maior valor é: {maior:.2f}')
