# Times de futebol
print('TABELA DE TIMES:\n')

times = ('Cruzeiro', 'Flamengo', 'Palmeiras', 'Bragantino', 'Botafogo',
        'Bahia', 'Mirassol', 'Fluminense', 'Atletio-MG', 'Internacional',
        'Corinthians', 'Ceara SC', 'Gremio', 'Sao Paulo', 'EC Vitoria',
        'Vasco da Gama', 'Santos', 'Juventude', 'Fortaleza', 'Sport Recife')

print('Tabela por colocação:')
for time in times:
    print(f'| [{time}]')

print('\nTOP 5:')
for i in range(0, 5):
    print(f'| {i+1}º - {times[i]}')

print('\nUltimos 4:')
for i in range(5, 1, -1):
    print(f'| {22-i}º - {times[-i]}')

print('\nOrdem Alfabetica:')
for time in sorted(times):
    print(f'| [{time}] ')

print('\nPosição da Chapecoense:')
busca = 'Chapecoense'
if busca in times:
    print(f'| {i+1}ª Posição')
else:
    print('Fora da tabela dos 20 primeiros!!')