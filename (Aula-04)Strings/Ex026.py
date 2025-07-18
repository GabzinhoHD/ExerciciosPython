# Ocorrencias de uma string
print('POSIÇÕES DE "A":\n')

frase = input('Digite uma frase: ').upper() # Torna a frase tuda maiuscula 
primeiro = frase.find('A')
ultimo = frase.rfind('A') # (rfind) começa do ultimo espaço da string

print('\nResultado:')
print(f'Frase: {frase}')
print(f'| Quantidade de "A": {frase.count('A')} ')
print(f'| Posição do primeiro "A": {primeiro + 1}')
print(f'| Posição do ultimo "A": {ultimo + 1}')
