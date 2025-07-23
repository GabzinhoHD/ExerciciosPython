# Progressão Aritmetica v2
print('PROGRESSÃO ARTIMETICA:\n')

primeiro = termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão: '))
decimo = primeiro + (10 - 1) * razao

print('\nResultado: ')
while termo != decimo:
    print(termo, end = ' ,')
    termo += razao

print('...')