# Aproveitamento de um jogador
print('GERENCIAMENTO DE UM JOGADOR:\n')
jogador = {}

jogador["Nome"] = input('Nome do jogador: ')

partidas = int(input('Quantas partidas ele jogou: '))
gols = []
total = 0

for p in range(0, partidas):
    gols.append(int(input(f'| Quantidade de gols na {p + 1}ª partida: ')))
    total += gols[p]

jogador["Gols"] = gols
jogador["Total"] = total

print('\nResultado:')
print(f'Nome do jogador: {jogador["Nome"]}')
for p in range(0, partidas):
    print(f'Gols da {p + 1}ª partida: {jogador["Gols"][p]}')

print(f'Total de gols: {total}')