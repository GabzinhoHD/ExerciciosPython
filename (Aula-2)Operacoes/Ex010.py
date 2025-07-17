"""
Conversor de Moedas
Cotação usada: U$ 1.00 = R$ 3.27
Que inveja dessa cotação viu!!
"""
print('CONVERSOR DE MOEDAS(R$ PARA U$):\n')

real = float(input('Digite o valor em real: '))
dolar = real / 3.27

print('\nResultado:')
print(f'R$ {real:.2f} = U$ {dolar:.2f}')
