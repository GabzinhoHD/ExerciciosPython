# Analisando um Triangulo v2
print('QUAL E O TIPO DO TRIAGULO:\n')

a = float(input('Qual o comprimento(m) da 1ª reta: '))
b = float(input('Qual o comprimento(m) da 2ª reta: '))
c = float(input('Qual o comprimento(m) da 3ª reta: '))

print('\nResultado:')
if a == b and b == c:
    print('O triangulo é Equilatero!!')

elif a == b and b != c or b == c and c != a or a == c and c != b:
    print('O triangulo é Isosceles!!')

else:
    print('O triangulo é Escaleno!!')