#Catetos e Hipotenusa
from math import hypot
print('HIPOTENUSA:  \n')

cateto_oposto =float(input('Digite o Cateto 0posto: '))
cateto_adjacente = float(input('Digite o Cateto Adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('\nResultado:')
print(f'O valor da hipotenusa desse triangulo retangulo é: {hipotenusa}')
