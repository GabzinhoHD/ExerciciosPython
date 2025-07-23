# (Ex064) com break
print('SOMADOR DE N VALORES:\n')

num = int(input('Digite um numero: '))
soma = 0
qtd = 1

while True:
    soma += num
    num = int(input('Digite outro numero(999 encerra): '))
    if num == 999:
        break
    
    qtd += 1

print('\nResultado:')
print(f'Você digitou: {qtd} numeros!')
print(f'A soma de todos eles(exceto 999) é: {soma}')