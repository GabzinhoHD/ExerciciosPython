# Analise de grupo v2
print('ANALISE DE GRUPO:\n')

i = 0
cont_idade = 0
cont_masc = 0
cont_fem = 0

while True:
    i += 1
    sexo = ''

    print(f'\n{i}ª Pessoa')
    idade = int(input('| Qual sua idade: '))
    while sexo != 'F' and sexo != 'M':
        sexo = input('Qual seu sexo(F/M): ').upper()

    if idade >= 18:
        cont_idade += 1

    if sexo == 'M':
        cont_masc += 1
    
    if sexo == 'F' and idade < 20:
        cont_fem += 1

    continua = input('\nContinua?(S/N): ').upper()

    if continua == 'N':
        break

print('\nResultado:')
print(f'A {cont_idade} pessoas maiores de idade!')
print(f'A {cont_masc} pessoas do sexo masculino!')
print(f'A {cont_fem} pessoas do sexo feminino com menos de 20 anos!')