# Progressão aritmetica
print('PROGRESSÃO ARITMETICA:\n')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da progressão: '))
decimo = primeiro + (10 -1) * razao

soma = 0
print('\nResultado:')
for termo in range(primeiro, decimo + razao, razao):
    print(termo, end = ' ,')

print('...')
