# Aumento Multiplos
print('AUMENTO DE SALARIO:\n')

salario = float(input('Digite o salario do funcionario: '))

print('\nResultado:')
if salario > 1250:
    print(f'Salario acima de R$1250.00. \nAumento de 10%: R${salario * 1.10:.2f}')
else:
    print(f'Salario abaixo de R$1250.00. \nAumento de 15%: R${salario * 1.15:.2f}')