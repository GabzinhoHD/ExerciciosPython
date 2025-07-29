# Operações de Formatação
# Para o Ex111 e Ex 112
"""
# Ex107
def metade(n):
    return n / 2

def dobro(n):
    return n * 2

def aumento(n, v):
    v  = (v + 100) / 100
    a = n * v
    return a

def diminuir(n, v):
    v = (100 - v) / 100
    d = n * v
    return d

# Ex108
def formatar(n):
    f = f'R${n:.2f}'
    return f

"""

# Ex 0109
def metade(n, f=False):
    n = n / 2
    if f == True:
        n = f'R${n:4.2f}'
    return n
    
def dobro(n, f=False):
    n = n * 2
    if f == True:
        n = f'R${n:4.2f}'
    return n

def aumento(n, v, f=False):
    v  = (v + 100) / 100
    a = n * v
    if f == True:
        a = f'R${a:4.2f}'
    return a

def diminuir(n, v, f=False):
    v = (100 - v) / 100
    d = n * v
    if f == True:
        d = f'R${d:4.2f}'
    return d


#Ex110
def resumo(n, a, d):
    met = metade(n, True)
    dobrado = dobro(n, True)
    aum = aumento(n, a, True)
    dim = diminuir(n, d, True)
    n = f'R${n:4.2f}'

    print('=' * 40)
    print(f'{"RESUMO DO PREÇO":^40}')
    print('-' * 40)
    print(f'{"Preço analisado:":<25}{n:>15}')
    print(f'{"Dobro do preço:":<25}{dobrado:>15}')
    print(f'{"Metade do preço:":<25}{met:>15}')
    print(f'{f"{a}% de aumento:":<25}{aum:>15}')
    print(f'{f"{d}% de redução:":<25}{dim:>15}')
    print('=' * 40)