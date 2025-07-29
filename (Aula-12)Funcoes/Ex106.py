# Interative helping system
from time import sleep
def titulo():
    print('\033[1;31m')
    print('+=' * 10)
    print('  SISTEMA DE AJUDA')
    print('+=' * 10)
    print('\033[m')
   
def ajuda(comando):
    help(comando)
    
while True:
        titulo()
        comando = input('Insira o nome da função ou biblioteca: ')
        if comando.upper() == 'FIM':
            print('SAINDO...')
            sleep(1)
            break
        else:
            ajuda(comando)
            sleep(2)
