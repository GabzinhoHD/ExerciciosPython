# Analisando um Texto
print('ANALISE DO NOME:\n')

nome = input('Digite seu nome completo: ').strip()
nome_dividido = nome.split()

print('\nResultado:')
print(f'Nome em Maiusculas: {nome.upper()}')
print(f'Nome em Minusculas: {nome.lower()}')
print(f'Total de letras no Nome: {len(nome) - nome.count(' ')}\n')
print(f'Primeiro Nome: {nome_dividido[0]}')
print(f'Total de letras no primeiro nome: {nome.find(' ')}')
