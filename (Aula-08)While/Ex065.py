# Tratando numeros v2
print('MEDIA D EN VALORES:\n')

num = int(input('Digite o 1º numero: '))
soma = 0
qtd = 1
continua = ''
maior = menor = num # Define num como maior e menor valor

while continua != 'N':
    soma += num
    # Determinação do maior e menor
    if num > maior:
        maior = num

    elif num < menor:
        menor = num

    continua = input('\nContinua?(S/N): ').upper()
    if continua == 'S':
        qtd += 1
        num = int(input(f'Digite o {qtd}º numero: '))
    

media = soma / qtd

print('\nResultado:')
print(f'A media dos numeros digitados foi: {media:.1f}')
print(f'O maior numero foi: {maior}')
print(f'O menor numero foi: {menor}')