# Estatisticas
print('CUSTO DE COMPRA:\n')

i = 0
qtd = 0
total = 0

while True:
    i += 1

    print(f'\n{i}º Produto')
    produto = str(input('| Qual so nome do produto: '))
    preco = float(input('| Quanto custa o produto: '))

    total += preco

    if preco > 1000: # Quantos produtos são custam mais que R$1000
        qtd += 1

    if i == 1: # Define o primeiro preço com menor valor
        menor = preco
    
    elif preco < menor: # Registra o nome no produto mais barato
        menor = preco
        barato = produto

    continua = input('\nContinua?(S/N): ').upper()

    if continua == 'N':
        break

print('\nResultado:')
print(f'O total gasto será: R${total:.2f}')
print(f'[{qtd}] produtos custam mais de R$1000.00')
print(f'O produto {barato} é o mais barato, custando: R${menor:.2f}')
