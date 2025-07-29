# print "Especial"
print('PRINT BONITO:\n')

def escreva(msg):
    tam = 4 + len(msg)

    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva(input('Digite seu nome: ').upper())
