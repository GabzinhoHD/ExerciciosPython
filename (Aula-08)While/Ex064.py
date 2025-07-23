# Tratando varios numeros v1
print('SOMADOR DE N VALORES:\n')

num = int(input('Digite um numero: '))
soma = 0
qtd = 1
while num != 999:
    soma += num
    qtd += 1
    num = int(input('Digite outro numero(999 encerra): '))
 

print('\nResultado:')
print(f'Você digitou: {qtd} numeros!')
print(f'A soma de todos eles(exceto 999) é: {soma}')