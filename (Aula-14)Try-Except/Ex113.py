# Validação de valores v2
print('VALIDAÇÃO DE NUMEROS:\n')

def leiaInt(msg):
    while True:
        try: 
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!! Tente novamente com um valor inteiro!\033[m\n')
            continue
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try: 
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!! Tente novamente com um valor real!\033[m\n')
            continue
        else:
            return n

num_int = leiaInt('Digite um numero: ')
num_float = leiaFloat('Digiter um numero real: ')

print('\nResultado:')
print(f'{num_int} é um inteiro!\n{num_float} é um numero real(float)')