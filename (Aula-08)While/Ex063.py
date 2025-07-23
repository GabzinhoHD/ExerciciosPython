# Sequencia de fibonacci
print('FIBONACCI:\n')

n = int(input('Digite quantos termo deseja ver: '))
qtd = 0
num1 = 0
num2 = 1

print('\nResultado:')
while n != qtd:
    soma = num1 + num2
    var = num1
    num1 = soma
    num2 = var
    print(soma, end = ' - ')
    qtd+= 1

print('')