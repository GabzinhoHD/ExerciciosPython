#Ano Bissexto
from datetime import date
print('E UM ANO BISSEXTO?:\n')

ano = int(input('Digite o ano(digite 0 para ano atual): '))

if ano == 0:
    ano = date.today().year # Pega o ano atual da maquina

if (ano % 4) == 0:                      # Regra 1: é divisível por 4?
    if (ano % 100) == 0:                # Regra 2: é divisível por 100?
        if(ano % 400) == 0:             # Regra 3: se for divisivel por 100, tambem é por 400?
            validacao = 'é bissexto!'
        else:
            validacao = 'não é bissexto!'
    else:
        validacao = 'é bissexto!'
else:
    validacao = 'não é bissexto!'

print('\nResultado:')
print(f'{ano} {validacao}')
