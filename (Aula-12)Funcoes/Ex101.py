# Validação para votação
from datetime import date
print('SUA SITUAÇÃO PARA VOTAR:\n')

def voto(idade):
    if idade >= 18:
        return 'VOTO OBRIGATORIO!'
    elif idade >= 16 or idade > 70:
        return 'VOTO OPCIONAL!'
    else: 
        return 'NÃO VOTA!'

idade = date.today().year - int(input('Seu ano de nascimento: '))

print('\nResultado:')
print(f'Com {idade}:', end = ' ')
print(voto(idade))