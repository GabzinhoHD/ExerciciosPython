# Progressão Aritmetica v3

print('PROGRESSÃO ARTIMETICA:\n')

primeiro = termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão: '))
posicao = 10
decimo = primeiro + (posicao - 1) * razao
continua = ''

print('\nResultado: ')
while continua != 'N':
    if continua == '':
        while termo != decimo:
            print(termo, end = ' ,')
            termo += razao

    else:
        while termo != enesimo:
            print(termo, end = ' ,')
            termo += razao

    continua = input('\nContinuar?(S/N): ').upper()
    if continua == 'S':
        num = int(input('Mais quantos termos?: '))
        posicao += num
        enesimo = primeiro +((posicao) - 1) * razao


