# Jogo da Adivinhação v1
from random import randint
print('ADIVINHE O NUMERO(0 a 5):\n')

num = randint(0, 5)
usuario = int(input('Digite seu chute(chance unica): '))

print('\nResultado:')
if num == usuario:
    print('Parabens! Você acertou!!')
else:
    print('Que triste! Você errou!!')
    print(f'O numero era: {num}')
