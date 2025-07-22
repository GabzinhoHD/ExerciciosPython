# Tabuada v2
print('TABUADA:\n')

num = int(input('Digite um numero: '))
limite = int(input('Digite o numero limite: '))

print('\nResultado:')
for i in range(0, limite+1):
    print(f'{num} X {i} = {num*i}')