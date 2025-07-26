# Jogo de Dados
from random import randint
from time import sleep
from operator import itemgetter
print('JOGO DE DADOS:\n')
jogadores = {
    "1º Jogador": randint(1, 6),
    "2º Jogador": randint(1, 6),
    "3º Jogador": randint(1, 6),
    "4º Jogador": randint(1, 6),
}
ranking = {}
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True)

print('Valores Sorteados:')
for k, v in jogadores.items():
    sleep(1)
    print(f'| {k} tirou: {v}')
    
print('\nRanking dos jogadores:')
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'| {i + 1}º posição: {v[0]}')