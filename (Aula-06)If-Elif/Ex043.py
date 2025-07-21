# IMC
print('QUAL O SEU IMC?:\n')

peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))

imc = peso / (altura * altura)

if imc < 18.5:
    status = 'ABIXO DO PESO'

elif imc >= 18.5 and imc < 25:
    status = 'PESO IDEAL'

elif imc >= 25 and imc < 30:
    status = 'SOBREPESO'

else:
    status = 'OBESIDADE MORBIDA'

print('\nResultado:')
print(f'IMC: {imc:.2f}, STATUS: {status}')