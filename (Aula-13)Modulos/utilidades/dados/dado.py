# Validação de entrada
# Ex 112
from utilidades.moeda import moeda
def leiaDinheiro(msg):
    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print(f'\033[1;31mERRO!! {n} não é um valor numerico!\033[m')



    