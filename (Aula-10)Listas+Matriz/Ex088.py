# Mega Sena
from random import randint
print('PALPITES MEGA-SENA:\n')
palpites = []

jogos = int(input('Quantos jogos quer sortear?: '))

for jogo in range(0, jogos):
    palpites.append([], )
    for p in range(0, 6):
        num = randint(0, 60)
        palpites[jogo].append(num)


print('\nResultado:')
for l in range(0, jogos):
    print(f'Jogo {l+1}:', end = ' ')
    for c in range(0, 6):
        print(f'[{palpites[l][c]}]', end = ' ')
    print('\n')