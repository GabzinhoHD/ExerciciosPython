# Boletim Escolar
print('BOLETIM ESCOLAR:\n')
boletim = []

continua = ''
while continua != 'N':
    nome = input('Nome do aluno: ')
    nota1 = float(input('| Nota 1: '))
    nota2 = float(input('| Nota 2: '))
    media = (nota1 + nota2) / 2

    boletim.append([nome, [nota1, nota2], media])
    continua = ''
    while continua != 'S' and continua != 'N':
        continua = input('Continua?(S/N): ').strip().upper()
        if continua != 'S' and continua != 'N':
            print('Entrada Invalida!!')

print('='* 30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'* 30)
for n, a in enumerate(boletim):
    print(f'{n:<4}{a[0]:<10}{a[2]:>8.1f}')
print('='* 30)

continua = ''
while continua != 'N':
    opcao = int(input('Mostrar de notas de qual aluno?: '))

    if opcao <= len(boletim) - 1:
        print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1]}!!')
    else:
        print('Aluno não encontrado!!')

    continua = ''
    while continua != 'S' and continua != 'N':
        continua = input('Continua?(S/N): ').strip().upper()
        if continua != 'S' and continua != 'N':
            print('Entrada Invalida!!')
