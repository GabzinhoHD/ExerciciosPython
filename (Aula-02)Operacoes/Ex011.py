# Calculo de consumo para pintar parede

print('CONSUMO DE PINTA PARA PAREDE:\n')

altura = float(input('Digite a altura da sua parede: '))
largura = float(input('Digite a largura da sua parede: '))

parede = largura * altura
tinta = parede / 2

print('\nResultado:')
print('OBS: 1L pinta 2m²')
print(f'As dimensões da parede são {largura}m X {altura}m. Com uma aréa de: {parede}m² ')
print(f'Você precisara de {tinta}L de tinta.')
