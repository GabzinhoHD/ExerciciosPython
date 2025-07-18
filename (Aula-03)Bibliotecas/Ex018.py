#Seno, Cosseno e Tangente
import math
print('SENO, COSSENO, TANGENTE DE UM ANGULO:\n')

angulo = float(input('Digite o valor do angulo: '))

seno = math.sin(math.radians(angulo))    # As funçoes(sin, cos, tan) retornar seus respectivos valores trigonometricos de (x) radianos.
cosseno = math.cos(math.radians(angulo)) # Por isso antes o valor angulo deve ser convertido para radianos
tangente = math.tan(math.radians(angulo))

print('\nResultado:')
print(f'Seno de {angulo}º é: {seno:.2f}')
print(f'Cosseno de {angulo}º é: {cosseno:.2f}')
print(f'Tangente de {angulo}º é: {tangente:.2f}')

