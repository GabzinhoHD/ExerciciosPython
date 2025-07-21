# Classificando atletas
from datetime import date
print('CATEGORIA DOS ATLETAS:\n')

nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento

if idade <= 9:
    categoria = 'MIRIM'

elif idade <= 14:
    categoria = 'INFANTIL'

elif idade <= 19:
    categoria = 'JUNIOR'

elif idade <= 20:
    categoria = 'SENIOR'

else:
    categoria = 'MASTER'

print('\nResultado:')
print(f'O atleta com idade de {idade} esta na categoria {categoria}')