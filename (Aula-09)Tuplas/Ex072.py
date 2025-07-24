# Numeros por extenso
print('POR EXTENSO:\n')

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
num = -1

while num < 0 or num > 20:
    num = int(input('Digite um numero(0 a 20): '))

    print('\nResultado:')
    if num > 0 and num < 20:
        for i in range(0, len(numeros)):
            if num == i:
                print(f'{num} por extenso é: {numeros[i]}')

    else:
        print(f'Numero {num} invalido. Tente Novamente!!\n')