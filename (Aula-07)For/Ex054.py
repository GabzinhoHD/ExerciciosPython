# Grupo de Maioridade
from datetime import date
print('CONTADOR DE MAIORIDADE:\n')

qtd = 0
for pessoa in range(0, 7):
    ano = int(input(f'Digite seu ano de nascimento({pessoa+1}ª pessoa): '))
    if (date.today().year - ano) < 18:
        qtd += 1

print('\nResultado:')
print(f'Ao todo {qtd} pessoas não são maiores de idade!')