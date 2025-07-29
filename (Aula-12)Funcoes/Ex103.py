# Paremetros opcionais
print('FICHA DE JOGADOR')

def ficha(nome ='DESCONHECIDO', gols = 0):
    print(f'O jogador {nome} fez {gols} no campeonato!')

nome = input('Nome do jogador: ')
gols = input('Quantos gols ele fez: ')

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome.strip() == '':
    ficha(gols=gols)
    
else:
    ficha(nome, gols)