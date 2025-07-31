from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'Cadastros.txt'

if not arquivoExiste(arquivo): 
    criarArquivo(arquivo)

items = ['Cadastrar pessoas', 'Mostrar Cadastros', 'Sair']

while True:
    resp = menu(items)

    if resp == 1:
        titulo('NOVO CADASTRO')
        nome = input('Digite o nome: ')
        idade = leiaInt('Digite a idade: ')
        cadastrar(arquivo, nome, idade)

    elif resp == 2:
        lerArquivo(arquivo)

    elif resp == 3:
        print('\033[1;33mSAINDO...')
        sleep(1)
        break

    else:
        print('\033[1;31mERRO!! Entrada invalida!\033[m')
    sleep(1)