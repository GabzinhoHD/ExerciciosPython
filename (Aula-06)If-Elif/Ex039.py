# Alistamento Militar
from datetime import date
print('TEMPO PARA SE ALISTAR\n')

nascimento = int(input('Digite o ano que voce nasceu: '))
ano = date.today().year

idade = ano - nascimento

print('\nResultado')
if idade > 18:
    print(f'Você deveria ter se alistado a {idade - 18} anos atras!!')

elif idade < 18:
    print(f'Faltam {18 - idade} anos para você se alistar!!')

else:
    print('Esse ano você deve se alistar!!')