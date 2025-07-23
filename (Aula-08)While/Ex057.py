# Validação
print('VALIDAÇÃO BASICA:\n')
sexo = ''


while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo(M/F): ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Entrada Invalida!!\n')

print('\nEntrada Correta!!')