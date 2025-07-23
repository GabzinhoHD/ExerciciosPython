# Tabuada v3
print('TABUADAS:\n')

num = int(input('Digite a tabuada desejada: '))
while True:
    i = 0
    print('-' * 20)
    while i <= 10:
        print(f'{num} X {i} = {num * i}')
        i += 1
    print('-' * 20)

    num = int(input('Digite outra tabuada desejada(numeros negativos encerram): '))
    if num < 0:
        print('Saindo...')
        break