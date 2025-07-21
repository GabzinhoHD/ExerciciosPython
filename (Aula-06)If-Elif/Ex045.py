# Jokenpô(Pedra, Papel, Tesoura)
from random import randint
print('='*13)
print('\nJOKENPÔ:')

print('| [1] Pedra')
print('| [2] Papel')
print('| [3] Tesoura')
print('\n' + ('='*13))

escolha = int(input('Qual sua escolha: '))
maquina = randint(1, 3)

print('\nResultado:')
if escolha == maquina:
    print('EMPATE!! \nA maquina escolheu o mesmo que você!!')

    """Usuario escolhe Pedra"""
elif escolha == 1 and maquina == 2:
    print('DERROTA!!')
    print('A maquina escolheu Papel!')

elif escolha == 1 and maquina == 3:
    print('VITORIA!!')
    print('A maquina escolheu Tesoura!')

    """Usuario escolhe Papel"""
elif escolha == 2 and maquina == 3:
    print('DERROTA!!')
    print('A maquina escolheu Tesoura!')

elif escolha == 2 and maquina == 1:
    print('VITORIA!!')
    print('A maquina escolheu Pedra!')
    
    """Usuario escolheu Tesoura"""
elif escolha == 3 and maquina == 1:
    print('DERROTA!!')
    print('A maquina escolheu Pedra!')

elif escolha == 3 and maquina == 2:
    print('VITORIA!!')
    print('A maquina escolheu Papel!')