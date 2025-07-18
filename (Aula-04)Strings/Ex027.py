# Primeiro e ultimo nome
print('PRIMEIRO E ULTIMO NOME:\n')

nome = input('Digite seu nome completo: ').strip()
nome = nome.split()

print('\nResultado:')
print(f'Seu primeiro nome: {nome[0]}')
print(f'Seu ultimo nome: {nome[len(nome) - 1]}')
