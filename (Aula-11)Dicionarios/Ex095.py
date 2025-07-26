## Aproveitamento de um jogadores v2
from time import sleep
print('GERENCIAMENTO DE UM JOGADORES:\n')

jogadores = []
jogador = {}

continua = ''
while continua != 'N':
    jogador["Nome"] = input(f'\nNome do jogador: ')

    partidas = int(input('Quantas partidas ele jogou: '))
    gols = []
    total = 0

    for p in range(0, partidas):
        gols.append(int(input(f'| Quantidade de gols na {p + 1}ª partida: ')))
        total += gols[p]

    jogador["Gols"] = gols
    jogador["Total"] = total
    jogadores.append(jogador, )

    jogador = {}

    continua = ''
    while continua != 'S' and continua != 'N':
        continua = input('Continua?(S/N): ').strip().upper()
        if continua != 'S' and continua != 'N':
            print('Entrada Invalida!!')


print('\nResultado:')
print('='*50)
print(f'{"No":<4}{"Nome":<15}{"Gols":<20}{"Total":>7}')
print('-'*50)

for n, v in enumerate(jogadores):
    print(f'{n:<4}{v["Nome"]:<15} {str(v["Gols"]):<20} {v["Total"]:>4}')
print('-'*50)

while True:
    opcao = int(input('Mostrar dados de qual jogador?(999 para parar): '))
    if opcao == 999:
        break

    print('-'*50)
    if opcao >= len(jogadores):
        print('ERRO!! Numero não encontrado!')
    
    else:
        print(f'Nome do jogador: {jogadores[opcao]["Nome"]}')
        for p, g in enumerate(jogadores[opcao]["Gols"]):
            sleep(0.5)
            print(f'Gols da {p + 1}ª partida: {[g]}')
    print('='*50)
sleep(0.5)
print('SAINDO...')