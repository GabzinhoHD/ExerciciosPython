# Analise de grupo
print('ANALISE DE UM GRUPO DE 4 PESSOAS:')
qtd = 0
soma= 0
for pessoa in range(0, 4):
    print(f'\n{pessoa+1}ª pessoa:')
    nome = input('| Digite seu nome: ')
    idade = int(input('| Digite sua idade: '))
    sexo = input('| Digite seu sexo(F/M): ')

    soma += idade

    if sexo.upper() == 'M':
        if pessoa == 0:
            maior = idade
        else: 
        # Determinção do nome no homem mais velho
            if idade > maior:
                maior = idade
                velho = nome

    if sexo.upper() == 'F':
        if idade < 20:
            qtd += 1

media = soma / 4

print('\nResultado:')
print(f'A media das idades do grupo é: {media}')
print(f'O nome do homem mais velho é: {velho}')
print(f'O numero de mulheres com menos de 20 anos é: {qtd}')