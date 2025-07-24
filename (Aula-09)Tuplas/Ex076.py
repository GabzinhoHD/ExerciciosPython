# Lista de preços
print('='* 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('='* 40)
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for i in range(0, len(produtos)):
    if (i % 2) == 0:
        print(f'{produtos[i]:.<30}', end = ' ')
    elif (i % 2) == 1:
        print(f'R$ {produtos[i]:3.2f}')

print('='* 40)