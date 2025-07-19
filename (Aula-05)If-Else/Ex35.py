# Analisando Triangulo v1
print('FORMA UM TRIANGULO?:\n')

a = float(input('Digite o valor da 1ª reta: '))
b = float(input('Digite o valor da 2ª reta: '))
c = float(input('Digite o valor da 3ª reta: '))

print('\nResultado: ')
if a + b > c and c + a > b and b + c > a:
    print('Forma-se um triangulo!!')
else:
    print('Impossivel formar um triagulo!!')