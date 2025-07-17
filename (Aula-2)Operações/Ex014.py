# Calculando conversão de temperaturas
print('CONVERSOR DE TEMPERATURA: \n(celsius para Fahrenheit)\n')

cel = float(input('Digite a temperatura em Celsius(ºC): '))

fah = (cel * 1.8) + 32

print('\nResultado:')
print(f'{cel}°C em Fahrenheit é: {fah:.1f}ºF ')