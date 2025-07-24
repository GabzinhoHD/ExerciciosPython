# Contando vogais

palavras = ('EU', 'GOSTO', 'DE', 'PROGRAMAR', 'EM',
            'LINGUAGEM', 'PYTHON', 'PORQUE', 'POSSO',
            'USAR', 'VARIAVEIS', 'STRING')
vogais = ()

for palavra in palavras: # Percorre a tupla
    for letra in palavra: # Percorre palavra

        if letra in 'AEIOU':
            vogais += (letra, ) # Adiciona as vogais a tupla
    
    print(f'\nNa palavra: {palavra} temos:', end = ' ')

    for vogal in vogais:
        print(f'{vogal} ', end = '')

    vogais = () #   Reseta a tupla para a proxima palavra

print('\nFIM...')