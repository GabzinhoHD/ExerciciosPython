# Analise de dados em tuplas
print('ANALISE DE DADOS:\n')
numeros = () # tuplas vazias
pares = ()

for i in range(0, 4):
    num = int(input(f'Digite o {i+1}º numero: '))
    numeros = numeros + (num,) # inserindo valores na tupla

    if (num % 2) == 0:
        pares += (num,)

if 3 in numeros:
    posicao = str(numeros.index(3) + 1) + 'ª' # Concatenação para ficar bonito

else:
    posicao = 'em nenhuma'


print('\nResultado:')
print(f'O nove[09] aparece: {numeros.count(9)} vezes')
print(f'O primeiro tres[03] esta {posicao} posição')
print('Numeros pares: ')
for i in pares:
    print(f'| [{i}]')