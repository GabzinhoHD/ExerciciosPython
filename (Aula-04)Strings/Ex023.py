# Separando um Numero
print('SEPARADOR DE DIGITOS(max: 9999):\n')

num = int(input('Digite um numero: '))
num = str(num)

print('\nResultado:')
print(f'O numero {num} tem:')
print(f'| Unidade: {num[3]}')
print(f'| Dezena: {num[2]}')
print(f'| Centena: {num[1]}')
print(f'| Milhar: {num[0]}') 
