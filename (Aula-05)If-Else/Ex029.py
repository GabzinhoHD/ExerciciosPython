# Radar Eletronico
print('VOCE FOI MULTADO?: \nMulta: R$7.00 para cada km/h acima de 80km/h\n')

velocidade = float(input('Digite quantos km/h você esta: '))

print('\nResultado:')
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'FOI MULTADO!!. \nValor da multa: R${multa:.2f}')
else:
    print('Fique tranquilo você não foi multado.')
