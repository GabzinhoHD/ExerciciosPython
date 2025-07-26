# Unindo dict + lista
print('ANALISE DE GRUPO:\n')

grupo = []
pessoa = {}
soma = 0

continua = ''
while continua != 'N':
    pessoa["Nome"] = input('\nNome: ')
    pessoa["Idade"] = int(input('Idade: '))
    soma += pessoa["Idade"]

    while True:
        pessoa["Sexo"] = input("Sexo(M/F): ").upper()
        if pessoa["Sexo"] == 'F' or pessoa["Sexo"] == 'M':
            break
        else:
            print('Entrada Invlaida!!\n')

    grupo.append(pessoa, )
    pessoa = {} # Reseta o dicionario apos armazena-lo na lista

    continua = ''
    while continua != 'S' and continua != 'N':
        continua = input('Continua?(S/N): ').strip().upper()
        if continua != 'S' and continua != 'N':
            print('Entrada Invalida!!')

media = soma / len(grupo)

print('\nResultado:')
print(f'O grupo tem {len(grupo)} pessoas')
print(f'A media das idades é: {media:.2f}')

print('Mulheres cadastradas: ', end = '')
for p in grupo:
    if p["Sexo"] == 'F':
        print(p["Nome"], end = ' ')
    
print('\nPessoas mais velhas que a media:', end = ' ')
for p in grupo:
    if p["Idade"] > media:
        print(p["Nome"], end = ' ')