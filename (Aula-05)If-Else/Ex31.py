#Custo de Viagem
print('PREÇO DA VIAGEM:\n')

km = float(input('Digite a distancia(km) da viagem: '))

if km <= 200:
    custo = km * 0.50
else:
    custo = km * 0.45

print('\nResultado:')
print(f'A viagem custara: R${custo:.2f}')