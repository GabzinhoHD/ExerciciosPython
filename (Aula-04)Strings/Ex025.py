# Procurando uma string dentro de outra
print('SEU NOME TEM SILVA?:\n')

nome = input('Digite seu nome: ').strip()

print('\nResultado:')
print(f'Seu nome tem Silva?: {'SILVA' in nome.upper()}')
