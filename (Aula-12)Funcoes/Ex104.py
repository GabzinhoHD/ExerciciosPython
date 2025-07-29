# Validação de valores
print('VALIDAÇÃO DE INTEIROS:\n')

def leiaInt(msg):
    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            return valor
        
        else:
            print(f'\033[1;31mERRO!! {n} não é um valor numerico!\033[m')


num = leiaInt('Digite um numero: ')
print(f'{num} é um numero!!')