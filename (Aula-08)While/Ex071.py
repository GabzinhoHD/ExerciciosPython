# Caixa Eletronico
print('CAIXA ELETRONICO:\n')

valor = int(input('Digite o valor a ser sacado: R$'))
cedula = 50
total = 0

print('\nResultado:')
while True:
    if valor >= cedula:
        valor -= cedula
        total += 1

    else:
        if total > 0:
            print(f'Total de {total} cedulas de R${cedula}')

        if cedula == 50:
            cedula = 20
        
        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1

        total = 0
        if valor == 0:
            break