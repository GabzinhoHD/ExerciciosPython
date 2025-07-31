from lib.interface import *

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()

    except FileNotFoundError:
        return False
    
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO!! arquivo não foi criado')

    else:
        print('Arquivo criado!!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO!! arquivo não foi lido')

    else:
        titulo('CADASTROS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{nome[0]:<30}{nome[1]:>3}')

    a.close()

def cadastrar(arq, nome='desconhecido', idade='0'):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO!! arquivo não aberto')

    else:
        try:
            a.white(f'{nome};{idade}\n')
        except:
            print('ERRO!! cadastro não realizado')

        else:
            print(f'Novo cadastro de {nome} realizado com sucesso')

        a.close()