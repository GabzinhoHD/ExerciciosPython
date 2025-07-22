# É Palindromo?
print('DETECTOR DE PALINDROMO:\n')

frase = input('Digite algo: ').strip().upper().replace(' ', '')
inversao = ''

for letra in range(len(frase) - 1, -1, -1):
    inversao += frase[letra]

if inversao == frase:
    status = 'É um Palindromo'
else:
    status = 'Não é palindromo'

print('\nResultado:')
print(f'{status}')