#Catetos e Hipotenusa
from math import hypot
print('\033[1;33;40mHIPOTENUSA:\n')

cateto_oposto =float(input('Digite o Cateto 0posto: '))
cateto_adjacente = float(input('Digite o Cateto Adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('\n\033[1;31;40mResultado:')
print(f'O valor da hipotenusa desse triangulo retangulo é: {hipotenusa}')
